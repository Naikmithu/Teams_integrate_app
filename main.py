import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Teams App", page_icon=":zap:", layout="wide")

st.title("Microsoft Teams Test App")
st.write("This is a dummy app for testing Teams integration.")

# Inject JavaScript to initialize Microsoft Teams SDK
teams_script = """
<script src="https://res.cdn.office.net/teams-js/2.15.0/js/MicrosoftTeams.min.js"></script>
<script>
  document.addEventListener("DOMContentLoaded", function () {
    microsoftTeams.app.initialize().then(() => {
      console.log("Teams SDK initialized successfully!");
    }).catch(err => {
      console.error("Teams SDK initialization failed:", err);
    });
  });
</script>
"""

components.html(teams_script, height=0)  # Inject JS into Streamlit

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
