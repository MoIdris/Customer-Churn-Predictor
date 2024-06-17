import streamlit as st
import pyodbc
import pandas as pd
import time

st.set_page_config(
    page_title='Dashboard Page',
    page_icon='📈',
    layout='wide',
    initial_sidebar_state='expanded'
)