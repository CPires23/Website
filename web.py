import streamlit as st
import streamlit_lottie as st_lottie
import requests

st.set_page_config(page_title='My Webpage', page_icon=':smile:', layout='wide')
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Load Assets---
lottie_coding = load_lottieurl('https://lottie.host/embed/3a3f20ab-c3fd-49a5-8e59-607ac5759ded/safOeiho6o.json')


#--- HEADER SECTION ---

st.subheader("Hi, I'm Carlos :wave:")
st.title("A Computer Science Student From UAL")
st.write("I am passionate about learning more and more about technologies!")
st.write("[Learn More>](https://www.google.com)")


#--- BODY SECTION ---
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("###")
        st.write("""
        At College I am studying to be the best I can Be
                 I am learning about programming and how to use it to make a difference in the world
                 I am also learning about how to use the coding to automate most tasks for people
        """)
        st.write("[UAL >](https://autonoma.pt)")
    with right_column:
        st_lottie(lottie_coding, height=300, key='coding')