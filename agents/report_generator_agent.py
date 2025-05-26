import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_action_plan_report(energy_data, incentives, carbon_estimate, user_goal):
    baseline = carbon_estimate['baseline_kwh']
    target_reduction_percent = carbon_estimate['target_reduction_percent']
    expected_reduction_kwh = carbon_estimate['expected_reduction_kwh']
    expected_emissions_reduction_kg = carbon_estimate['expected_emissions_reduction_kg']
    duration = int(carbon_estimate['duration'])

    total_co2_reduction = user_goal['duration'] * expected_emissions_reduction_kg

    summary = (
        f"To achieve a {target_reduction_percent}% reduction in carbon footprint "
        f"over {duration} month(s), focus on reducing approximately "
        f"{expected_reduction_kwh:.2f} kWh per month, "
        f"which equates to an estimated reduction of "
        f"{expected_emissions_reduction_kg:.2f} kg CO₂ per month. "
        f"Total CO₂ reduction over {duration} months: {total_co2_reduction:.2f} kg CO₂."
    )

    # Graph 1: Baseline vs Target kWh
    target_kwh = baseline - expected_reduction_kwh
    bar_df = pd.DataFrame({
        'Scenario': ['Baseline', 'After Reduction'],
        'kWh per Month': [baseline, target_kwh]
    })

    # Graph 2: Cumulative CO₂ Saved Over Months
    months = np.arange(1, duration + 1)
    # Generate months array
    months = np.arange(1, duration + 1)

    # Base cumulative CO₂ saved
    base_cumulative = months * expected_emissions_reduction_kg

    # Add random noise (±5%)
    noise_factor = np.random.normal(1.0, 0.05, size=months.shape)
    cumulative_co2 = base_cumulative * noise_factor

    # Ensure no negative values (just in case)
    cumulative_co2 = np.maximum(cumulative_co2, 0)

    # Create DataFrame
    line_df = pd.DataFrame({
        'Month': months,
        'Cumulative CO₂ Saved (kg)': cumulative_co2
    })

    # Graph 3: Pie Chart for Reduction %
    pie_sizes = [target_reduction_percent, 100 - target_reduction_percent]
    pie_labels = ['Reduction', 'Remaining']
    pie_colors = ['green', 'lightgrey']

    return {
        "summary": summary,
        "energy_data": energy_data,
        "incentives": incentives,
        "carbon_estimate": carbon_estimate,
        "charts": {
            "bar_df": bar_df,
            "line_df": line_df,
            "pie_sizes": pie_sizes,
            "pie_labels": pie_labels,
            "pie_colors": pie_colors
        }
    }
