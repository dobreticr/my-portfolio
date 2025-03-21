import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.png") #Change image size with width=600

with (col2):
    st.title("Ronaldo Dobretic")
    content  = """
    I’m a programmer with a solid foundation in Python, having completed the Complete Python Bootcamp by Ardit Sulce. Skilled in data structures, OOP, APIs, and building real-world applications, I enjoy solving problems and continuously learning. Ready to apply my skills to create innovative solutions and contribute to meaningful projects. Let’s connect and build something great!
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have build in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index,row in df[:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index,row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
