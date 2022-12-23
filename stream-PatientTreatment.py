import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open('Patient_Treatment.sav', 'rb'))

# Judul web
st.title('Data Mining Prediksi Perawatan Pasien')

col1, col2 = st.columns(2)

with col1:
    heamatocrit = st.number_input('Input Nilai Heamatocrit')

with col2:
    heamoglobins = st.number_input('Input Nilai Heamoglobins')

with col1:
    erythrocyte = st.number_input(' Input Nilai Erythrocyte')

with col2:
    leucocyte = st.number_input('Input Nilai Leucocyte')

with col1:
    thrombocyte = st.number_input('Input Nilai Thrombocyte')

with col2:
    mch = st.number_input('Input Nilai Mch')

with col1:
    mchc = st.number_input(' Input Nilai Mchc')

with col2:
    mcv = st.number_input('Input Nilai Mcv')

with col1:
    age = st.number_input('Input Nilai Age')

with col2:
    sex = st.number_input('Input Nilai Sex')

# code untuk prediksi
    perawatan_diagnosis = ''

# membuat tombol
if st.button('Mulai'):
    perawatan_prediction = model.predict([[heamatocrit, heamoglobins, erythrocyte, leucocyte, thrombocyte, mch, mchc, mcv, age,
                                          sex]])

    if (perawatan_prediction[0] == 1):
        perawatan_diagnosis = 'Pasien Rawat Inap'
    else:
        perawatan_diagnosis = 'Pasien Rawat Jalan'

st.success(perawatan_diagnosis)
