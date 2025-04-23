# predictive_trigger.py
from copernicus_fetcher import fetch_dust_forecast

DUST_RISK_THRESHOLD = 0.7

def should_trigger_preemptive_cleaning():
    forecast = fetch_dust_forecast()
    risk = forecast['dust_storm_risk']
    print(f"Forecasted dust storm risk: {risk}")
    if risk > DUST_RISK_THRESHOLD:
        print("High risk! Preemptively scheduling cleaning.")
        # TODO: Integrate with NebulOuS orchestration / cleaning trigger
        return True
    else:
        print("Risk level normal. No preemptive action needed.")
        return False

if __name__ == "__main__":
    should_trigger_preemptive_cleaning()
