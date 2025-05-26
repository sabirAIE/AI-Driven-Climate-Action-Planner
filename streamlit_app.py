import streamlit as st
from agents.climate_planner_agent import ClimatePlannerAgent
import matplotlib.pyplot as plt

st.set_page_config(page_title="Climate Action Planner", page_icon="🌍", )

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    """
    🌱 **Climate Action Planner**  
    Generate a personalized carbon reduction plan.Generate a personalized carbon reduction plan.

    👉 [View source code on GitHub](https://github.com/sabirAIE/AI-Driven-Climate-Action-Planner)
    """
)

# Main Page
st.title("🌍 Climate Action Planner")
st.write("Provide your details to generate a personalized carbon reduction plan.")
# Input Fields
location = st.text_input("Location", value="all india", disabled=True)
target_reduction = st.text_input("Target Carbon Reduction (%)", value="20%")
duration = st.text_input("Duration in Month(s)", value="12")

# Convert input strings to floats
target_reduction = float(target_reduction.strip().rstrip('%'))
duration = float(duration)

# Generate Action Plan
if st.button("Generate Action Plan"):
    user_goal = {
        "location": location,
        "target_reduction": target_reduction,
        "duration": duration
    }
    with st.spinner("Generating your action plan..."):
        agent = ClimatePlannerAgent()
        action_plan = agent.handle_goal(user_goal)

    if action_plan:
        # Show summary
        st.success(action_plan['summary'])

        # Bar Chart
        st.subheader("Baseline vs After Reduction (kWh/month)")
        st.bar_chart(action_plan['charts']['bar_df'].set_index('Scenario'))

        # Line Chart
        st.subheader("Cumulative CO₂ Saved Over Time")
        st.line_chart(action_plan['charts']['line_df'].set_index('Month'))

        # Pie Chart
        st.subheader("Reduction Percentage")
        fig, ax = plt.subplots()
        ax.pie(
            action_plan['charts']['pie_sizes'],
            labels=action_plan['charts']['pie_labels'],
            colors=action_plan['charts']['pie_colors'],
            autopct='%1.1f%%',
            startangle=90
        )
        ax.axis('equal')
        st.pyplot(fig)
        st.subheader("Energy Data")
        st.json(action_plan['energy_data'])
        st.subheader("Incentives")
        st.json(action_plan['incentives'])
        st.subheader("Carbon Estimate")
        st.json(action_plan['carbon_estimate'])
    else:
        st.error("Plan generation failed! Please try again")
