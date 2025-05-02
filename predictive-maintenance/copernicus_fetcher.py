"""
copernicus_fetcher.py

This module attempts to fetch dust storm (or similar) forecast data from a Copernicus API.
In a production environment, replace the placeholder URL, parameters, and API key with actual values.
For now, if the request fails or the data is missing, the module falls back to generating a simulated risk.
"""

import requests
import random

# Placeholder API endpoint; update with the actual Copernicus API endpoint.
API_URL = "https://api.example.com/copernicus/forecast"
# In a production setting, do not hardcode your API key; load it securely instead.
API_KEY = "YOUR_API_KEY_HERE"
DEFAULT_TIMEOUT = 10  # seconds

def fetch_dust_forecast():
    """
    Fetches the dust storm risk from the Copernicus API.
    
    Returns:
        dict: A dictionary with 'dust_storm_risk' as a float (0 to 1 scale).
    
    In the event of an error (HTTP or parsing), a simulated risk value is returned.
    """
    params = {
        "apikey": API_KEY,
        "parameter": "dust_storm_risk",
        "lat": 37.0,    # Example latitude (e.g., Almería)
        "lon": -2.5,    # Example longitude (e.g., Almería)
        # Add any additional parameters required by the API here.
    }
    
    try:
        response = requests.get(API_URL, params=params, timeout=DEFAULT_TIMEOUT)
        response.raise_for_status()  # Raises HTTPError for bad responses.
        data = response.json()  # Parse the JSON response.
        
        # Assume the API returns a JSON with a key "risk" holding the dust storm risk value.
        risk_value = float(data.get("risk", 0))
        return {"dust_storm_risk": risk_value}
    except (requests.RequestException, ValueError) as exc:
        print(f"Error fetching Copernicus forecast: {exc}")
        # Fallback: simulate a dust storm risk value.
        simulated_risk = round(random.uniform(0, 1), 2)
        print(f"Returning simulated dust storm risk: {simulated_risk}")
        return {"dust_storm_risk": simulated_risk}

if __name__ == "__main__":
    forecast = fetch_dust_forecast()
    print("Copernicus forecast:", forecast)
