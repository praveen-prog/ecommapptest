import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns

def title_call():
    st.title("This is an EComm App")
    st.sidebar.title("you can upload the file here.")
    upload_file = st.sidebar.file_uploader("upload your file" ,  type = ['csv','xlsx'])

    if upload_file is not None:
        try:
            if upload_file.name.endswith('csv'):
                data = pd.read_csv(upload_file)

            else:
                data = pd.read_excel(upload_file)    
            st.sidebar.success('File Uploaded Successfully') 

            st.subheader("Data Details")
            st.dataframe(data.head())
            st.subheader("More cases in Data")
            st.write("Shape of the data", data.shape)
            st.write("Columns are ", data.columns)
            st.write("Missing Columns", data.isnull().sum())

            st.subheader("Some Stats")
            st.write(data.describe())

        except Exception as e:
            print(e)    


if __name__ == "__main__":
    title_call()    
