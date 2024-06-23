# Import libraries
import streamlit as st
import requests
import json
#from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title='Home Page',
    page_icon='🏠',
    layout='wide',
    initial_sidebar_state='expanded'
)

# # Define function to get animation
# def lottie_url(url: str):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

#lottie_img = lottie_url("https://lottie.host/80d6a368-c787-af59-Beca-9t64cf41btb/VdfzfJexsp.jscn")

selected = option_menu(None, options=["Home", "About Us", "Upload"], 
    icons=['house','gear' 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected

# Intro on title
if selected == "Home":
    st.title("Customer Churn Predictor")
    st.write("""Revealing the Factors Behind Customer Churn !!""")
    st.write("##")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## We're happy to have you here!")
        st.write("---")
        st.markdown("""Every business aims to boost its earnings and revenue, and a significant strategy to achieve this is by focusing on customer retention.""")
        st.write("""Our Customer Churn Predictor is designed to address this critical area for industry leaders""")          
        st.write("""
                 **With us, you can:**
                - Identify the factors contributing to customer churn.
                - Take proactive measures to retain their valuable customers.
                - Better calculate the lifetime value of your customers.
        """)

    # with col2:
    #     st_lottie(
    #         lottie_img,
    #         speed=1,
    #         reverse=False,
    #         loop=True,
    #         quality="high",
    #         key="coding",
    #         height=500,
    #         width=600
    #     )

         
if selected == "About Us":
    col3, col4 = st.columns(2)
    with col3:
        st.title("About us")
        st.write("##")
        st.write("""
                 Our team of experts operates with the following objectives:

                 - Thoroughly explore our clients' data to determine the most efficient classification models.
                 - Calculate the lifetime value of each customer and identify the factors influencing customer churn rates.
                 - Predict whether a customer will churn or not.""")
#     with col4
#         st_lottie(
#     lottie_home,
#     speed=1,
#     reverse= False,
#     loop=True,
#     quality="high",
#     key="coding",
#     height=500,
#     width=600

# )

if selected == "Upload":
        st.title("Explore")
        st.write("##")
        st.markdown("""
                    ### Our robust machine learning algorithms enable you to forecast customer churn with your dataset""")
        st.write("##")
        uploaded_file = st.file_uploader("Upload your file here")
        st.markdown("*Kindly rename your columns to align with our naming conventions: Cheers 🥂*")

# with st.container():
#     st.write(" ... ")
#     st.header("Explore")
#     st.write("##")
#     st.write("You can explore the predictive capabilities of our robust machine learning algorithms to forecast whether a customer is likely to churn..")
#     st.write("##")
#     uploaded_file = st.file_uploader("Upload your file here")
