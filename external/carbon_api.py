import requests

CLIMATIQ_API_KEY = "Q6ND6W18VN5F92G3RWDJN0M2GG"  # replace with your real API key


def estimate_carbon_emissions(kwh):
    url = "https://api.climatiq.io/estimate"
    headers = {
        "Authorization": f"Bearer {CLIMATIQ_API_KEY}",
        "Content-Type": "application/json",
        "Accept - Encoding": "gzip"
    }
    payload = {
        "emission_factor": {
            "activity_id": "electricity-supply_grid-source_total_supplier_mix",
            "region": "GB",
            "year": 2020,
            "data_version": "^21"
        },
        "parameters": {
            "energy": 800,
            "energy_unit": "kWh"
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        emissions = data.get("co2e", 0)
        print(f"Estimated CO₂ emissions: {emissions} kg")
        return emissions
    except Exception as e:
        print(f"Error estimating emissions: {e}")
        return None


def estimate_carbon_emissions_dep(energy_kwh):
    pass
    # Placeholder for actual API call to Climati Example call
    # Replace with actual API endpoint and parameterif __name__ == "__main__":
    # Q6ND6W18VN5F92G3RWDJN0M2GG    emissions = estimate_carbon_emissions(500)
    # For demonstration, returning mock data    print(f"500 kWh → {emissions} kg CO₂")
    # emission_factor = 0.233  # kg CO2 per kWh
    # emissions = energy_kwh * emission_factor
    # return {
    #     "energy_kwh": energy_kwh,
    #     "emissions_kg": emissions
    # }