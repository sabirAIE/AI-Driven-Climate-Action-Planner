from external.carbon_api import estimate_carbon_emissions


def estimate_carbon_reduction(energy_data, user_goal):
    if energy_data is not None:
        print("Enery data")
        print(energy_data)
        print(user_goal)
        baseline = energy_data['average_monthly_kwh'] if energy_data['average_monthly_kwh'] else 0
        target_reduction_percent = user_goal['target_reduction']
        reduction_kwh = baseline * (target_reduction_percent / 100) if baseline else 0
        print(f"reduction KW {reduction_kwh}")
        emissions = estimate_carbon_emissions(reduction_kwh)
        print(emissions)
        return {
            "baseline_kwh": baseline,
            "target_reduction_percent": target_reduction_percent,
            "expected_reduction_kwh": reduction_kwh,
            "expected_emissions_reduction_kg": emissions,
            "duration": user_goal['duration']
        }
    else:
        return {
            "baseline_kwh": 0,
            "target_reduction_percent": 0,
            "expected_reduction_kwh": 0,
            "expected_emissions_reduction_kg":0,
            "duration": user_goal['duration']
        }
