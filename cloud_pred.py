# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:31:46 2024

@author: Lenovo
"""

import pickle
import streamlit as st
import numpy as np
zta_model= pickle.load(open('zta_finalized_model.sav','rb'))

st.markdown(
    """
    <h1 style='font-size:30px; margin-bottom:0;'>
        Enhancing Cloud Security through Continuous Verification: A Zero Trust Approach to Identity and Access Management
    </h1>
    """,
    unsafe_allow_html=True
)

headings = [
    ' Fwd Packet Length Max', 'Total Length of Fwd Packets', 'Init_Win_bytes_forward', ' Total Fwd Packets', ' act_data_pkt_fwd', 'Bwd Packet Length Max', ' Destination Port', ' Bwd Packet Length Min', 'Bwd IAT Total', ' Init_Win_bytes_backward'
]

RED_SCREEN_CSS = """
<style>
body {
    background-color: red !important;
}
</style>
"""
num_columns = 2
columns = st.columns(num_columns)

# Dictionary to store inputs
inputs = {}

# Iterate through the headings and create input fields in the columns
for idx, heading in enumerate(headings):
    col = columns[idx % num_columns]  # Select the column
    inputs[heading] = col.number_input(
        heading, value=0.0, step=0.1, 
    )  # Default is 0.0, step by 0.1

zta_result= ''
# Display submitted inputs
if st.button("Predict"):
    input_values = [float(inputs[heading]) for heading in headings]
    input_array = np.array(input_values).reshape(1, -1)
    zta_prediction = zta_model.predict(input_array)
    
    
    if(zta_prediction[0]==0):
        zta_result="Benign"
        st.success(zta_result)
    else:
        st.markdown(RED_SCREEN_CSS, unsafe_allow_html=True)
        zta_result="Malicious"
        st.error(zta_result)
    
        
   
   
    
   
    