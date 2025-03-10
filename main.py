import streamlit as st
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Teams App", page_icon=":zap:", layout="wide")

st.title("Microsoft Teams Test App")
st.write("This is a dummy app for testing Teams integration.")

# Inject JavaScript for Teams SDK initialization
teams_script = """
<script>
  if (typeof microsoftTeams !== "undefined") {
    microsoftTeams.app.initialize()
      .then(() => {
        console.log("✅ Teams SDK initialized successfully!");
        document.getElementById("teams-status").innerText = "✅ Teams SDK Loaded";
      })
      .catch(err => {
        console.error("❌ Teams SDK initialization failed:", err);
        document.getElementById("teams-status").innerText = "⚠️ SDK Init Failed";
      });
  } else {
    console.warn("⚠️ Microsoft Teams SDK not available.");
    document.getElementById("teams-status").innerText = "⚠️ Teams SDK Not Found";
  }
</script>

<div id="teams-status" style="margin-top: 10px; font-weight: bold;">Loading Teams SDK...</div>
"""

components.html(teams_script, height=50)  # Inject the JavaScript into Streamlit

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
