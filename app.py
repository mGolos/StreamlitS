import streamlit as st

st.title('Requirements test')
with open('requirements.txt') as file:
    for line in file:
        st.write(line)