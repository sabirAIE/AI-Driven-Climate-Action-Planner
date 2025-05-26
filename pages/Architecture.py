import streamlit as st

st.set_page_config(page_title="Architecture Diagram", page_icon="🛠")
st.title("🌱 Climate Action Planner")
st.markdown("""
      This is a Streamlit app designed to help users create a **personalized carbon reduction plan** based on their
      location, energy usage, and carbon reduction goals.

    ## 🚀 Features
    ✅ Generate a carbon reduction action plan  
    ✅ Estimate monthly energy (kWh) reduction targets  
    ✅ Calculate expected CO₂ emissions savings  
    ✅ Provide local incentives and recommendations  
    ✅ Easy-to-use Streamlit interface  
    ✅ **Sidebar About page** with project info and links
""")

st.title("🛠 Application Architecture")
st.image("assets/img.png", caption="System Architecture Diagram", use_column_width=True)

st.markdown("""
### How It Works

- **User Input** → Users provide location, target reduction, and duration.
- **Planner Agent** → The ClimatePlannerAgent processes the goal.
- **Data Sources** → The system fetches energy, incentive, and carbon data.
- **Output** → A customized action plan is shown in the app.

For more technical details, visit the [GitHub repository](https://github.com/sabirAIE/AI-Driven-Climate-Action-Planner).
""")
