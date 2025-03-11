import streamlit as st
import streamlit.components.v1 as components

# Microsoft Teams SDK for authentication and integration
teams_sdk = """
<script src="https://res.cdn.office.net/teams-js/2.10.0/js/MicrosoftTeams.min.js"></script>
<script>
    microsoftTeams.app.initialize().then(() => {
        console.log("Teams app initialized");
    }).catch(err => {
        console.error("Teams initialization error", err);
    });
</script>
"""

# Inject the Teams SDK script
components.html(teams_sdk, height=0)

# Set page configuration
st.set_page_config(page_title="Teams App", page_icon=":zap:", layout="wide")

st.title("Microsoft Teams Test App")
st.write("This is a dummy app for testing Teams integration.")

# Input Field
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.success(f"Hello, {name}! This app is running inside Teams.")

# Features
st.write("### Features:")
st.write("- Simple input field")
st.write("- Dynamic response")
st.write("- Basic UI")

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.page_link("pages/privacy.py", label="Privacy Policy")
st.sidebar.page_link("pages/terms.py", label="Terms of Use")
