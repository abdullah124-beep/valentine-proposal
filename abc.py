import streamlit as st

st.title("❤️ Will You Be My Valentine? ❤️")

answer = st.radio("Choose your answer:", ["Yes", "No"])

if answer == "Yes":
    st.balloons()
    st.success("Yay! I love you, Areesha! ❤️🥰")
else:
    st.error("Sorry, wrong answer ma’am! Say yes, nahi to maru ga! 😂")


# HTML files to create:
# templates/index.html
# templates/no.html
