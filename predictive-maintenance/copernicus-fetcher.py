# copernicus_fetcher.py
"""
Simulates fetching dust storm/forecast data from Copernicus API.
Replace dummy data with real API calls after integration.
"""

import random

def fetch_dust_forecast():
    """Simulate a forecast with dust risk on a 0-1 scale."""
    # TODO: Integrate real Copernicus API call here
    return {"dust_storm_risk": round(random.uniform(0, 1), 2)}

if __name__ == "__main__":
    forecast = fetch_dust_forecast()
    print("Copernicus forecast:", forecast)
