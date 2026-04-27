import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title('Lappytol')

company = st.selectbox('Brand', df['Company'].unique())
type = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('Ram(GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
os = st.selectbox('OS', df['OpSys'].unique())
weight = st.number_input(label='Weight of Laptop')
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS', ['No', 'Yes'])
screen_size = st.number_input('Screen Size')
fullhd = st.selectbox('Full HD', ['No', 'Yes'])
resolution = st.selectbox('Screen Resolution', ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
cpu = st.selectbox('Brand', df['Cpu brand'].unique())
hdd = st.selectbox('HDD(GB)', [0, 128, 256, 512, 1024, 2048])
ssd = st.selectbox('SSD(GB)', [0, 8, 128, 256, 512, 1024, 2048])
gpu = st.selectbox('GPU', df['Gpu brand'].unique())

if st.button('Predict Price'):
    try:
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if fullhd == 'Yes':
            fullhd = 1
        else:
            fullhd = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        x_res = int(resolution.split('x')[0])
        y_res = int(resolution.split('x')[1])
        if screen_size != 0:
            ppi = (((x_res) ** 2 + (y_res) ** 2) ** 0.5) / screen_size
        else:
            ppi = 0

        query_df = pd.DataFrame(data=[[company, type, ram, weight, touchscreen, fullhd, ips, ppi, cpu, hdd, ssd, gpu, os]],
                                columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Full HD', 'IPS', 'ppi',
                                         'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'OpSys'])

        predicted_price = int(np.exp(pipe.predict(query_df)[0]))
        formatted_price = "{:,.2f}".format(predicted_price)

        st.title("Predicted Price: " + formatted_price)

    except Exception as e:
        st.error(f"An error occurred: {e}")
