import streamlit as st

# Set Streamlit page config
st.set_page_config(page_title="Teams App", page_icon=":zap:", layout="wide")

# Function to display Privacy Policy
def show_privacy_policy():
    st.title("Privacy Policy")
    st.write("### **Privacy Policy for Teams Integrate App**")
    st.write("**Effective Date:** [Insert Date]  \n**Last Updated:** [Insert Date]")
    
    st.write("Welcome to **Teams Integrate App**. This privacy policy describes how we handle your data.")
    
    st.subheader("1. Scope")
    st.write("This policy applies to **Teams Integrate App** and any related services we provide.")

    st.subheader("2. Data Collection & Usage")
    st.write("- **User Input Data:** We collect only the data you voluntarily provide (e.g., name).")
    st.write("- **Usage Data:** We track basic interactions to improve the app experience.")
    st.write("- **Microsoft Teams Data:** No Teams messages, contacts, or files are accessed.")

    st.subheader("3. Data Storage, Retention & Deletion")
    st.write("- **Storage:** We do not store personal data on our servers.")
    st.write("- **Retention:** Anonymous usage statistics may be retained.")
    st.write("- **Deletion:** No data storage means no deletion is required.")

    st.subheader("4. Security & Data Protection")
    st.write("- **Secure Communication:** Data is transmitted over HTTPS.")
    st.write("- **No Third-Party Sharing:** We do not share your data with third parties.")

    st.subheader("5. Contact Information")
    st.write("For any concerns, contact us at: **[Your Email]**")

    st.subheader("6. Updates to This Policy")
    st.write("The latest version of this policy is available at:")
    st.write("[Insert Your Privacy Policy URL]")

# Function to display Terms of Use
def show_terms_of_use():
    st.title("Terms of Use")
    st.write("### **Terms of Use for Teams Integrate App**")
    
    st.write("By using this application, you agree to the following terms:")
    
    st.subheader("1. Acceptance of Terms")
    st.write("By accessing the app, you agree to comply with these terms.")

    st.subheader("2. Use of the Application")
    st.write("- The app is for testing Teams integration only.")
    st.write("- You must not misuse or exploit the app's features.")

    st.subheader("3. Limitation of Liability")
    st.write("We are not responsible for any loss arising from the use of this application.")

    st.subheader("4. Changes to Terms")
    st.write("We reserve the right to update these terms at any time.")

    st.subheader("5. Contact Information")
    st.write("For questions, contact us at: **[Your Email]**")

# Function to display Main App
def show_main_app():
    st.title("Microsoft Teams Test App")
    
    st.write("This is a dummy app for testing Teams integration.")
    
    name = st.text_input("Enter your name as:")
    if st.button("Submit"):
        st.success(f"Hello, {name}! This app is running inside Teams.")
    
    st.write("### Features:")
    st.write("- Simple input field")
    st.write("- Dynamic response")
    st.write("- Basic UI")

# Get query parameters
query_params = st.query_params  # Updated to the new recommended method

# Route based on query parameters
if "view" in query_params:
    if query_params["view"] == "privacy":
        show_privacy_policy()
    elif query_params["view"] == "terms":
        show_terms_of_use()
    else:
        show_main_app()
else:
    show_main_app()
