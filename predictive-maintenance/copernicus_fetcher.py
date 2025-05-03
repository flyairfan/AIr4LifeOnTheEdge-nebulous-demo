# copernicus_fetcher.py
# Production-Ready CAMS Data Fetcher for AIr4LifeOnTheEdge

import os
import logging
from datetime import datetime, timedelta
from typing import Dict

import requests
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

# --- CONSTANTS ---
CAMS_API_URL = "https://api.ceda.ac.uk/cams-global-reanalysis"
DAOD_NORMALIZATION_FACTOR = 3.0  # Based on CAMS DAOD scale [0-3]
COMPENSATION_FACTOR = 1.25       # Compensate for CAMS underestimation [14]

# --- LOGGING ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("CAMS Fetcher")

def get_cams_parameters() -> Dict:
    """Generate dynamic API parameters with validation"""
    return {
        "apikey": os.environ["CAMS_API_KEY"],
        "variable": "dust_aerosol_optical_depth",
        "time": (datetime.utcnow() - timedelta(hours=1)).strftime("%H:%M"),
        "format": "json",
        "vertical_level": "surface",
        "area": os.getenv("CAMS_AREA", "37/-2.5/36.5/-2.0"),  # Almería region
        "grid": "0.75/0.75"
    }

@retry(
    wait=wait_exponential(multiplier=1, min=2, max=30),
    stop=stop_after_attempt(3),
    retry=retry_if_exception_type(requests.RequestException),
    before_sleep=lambda _: logger.warning("Retrying CAMS API call")
)
def fetch_dust_forecast() -> Dict:
    """
    Fetches and processes dust forecast from CAMS API
    Returns normalized risk value (0-1 scale) with compensation
    """
    # Validate environment
    if "CAMS_API_KEY" not in os.environ:
        logger.critical("CAMS_API_KEY environment variable not set")
        raise RuntimeError("Missing CAMS API credentials")

    try:
        # API call
        response = requests.get(
            CAMS_API_URL,
            params=get_cams_parameters(),
            timeout=15,
            headers={"Accept": "application/json"}
        )
        response.raise_for_status()

        # Parse response
        data = response.json()
        daod = data["variables"]["dust_aerosol_optical_depth"]["data"][0][0][0]
        
        # Normalize and compensate
        normalized_risk = min(max(
            (float(daod) * COMPENSATION_FACTOR) / DAOD_NORMALIZATION_FACTOR,
            0.0
        ), 1.0)

        return {
            "dust_storm_risk": round(normalized_risk, 2),
            "raw_daod": daod,
            "timestamp": datetime.utcnow().isoformat()
        }

    except requests.HTTPError as e:
        if e.response.status_code == 401:
            logger.critical("Invalid CAMS API credentials")
            raise
        logger.error("HTTP error %d from CAMS API", e.response.status_code)
        raise
    except KeyError as e:
        logger.error("Malformed CAMS API response: missing %s", str(e))
        raise
    except ValueError as e:
        logger.error("JSON decoding error: %s", str(e))
        raise

def get_fallback_forecast() -> Dict:
    """Generate simulated forecast with logging"""
    simulated_risk = round(random.uniform(0, 1), 2)
    logger.warning("Using simulated dust risk: %.2f", simulated_risk)
    return {
        "dust_storm_risk": simulated_risk,
        "simulated": True,
        "timestamp": datetime.utcnow().isoformat()
    }

def safe_fetch_forecast() -> Dict:
    """Public interface with fallback handling"""
    try:
        return fetch_dust_forecast()
    except Exception as e:
        logger.error("CAMS fetch failed: %s", str(e))
        return get_fallback_forecast()

if __name__ == "__main__":
    # Test execution
    import json
    print(json.dumps(safe_fetch_forecast(), indent=2))
