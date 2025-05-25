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

    # Placeholder for actual API call to Climati# Example call
    # Replace with actual API endpoint and parameterif __name__ == "__main__":
    # Q6ND6W18VN5F92G3RWDJN0M2GG    emissions = estimate_carbon_emissions(500)
    # For demonstration, returning mock data    print(f"500 kWh → {emissions} kg CO₂")
    # emission_factor = 0.233  # kg CO2 per kWh
    # emissions = energy_kwh * emission_factor
    # return {
    #     "energy_kwh": energy_kwh,
    #     "emissions_kg": emissions
    # }


estimate_carbon_emissions(97.81532958333334)

# import requests
#
# ENERGY_API_URL = "https://cea.nic.in/api/power_generation.php"  # replace with your real API endpoint
#
#
# def fetch_energy_data(location):
#     try:
#         response = requests.get(ENERGY_API_URL)
#         response.raise_for_status()
#         data = response.json()
#         # print(data)
#
#         # Aggregate total generation per mode
#         mode_totals = {}
#         mode_counts = {}
#
#         for year, records in data.items():
#             for record in records:
#                 if record["Region_State"].lower() == location.lower() or location.lower() == "all india":
#                     mode = record["mode"]
#                     bus_value = float(record["bus"])
#                     mode_totals[mode] = mode_totals.get(mode, 0) + bus_value
#                     mode_counts[mode] = mode_counts.get(mode, 0) + 1
#
#         # Calculate average monthly kWh per mode
#         average_monthly_kwh = {
#             mode: (total / count) if count > 0 else 0
#             for mode, (total, count) in zip(mode_totals.keys(), zip(mode_totals.values(), mode_counts.values()))
#         }
#
#         # Example placeholder for peak usage times (real API probably doesn’t provide this)
#         peak_usage_times = ["6pm-9pm"]
#
#         return {
#             "location": location,
#             "average_monthly_kwh": average_monthly_kwh,
#             "peak_usage_times": peak_usage_times
#         }
#
#     except Exception as e:
#         print(f"Error fetching energy data: {e}")
#         return None
#
#
# # Example call
# if __name__ == "__main__":
#     result = fetch_energy_data("All India")
#     print("\n=== Energy Data Summary ===")
#     print(result)
