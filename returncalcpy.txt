import streamlit as st
st.title('Return calculator')

if 'show_options' not in st.session_state:
    st.session_state.show_options = False

if st.button('Type', key = 'A'):
    st.session_state.show_options = True

if st.session_state.show_options:
    options = ['Fixed deposit','Recurring deposit']
    choice = st.selectbox('Choose your investment type :', options)
    if choice == 'Fixed deposit':
        st.header('Fixed deposit')
        PRIN = st.number_input('What amount you want to invest?')
        ROI = st.number_input('Annual rate of interest(%)')
        NPER = st.number_input('For how many years you want to invest?')
        if st.button('calculate', key = 'B'):
            def fd_r(PRIN, ROI, NPER):
                fd_r = PRIN*((1+ (ROI/100))**(NPER))
                return 'Your amount will become :{}'.format(round(fd_r))
            if PRIN>0 and ROI>0 and NPER>0:
                RESULT = fd_r(PRIN, ROI, NPER)
                st.write(RESULT)
            else:
                st.write('Please enter all values required')
        
    elif choice == 'Recurring deposit':
        st.header('Recurring deposit')
        prin = st.number_input('What amount you want to invest monthly?')
        Roi = st.number_input('Annual rate of interest(%)')
        Nper = st.number_input('For how many years you want to invest?')
        if st.button('calculate', key = 'C'):
            def rd_r(prin, Roi, Nper):
                roi = ((1+ (Roi/100))**(1/12)-1)
                nper = Nper*12
                rd_r = (prin*(1+ roi)*((1+ roi)**(nper)-1))/(roi)
                return 'Your amount will become : {}'.format(round(rd_r))
            if prin>0 and Roi>0 and Nper>0:
                result = rd_r(prin, Roi, Nper)
                inv = prin*(Nper*12)
                st.write('Total amount invested :{}'.format(round(inv)))
                st.write(result)
            else:
                st.write('Please enter all values required')
