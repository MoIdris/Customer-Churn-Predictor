# # import os
# # import streamlit as st
# # import pandas as pd

# # st.set_page_config(
# #     page_title ='History Page',
# #     page_icon ='📜',
# #     layout="wide"
# # )


# # def display_history_page():
# #     # get the path of the history data
# #     csv_path = "./data/prediction_history.csv"
# #     csv_exists = os.path.exists(csv_path)

# #     if csv_exists:
# #         history_data= pd.read_csv(csv_path)
# #         st.dataframe(history_data)
# #     else:
# #         st.write("No history data found")
# #         st.write("Please run the app and make a prediction to view the history page")
# #         st.stop()





# #         #st.dataframe(history_df)

# # if __name__ == "__main__":
# #     st.title("History Page 📜")
# #     display_history_page()



# # import os
# # import streamlit as st
# # import pandas as pd

# # st.set_page_config(
# #     page_title ='History Page',
# #     layout="wide"
# # )

# # # Display the app content based on authentication status
# # if "authentication_status" not in st.session_state:
# #     st.session_state['authentication_status']== None
# #     st.warning('Please login from the home page')
# # elif st.session_state['authentication_status'] == False:
# #     st.error('Username/password is incorrect')
# # elif st.session_state['authentication_status']:

# #     def display_history_page():
# #         # get the path of the history data
# #         csv_path = "./Data/prediction_history.csv"
# #         csv_exists = os.path.exists(csv_path)

# #         if csv_exists:
# #             history_data= pd.read_csv(csv_path)
# #             st.dataframe(history_data)
# #         else:
# #             st.write("No history data found")
# #             st.write("Please run the app and make a prediction to view the history page")
# #             st.stop()






# #     # st.dataframe(history_df)

# #     if __name__ == "__main__":
# #         st.title("History Page")
# #         display_history_page()


# import os
# import streamlit as st
# import pandas as pd

# st.set_page_config(
#     page_title ='History Page',
#     layout="wide"
# )

# # Display the app content based on authentication status
# if st.session_state['authentication_status']== None:
#     st.warning('Please login from the home page')
# elif st.session_state['authentication_status'] == False:
#     st.error('Username/password is incorrect')
# elif st.session_state['authentication_status']:

#     def display_history_page():
#         # get the path of the history data
#         csv_path = "./Datasets/prediction_history.csv"
#         csv_exists = os.path.exists(csv_path)

#         if csv_exists:
#             history_data= pd.read_csv(csv_path)
#             st.dataframe(history_data)
#         else:
#             st.write("No history data found")
#             st.write("Please run the app and make a prediction to view the history page")
#             st.stop()






#     # st.dataframe(history_df)

#     if __name__ == "__main__":
#         st.title("History Page")
#         display_history_page()


# import streamlit as st
# import pandas as pd
# import os
# import yaml
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth


# # Set page configuration
# st.set_page_config(page_title="History", page_icon="📜",  layout="wide")

# with open('./Utils/config.yaml') as file:
#     config = yaml.load(file, Loader=SafeLoader)

# authenticator = stauth.Authenticate(
#     config['credentials'],
#     config['cookie']['name'],
#     config['cookie']['key'],
#     config['cookie']['expiry_days'],
#     config['preauthorized']
# )

# name, authentication_status,username = authenticator.login(location='sidebar')


# if st.session_state['authentication_status']:
#     authenticator.logout(location='sidebar')


#     def display_history_prediction():

#         csv_path = "./Data/history.csv"
#         csv_exists = os.path.exists(csv_path)

#         if csv_exists:
#             history = pd.read_csv(csv_path)
#             st.dataframe(history)


#     if __name__ == '__main__':

#         st.title('History Page')
#         display_history_prediction()
        

# elif st.session_state['authentication_status'] is False:
#     st.error('Wrong username/password')
# elif st.session_state['authentication_status'] is None:
#     st.info('Login to get access to the app')
#     st.code("""
#     Test Account
#     Username: beela
#     Password: 456123
#     """)

# # st.write(st.session_state)