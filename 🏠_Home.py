# Import necessary libraries
import streamlit as st
import pandas as pd
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import requests
import json
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title="Home", page_icon="🏠",  layout="wide")

with open('./Utils/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status,username = authenticator.login(location='sidebar')


if st.session_state['authentication_status']:
    authenticator.logout(location='sidebar')


    # Add CSS for animations
    st.write("""
        <style>
            @keyframes zoom-in {
                0% {
                    transform: scale(0);
                }
                100% {
                    transform: scale(1);
                }
            }
            @keyframes slide-in-right {
                0% {
                    transform: translateX(100%);
                }
                100% {
                    transform: translateX(0);
                }
            }
            @keyframes slide-in-left {
                0% {
                    transform: translateX(-100%);
                }
                100% {
                    transform: translateX(0);
                }
            }
            @keyframes slide-in-bottom {
                0% {
                    transform: translateY(100%);
                }
                100% {
                    transform: translateY(0);
                }
            }
            @keyframes slide-in-top {
                0% {
                    transform: translateY(-100%);
                }
                100% {
                    transform: translateY(0);
                }
            }
            .zoom-in-animation {
                animation: zoom-in 1.5s ease-in-out;
            }
            .slide-in-right-animation {
                animation: slide-in-right 1.5s ease-in-out;
            }
            .slide-in-left-animation {
                animation: slide-in-left 1.5s ease-in-out;
            }
            .slide-in-bottom-animation {
                animation: slide-in-bottom 1.5s ease-in-out;
            }
            .slide-in-top-animation {
                animation: slide-in-top 1.5s ease-in-out;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header with zoom-in animation
    st.markdown('<div class="slide-in-top-animation"><h1>Welcome to Customer Churn Predictor App!</h1></div>', unsafe_allow_html=True)

    # Content with different slide-in animations
    st.write('<div class="slide-in-bottom-animation"><h3>Harnessing the capabilities of machine learning to forecast customer churn</h3></div>', unsafe_allow_html=True)

    # Home Page Content
    st.markdown('<div class="slide-in-right-animation"><h2>About This App</h2></div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="slide-in-left-animation">
            <p>The <span class="slide-in-bottom-animation">Customer Churn Prediction App</span> serves as a powerful tool for businesses operating in the telecommunications industry. Its primary purpose is to predict whether a customer is likely to churn, which means leaving the service. By harnessing advanced machine learning techniques, this app offers valuable insights into customer behavior patterns. Armed with this information, companies can take proactive measures to enhance customer retention. In essence, it empowers businesses to make informed decisions and foster stronger relationships with their clientele.</p>
        </div>
    """, unsafe_allow_html=True)

   
    selected = option_menu(None, options=["Home", "About Us", "Upload"], 
        icons=['house','gear' 'cloud-upload'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    selected
  
                
    # Intro on title
    if selected == "Home":
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

       # Create columns for Key Features, How It Works, and Benefits
        col1, col2, col3 = st.columns(3)

        # Key Features with slide-in-right animation
        with col1:
            st.markdown('<div class="zoom-in-animation">', unsafe_allow_html=True)
            st.markdown("## Key Features")
            st.markdown("""
            - **Model Training:** Train various machine learning models, such as Logistic Regression, Random Forest, and XGBoost, to predict customer churn.
            - **Feature Importance:** Analyze feature importances to understand the drivers of customer churn.
            - **User-Friendly Interface:** Interact with the app through an intuitive and engaging user interface.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # How It Works with slide-in-bottom animation
        with col2:
            st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
            st.markdown("## How It Works")
            st.markdown("""
            - **Data Collection:** Gather customer data from various sources.
            - **Data Preprocessing:** Clean and preprocess the data for model training.
            - **Model Training:** Train multiple machine learning models to predict churn.
            - **Model Evaluation:** Evaluate model performance using various metrics.
            - **Deployment:** Deploy the best-performing model to make real-time predictions.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # Benefits with slide-in-top animation
        with col3:
            st.markdown('<div class="slide-in-top-animation">', unsafe_allow_html=True)
            st.markdown("## Benefits")
            st.markdown("""
            - **Improve Customer Retention:** Identify at-risk customers and take proactive measures to retain them.
            - **Optimize Marketing Strategies:** Tailor marketing efforts to target customers who are likely to churn.
            - **Enhance Business Performance:** Reduce churn rates and increase customer lifetime value.
            """)
            st.markdown('</div>', unsafe_allow_html=True)    
 
            
    if selected == "About Us":
        col3, col4 = st.columns(2)
        with col3:
            st.write("""
                    Our team of experts operates with the following objectives:

                    - Thoroughly explore our clients' data to determine the most efficient classification models.
                    - Calculate the lifetime value of each customer and identify the factors influencing customer churn rates.
                    - Predict whether a customer will churn or not.""")
    

    if selected == "Upload":
            st.markdown("""
                        ### Our robust machine learning algorithms enable you to forecast customer churn with your dataset""")
            #st.write("##")
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
            uploaded_file = st.file_uploader("Upload your file here")
            st.markdown("*Kindly rename your columns to align with our naming conventions: Cheers 🥂*")
            

    
    # Footer
    st.markdown("""
        ---
        ©2024 CustomerChurnPredictor. All rights reserved.
    """)        


elif st.session_state['authentication_status'] is False:
    st.error('Wrong username/password')
elif st.session_state['authentication_status'] is None:
    st.info('Login to get access to the app')
    st.code("""
    Test Account
    Username: analystidris
    Password: 456123
    """)

# st.write(st.session_state)