import os
import streamlit as st
import pandas as pd
import joblib
import datetime

st.set_page_config(
    page_title ='Bulk Predict Page',
    page_icon ='🔮',
    layout="wide"
)
st.title("Bulk Prediction Page 🔮!")

# load the machine learning model components
@st.cache_resource
def load_logistic_reg_pipeline():
    pipeline = joblib.load('Models/new/Logistic_reg.joblib')
    return pipeline

@st.cache_resource
def load_adaboost_pipeline():
    pipeline = joblib.load('Models/new/AdaBoost.joblib')
    return pipeline

def select_model():
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox('Select a model', options=['Logistic Regression', 'AdaBoost'], key='selected_model')
    with col2:
        pass

    if st.session_state['selected_model'] == 'Logistic Regression':
        pipeline = load_logistic_reg_pipeline()
    else:
        pipeline = load_adaboost_pipeline()

    encoder = joblib.load('Models/encoder.joblib')

    return pipeline, encoder

def values_mapper(df,columns):
    """ This function takes two parameters and map the values in the column
    df: dataframe object
    columns_columns: columnsin in the dataframe that you want to map the values
    returns dataframe
    """
    for col in columns:
        cat_mapping = {True:"Yes",False:"No","No internet service":"No","No phone service":"No"}
        df[col] = df[col].replace(cat_mapping)
    return df

columns_to_map = ["PaperlessBilling","Partner","Dependents","PhoneService","StreamingMovies","StreamingTV","MultipleLines","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport"]

def make_bulk_prediction(pipeline,encoder,data):
    # make prediction
    df = pd.DataFrame(data)
    pred = pipeline.predict(df)
    # decode label to original label in the dataset
    decoded_prediction = encoder.inverse_transform(pred.reshape(-1,1))
    # calculate prediction probability 
    probabbility = pipeline.predict_proba(df)
    # probability_label
    prediction_label = ["Yes" if p == 1 else "No" for p in pred]
    # create a dataframe to store the prediction and probability
    df["PredictionTime"] = datetime.date.today()
    df["Prediction"] = prediction_label
    df["PredictionProbability"] = [probabbility[i][p] for i,p in enumerate(pred)]

    return df


if __name__ == "__main__":
    # call the get_selected_model function
   # pipeline,encoder = get_selected_model()
    
    # accept data from user
    uploaded_data = st.file_uploader("Upload your CSV data here for prediction",type="csv")

    if uploaded_data is not None:
        data = pd.read_csv(uploaded_data)

        # drop the churn column
        if "Churn" in data.columns:
            data = data.drop(columns="Churn",axis=1)
        # map the values in the columns
        data = values_mapper(data,columns=columns_to_map)
        # convert TotalCharges to numeric datatype
        data["TotalCharges"] = pd.to_numeric(data["TotalCharges"],errors="coerce")
        # map the senior citizen column into Yes or No
        data["SeniorCitizen"] = data["SeniorCitizen"].map({0:"No",1:"Yes"})
        
        # call the make predictions
        prediction_df = make_bulk_prediction(pipeline, encoder, data)
        st.markdown("### 👇View Prediction Result")
        st.write(prediction_df)

        # convert data to csv
        pred_csv = prediction_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download the Data",
            data=pred_csv,
            file_name="Prediction_Result.csv",
            mime="text/csv")
    else:
        st.write("Please upload your data")

   