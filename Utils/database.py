# # Import necessary libraries
# import streamlit as st
# import pyodbc
# import pandas as pd 
# import time
# from Utils.more_info import markdown_table1, markdown_table2

# # Set page configuration
# st.set_page_config(
#     page_title='Customer Churn Predictor Database',
#     page_icon='📊',
#     layout='wide',
#     initial_sidebar_state='expanded'
# )

# # Set page title
# st.title("Customer Churn Predictor Database ")

# # Function to initialize database connection
# @st.cache_resource(show_spinner="Connecting to database, please wait...")
# def init_connection():
#     """Establishes a connection to the SQL Server database."""
#     return pyodbc.connect(
#         f"DRIVER={{SQL Server}};SERVER={st.secrets['server']};DATABASE={st.secrets['database']};UID={st.secrets['username']};PWD={st.secrets['password']}"
#     )

# # Initialize database connection
# connection = init_connection()  

# # Function to execute SQL query
# @st.cache_data(show_spinner="running_query...")
# def running_query(query):
#     """Executes a SQL query and returns the result as a DataFrame."""
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         rows = cursor.fetchall()
#         df = pd.DataFrame.from_records(rows, columns=[column[0] for column in cursor.description])
#     return df

# def get_all_column():
#     """Fetches all columns from the LP2_Telco_churn_first_3000 table."""
#     sql_query = " SELECT * FROM LP2_Telco_churn_first_3000 "
#     df = running_query(sql_query)
#     return df

# def load_and_concat_datasets(first_dataset_func, second_dataset_path):
#     """
#     Load the first dataset using a provided function and the second dataset from a CSV file,
#     then concatenate them into a single DataFrame.
    
#     Parameters:
#     - first_dataset_func: function that returns a DataFrame for the first dataset.
#     - second_dataset_path: string path to the second dataset CSV file.
    
#     Returns:
#     - A concatenated DataFrame containing both datasets.
#     """
#     # Load the first dataset using the provided function
#     first_train = first_dataset_func()
    
#     # Load the second dataset from the provided CSV file path
#     second_train = pd.read_csv(second_dataset_path)
    
#     # Concatenate the two DataFrames
#     train_df = pd.concat([first_train, second_train], ignore_index=True)
    
#     return train_df

# train_df = load_and_concat_datasets(get_all_column, "./Data/LP2_Telco-churn-second-2000.csv")


# # Define a dictionary for mapping boolean and None values to more meaningful categories
# new_cat_values_mapping = {
#     'multiple_lines': {True: 'Yes', False: 'No', None: 'No phone service'},
#     'online_security': {True: 'Yes', False: 'No', None: 'No internet service'},
#     'online_backup': {True: 'Yes', False: 'No', None: 'No internet service'},
#     'device_protection': {True: 'Yes', False: 'No', None: 'No internet service'},
#     'tech_support': {True: 'Yes', False: 'No', None: 'No internet service'},
#     'streaming_tv': {True: 'Yes', False: 'No', None: 'No internet service'},
#     'streaming_movies': {True: 'Yes', False: 'No', None: 'No internet service'},
#     'churn': {True: 'Yes', False: 'No', None: 'No'},
#     'partner': {True: 'Yes', False: 'No'},
#     'dependents': {True: 'Yes', False: 'No'},
#     'paperless_billing': {True: 'Yes', False: 'No'},
#     'phone_service': {True: 'Yes', False: 'No'},
# }

# # Replace old categories with the new ones
# train_df.replace(new_cat_values_mapping, inplace=True)

# #create a progress bar to let user know data is loading
# progress_bar = st.progress(0)
# for perc_completed in range(100):
#     time.sleep(0.03)
#     progress_bar.progress(perc_completed+1)

# st.success("Data loaded successfully!")

# #grouping all numeric columns
# numerics = train_df.select_dtypes("number").columns
# #grouping all categorical columns
# categoricals = train_df.select_dtypes("object").columns

# col1,col2 = st.columns(2)
# with col1:
#     option = st.selectbox(
#         "How would you like to view data?",
#         ("All columns", "Numerical columns", "Categorical columns"),
#         index=None,
#         placeholder="Select contact method...",)
# # Conditionally display data based on the selected option
# if option == "All data":
#     st.write("### All Data")
#     st.dataframe(train_df)
#     if st.button("Click here to get more information about data dictionary"):
#         col3,col4 = st.columns(2)
#         with col3:
#         # Display the markdown table inside the expander
#             st.markdown(markdown_table1)
#         with col4:
#             st.markdown(markdown_table2)
# elif option == "Numerical columns":
#     st.write("### Numerical Columns")
#     st.dataframe(train_df[numerics])
#     if st.button("Click here to get more information about data dictionary"):
#         # Display the markdown table inside the expander
#         col3,col4 = st.columns(2)
#         with col3:
#         # Display the markdown table inside the expander
#             st.markdown(markdown_table1)
#         with col4:
#             st.markdown(markdown_table2)
# elif option == "Categorical columns":
#     st.write("### Categorical Columns")
#     st.dataframe(train_df[categoricals])
#     if st.button("Click here to get more information about data dictionary"):
#         # Display the markdown table inside the expander
#         col3,col4 = st.columns(2)
#         with col3:
#         # Display the markdown table inside the expander
#             st.markdown(markdown_table1)
#         with col4:
#             st.markdown(markdown_table2)