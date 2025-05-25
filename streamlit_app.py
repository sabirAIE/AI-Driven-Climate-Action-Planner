import streamlit as st
from agents.climate_planner_agent import ClimatePlannerAgent

st.set_page_config(page_title="Climate Action Planner", page_icon="🌍", )

# Sidebar
st.sidebar.title("About")
st.sidebar.info(
    """
    🌱 **Climate Action Planner**  
    Generate a personalized carbon reduction plan.

    👉 [View source code on GitHub](https://github.com/sabirAIE/AI-Driven-Climate-Action-Planner)

    📊 [View Architecture Diagram]
        please check in navigation bar
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
        st.success("Plan generated!")
        st.subheader("Summary")
        st.write(action_plan['summary'])
        st.subheader("Energy Data")
        st.json(action_plan['energy_data'])
        st.subheader("Incentives")
        st.json(action_plan['incentives'])
        st.subheader("Carbon Estimate")
        st.json(action_plan['carbon_estimate'])
    else:
        st.error("Plan generation failed! Please try again")
