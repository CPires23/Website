import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title='My Webpage', page_icon=':smile:', layout='wide')
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load Assets---
lottie_coding = load_lottieurl('https://lottie.host/3a3f20ab-c3fd-49a5-8e59-607ac5759ded/safOeiho6o.json')


#--- HEADER SECTION ---

st.subheader("Hi, I'm Carlos :wave:")
st.title("A Computer Science Student From [UAL](https://autonoma.pt)")
st.write("I am passionate about learning more and more about technologies!")


#--- BODY SECTION ---
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("###")
        st.write("At College I am studying to be the best I can Be I am learning about programming and how to use it to make a difference in the world")
        st.write("I am also learning about how to use the coding to automate most tasks for people!")
        st.write("I am now starting my master's degree in Computer Engineering and Telecommunications.")
        
    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')
        
        
with st.container():
    st.write('---')
    st.header("My Projects")
    st.write("###")

    # Cria três colunas para os projetos
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://images.unsplash.com/photo-1551033406-611cf9a28f22?auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.write("Still working on this project, but I will update it soon!")
        st.subheader("To‑Do App")
        st.write("A Flutter app to manage tasks locally with Hive storage.")
        st.markdown("[View on GitHub](https://github.com/CPires23)")

    with col2:
        st.image("https://images.unsplash.com/photo-1605902711622-cfb43c4437b5?auto=format&fit=crop&w=800&q=80", use_container_width=True)
        st.subheader("Password Generator")
        st.write("A Python tool that creates secure passwords with some complexity.")
        st.markdown("[Try it Online](https://seusite.com/password-generator)")

    with col3:
        st.image("https://images.unsplash.com/photo-1556761175-5973dc0f32e7", use_container_width=True)
        st.subheader("Workout Dashboard")
        st.write("A Streamlit dashboard tracking gym progress and tennis sessions.")
        st.markdown("[See Demo](https://seusite.com/workout-dashboard)")