import streamlit as st
def calculate_emi(p,n,r):
	emi=p*(r/100)*(1+(r/100)**n)/(((1+(r/100))**n)-1)
	st.write("EMI Calculated=",emi)

st.title("EMI Calculator")
principal=st.slider("Loan Amount",1000.0,1000000.0)
tenure=st.slider("Time Period of Loan",1,50)
roi=st.slider("Rate of Interest",1,20)
if st.button("Calculate"):
	calculate_emi(principal,tenure,roi)

