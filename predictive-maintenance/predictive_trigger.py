# predictive_trigger.py
from copernicus_fetcher import fetch_dust_forecast

DUST_RISK_THRESHOLD = 0.7

def get_forecast_data():
    """
    Fetch the dust forecast and extract the risk level.
    Returns:
        float: The forecasted dust storm risk.
    """
    forecast = fetch_dust_forecast()
    risk = forecast['dust_storm_risk']
    print(f"Forecasted dust storm risk: {risk}")
    return risk

def should_trigger_preemptive_cleaning():
    """
    Determines whether preemptive cleaning should be triggered.
    Returns:
        bool: True if the forecasted risk exceeds the threshold, False otherwise.
    """
    risk = get_forecast_data()
    if risk > DUST_RISK_THRESHOLD:
        print("High risk! Preemptively scheduling cleaning.")
        # TODO: Integrate with NebulOuS orchestration / cleaning trigger
        return True
    else:
        print("Risk level normal. No preemptive action needed.")
        return False

if __name__ == "__main__":
    # For testing purposes:
    risk = get_forecast_data()
    print("Fetched forecast risk:", risk)
    decision = should_trigger_preemptive_cleaning()
    print("Should trigger preemptive cleaning:", decision)
