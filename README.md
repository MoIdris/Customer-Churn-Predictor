# Customer-churn-Predictor : Embedding Machine Learning Models in GUIs

## 📚 Table of Contents

1. [Introduction](#-introduction)
2. [Project Overview](#-project-overview)
   - [The Importance of Customer Churn Prediction](#the-importance-of-customer-churn-prediction)
   - [Machine Learning Models](#machine-learning-models)
   - [Dataset and Model](#dataset-and-model)
3. [Streamlit Web Application](#-streamlit-web-application)
   - [Home Page](#home-page)
   - [Data Page](#data-page)
   - [Visualize Page](#visualize-page)
   - [Predict Page](#predict-page)
   - [History Page](#history-page)
4. [Conclusion](#-conclusion)
5. [Authors](#-authors)
6. [Show your support](#-show-your-support)
7. [Acknowledgments](#-acknowledgments)
8. [License](#-license)


## 📄 Introduction

Customer churn poses a significant challenge for many large companies, particularly in the telecommunications sector. The direct impact on revenue makes it crucial for businesses to predict and effectively mitigate churn. In this project, I created a web application using Streamlit to predict customer churn based on various features. The application offers an intuitive interface for data exploration, trend visualization, and machine learning-based predictions.

---

## 🏗️ Project Overview

### The Importance of Customer Churn Prediction

Predicting customer churn is essential for businesses aiming to enhance customer retention and optimize marketing strategies. By identifying at-risk customers, companies can proactively implement measures to retain them, ultimately improving business performance and increasing customer lifetime value.

### Machine Learning Models

The Streamlit web application incorporates the best-performing models—Logistic Regression and AdaBoost—derived from my analysis. These models were carefully evaluated using metrics such as accuracy, precision, recall, and F1-score. The selected models were then deployed within the Streamlit framework to provide accessible and actionable churn predictions for business users.

### Dataset and Model

The dataset used contains customer information, including demographics, account details, and subscribed services. Our primary objective was to build a model capable of predicting whether a customer would churn (i.e., leave the service) or remain. Following the CRISP-DM framework, we engaged in data cleaning, exploration, feature engineering, model training, and evaluation.

---

## 💻 Streamlit Web Application

To create an interactive and user-friendly interface for our churn prediction models, we developed a Streamlit web application. The application comprises several pages, each serving a specific purpose:

### 🏠 Home Page

The Home page serves as an introduction to the application. It provides an overview of the project, explaining the importance of churn prediction and how the application can help users understand and predict customer churn. The page sets the context and guides users on how to navigate through the app.

### 📊 Data Page

The Data page allows users to explore the dataset used for building the churn prediction model. Users can view the dataset, apply filters based on specific criteria, and gain insights into data distribution. This page serves as a familiarization point, helping users understand the various features relevant to churn prediction.

### 📈 DashBoard Page

The Visualize page empowers users to create visualizations that reveal relationships and trends within the data. For instance, users can explore the distribution of customers across different tenures, payment methods, or monthly charges. These visualizations aid in identifying patterns and correlations that may influence customer churn.

### 🔍 Predict Page

The Predict page enables users to input customer data and receive real-time churn predictions from the machine learning model. Users can manually input data via forms or upload a CSV file for batch predictions. The page displays whether a customer is likely to churn and provides associated probabilities.

### 📜 History Page

The History page maintains a record of all predictions made by the user. It includes input data and corresponding predictions, serving as a reference for analysis and trend tracking. This feature proves valuable for monitoring historical churn predictions.

---

## 🔚 Conclusion

Through the development of this Streamlit web application, we have made customer churn prediction accessible and actionable for business users. The application provides an intuitive interface for exploring data, visualizing trends, and making predictions using machine learning models. This project demonstrates the power of integrating data science and web development to solve real-world business problems.


#### 👥 Authors

🕵🏽‍♀️ **Mohammed Idris**

- GitHub: [GitHub Profile](https://github.com/MoIdris)
- Twitter: [Twitter Handle](https://twitter.com/IdrisBaaba)
- LinkedIn: [LinkedIn Profile](www.linkedin.com/in/idris-ibn-mohammed)
- Medium: [Medium Profile](https://medium.com/@idmoh44)


** 🤝 Contributors**

Elvis Yeboah

#### ⭐️ Show your support

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

#### 🙏 Acknowledgments

I express my sincere gratitude to all my tutors at Azubi Africa and my dedicated team members. Their guidance, unwavering support, and diligent efforts throughout this project have been invaluable. Their expertise, insights, and collaborative spirit significantly influenced the analysis and outcomes, making this endeavor a success.

#### 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

