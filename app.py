import streamlit as st
import joblib

# load the joblib model
model_nb = joblin.load('spam - ham')

st.title('SPAM HAM CLASSIFIER')
ip = st.text_input('ENTER YOUR TEXT:')

op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
                 
