import streamlit as st
import numpy as np
import joblib
ml = joblib.load("lm.pkl")
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.indabaxtunisia.com/2023/assets/images/supcom.png");
    background-size: cover;
    opacity: 0.1;  /* transparency: 1 = opaque, 0 = fully transparent */
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)
Study_Hours=st.slider("study hours", 0.0,10.0)
Attendance=st.slider("Attendance", 50.0 , 100.0)
Practice_Tests=st.slider("how many exams did u practice on",0,7,step=1)
if st.button("Predict final score !"):
    input_data= np.array([[Study_Hours,Attendance,Practice_Tests]])
    prediction=ml.predict(input_data)[0]
    prediction=max(0,min(100,prediction))
    if prediction < 50 : 
        string='LMARRA EJEYA NCHALLAH'
        st.error(f"⚠️ the predicted score is {int(prediction*100)/100} {string}")
    else :
        string='MABROUUK'
        st.success(f"the predicted score is {int(prediction*100)/100} {string}")
