import streamlit as st

def main():
    st.title("Microsoft Teams Test App")
    
    st.write("This is a dummy app for testing Teams integration.")
    
    name = st.text_input("Enter your name:")
    if st.button("Submit"):
        st.success(f"Hello, {name}! This app is running inside Teams.")
    
    st.write("### Features:")
    st.write("- Simple input field")
    st.write("- Dynamic response")
    st.write("- Basic UI")
    
if __name__ == "__main__":
    main()
