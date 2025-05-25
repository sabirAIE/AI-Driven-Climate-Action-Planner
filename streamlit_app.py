import streamlit as st
from agents.climate_planner_agent import ClimatePlannerAgent

st.title("🌍 AI-Driven Climate Action Planner")

st.write("Provide your details to generate a personalized carbon reduction plan.")

location = st.text_input("Location", value="all india")
target_reduction = st.text_input("Target Carbon Reduction (%)", value="20%")
duration = st.text_input("Duration in Month(s)", value="12")
target_reduction = float(target_reduction.strip().rstrip('%'))
duration = float(duration)
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
        st.error("Plan generation failed!")
