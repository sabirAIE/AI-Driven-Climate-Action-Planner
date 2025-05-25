def generate_action_plan_report(energy_data, incentives, carbon_estimate, user_goal):
    summary = (
        f"To achieve a {carbon_estimate['target_reduction_percent']}% reduction in carbon footprint "
        f"over {int(carbon_estimate['duration'])} month(s), focus on reducing approximately "
        f"{carbon_estimate['expected_reduction_kwh']:.2f} kWh per month, "
        f"which equates to an estimated reduction of "
        f"{carbon_estimate['expected_emissions_reduction_kg']:.2f} kg CO₂."
        f" Total CO₂ reduction {user_goal['duration']*carbon_estimate['expected_emissions_reduction_kg']:.2f} Kg CO₂"
    )
    return {
        "summary": summary,
        "energy_data": energy_data,
        "incentives": incentives,
        "carbon_estimate": carbon_estimate
    }
