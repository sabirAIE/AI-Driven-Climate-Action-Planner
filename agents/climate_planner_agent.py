from tools.energy_data_tool import get_local_energy_data
from tools.carbon_estimator_tool import estimate_carbon_reduction
from agents.incentive_finder_agent import find_government_incentives
from agents.report_generator_agent import generate_action_plan_report


class ClimatePlannerAgent:
    def handle_goal(self, user_goal):
        location = user_goal['location']
        energy_data = get_local_energy_data(location)
        incentives = find_government_incentives(location)

        carbon_estimate = estimate_carbon_reduction(energy_data, user_goal)
        print(f"carbon estimate {carbon_estimate}")
        if carbon_estimate['baseline_kwh'] and carbon_estimate['expected_reduction_kwh'] and carbon_estimate['expected_emissions_reduction_kg']:
            report = generate_action_plan_report(energy_data, incentives, carbon_estimate, user_goal)
            return report
        else:
            return None

