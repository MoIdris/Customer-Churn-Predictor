# Import libraries
import streamlit as st
import requests
import json
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


# Set page configuration
st.set_page_config(
    page_title='Home Page',
    page_icon='🏠',
    layout='wide',
    initial_sidebar_state='expanded'
)


with open('./Utils/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create an authentication object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# invoke the login authentication
name, authentication_status, username = authenticator.login(location="sidebar")

if st.session_state["authentication_status"] is None:
    st.warning("Please Log in to get access to the application")
    test_code = '''
    Test Account
    username: analystidris
    password: 456123
    '''
    st.code(test_code)
        
elif st.session_state["authentication_status"] == False:
    st.error("Wrong username or password")
    st.info("Please Try Again")
    test_code = '''
    Test Account
    username: analystidris
    password: 456123
    '''
    st.code(test_code)
else:
    st.info("Login Successful")
    st.write(f'Welcome *{username}*')
    #logout user using streamlit authentication logout
    authenticator.logout('Logout', 'sidebar')


# with open('./Utils/config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status, username = authenticator.login(location='sidebar')



# if st.session_state['authentication_status']:
#     authenticator.logout(location='sidebar')
#     st.title('Customer Churn Predictor')

# if st.session_state['authentication_status']:
#     st.title('Customer Churn Predictor')
# elif st.session_state['authentication_status'] is False:
#     st.error('Wrong username/password')
# elif st.session_state['authentication_status'] is None:
#     st.info("Login to get access to the app")
#     st.code("""
#     Test Account
#     Username: analystidris
#     Password: 456123
#     """)

# if st.session_state['authentication_status']:
#     st.title = "Customer Churn Predictor"
#     authenticator.logout(location='sidebar')

selected = option_menu(None, options=["Home", "About Us", "Upload"], 
    icons=['house','gear' 'cloud-upload'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected



# Intro on title
if selected == "Home":
    #st.title('Customer Churn Predictor')
    st.write("""Revealing the Factors Behind Customer Churn """)
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

        col1,col2 = st.columns(2)
        with col1:
            st.header("Key Features")
            st.write("""
                        - View Data - Allows you to view data 
                        - Predict - Feature that allows to make single prediction or predict your csv data in bulk
                        - View History - Allows you to view the history of your predictions
                        - Dashboard - View data visualizations
                        """)
            
        with col2:
            st.header("User Benefits")
            st.write("""
                        - Make data driven decisions effortlessly
                        - User-Friendly Interface
                        - Real-Time predictions
                        - Insightful dashboards
                        - Ease to use
                        """)
            
        col1,col2 = st.columns(2)
        with col1:
            st.header("Machine Learning Integration")
            st.write("""
                    - You have access three trained machine learning models
                    - Simple integration and user-friendly access
                    - Save data to local database or locally for future use
                    - Get probability of predictions
                    """)
        with col2:
            st.header("How To Run Applicattion")
            code = '''
            #Activate Virtual Environment
            source venv/bin/activate

            #Install dependencies
            pip install -r requirements.txt

            #Run the application
            streamlit run app.py
            '''
            st.code(code,language="python")
            

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
        #st.title("About us")
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
        #st.title("Explore")
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
