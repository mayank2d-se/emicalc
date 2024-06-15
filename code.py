import streamlit as st

st.title('EMI calculator')

loan_amt = st.text_input(label = "Amount of loan taken")

ROI = st.text_input(label = "Annual Rate of interest(%)")

NPER = st.text_input(label = "In how many years, you want to pay it back")


loan_amt = float(loan_amt) if loan_amt else 0
ROI = float(ROI) if ROI else 0
NPER = int(NPER) if NPER else 0

def emi(loan_amt, ROI, NPER):
    roi = ((1+(ROI/100))**(1/12))-1
    nper = NPER*12
    emi = (loan_amt*roi*(1+roi)**(nper))/((1+roi)**(nper)-1)
    return " Monthly emi is {}".format(round(emi,2))
    
if st.button("calculate", key = "calculate_button"):
    if loan_amt>0 and ROI>0 and NPER>0 :
        result = emi(loan_amt, ROI, NPER)
        st.write(result)
    else :
        st.error("Please fill all values required")
