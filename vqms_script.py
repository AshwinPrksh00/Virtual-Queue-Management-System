import streamlit as st
import datetime as dt
import numpy as np
import pandas as pd


st.set_page_config(
    page_title= 'VQMS Branch',
    page_icon= "https://i.ibb.co/YpvKQnc/CompLogo.jpg"
)

from vqms import df, check, add, cancel, update

#CSS Stylings
title_style = """<div style="background-image: linear-gradient(to right, #00467F , #A5CC82); width: 130%; float: left; padding: 10px; border-radius: 20px;">
<h2 style="color:white; text-align:left; text-indent: 35px;"><b>Vedanta Medical Shop</b></h2>
</div>"""
 

war_style = """<div style="background-image: linear-gradient(to right, #4b6cb7, #182848); padding: 5px; border-radius: 25px; width: 130%">
<h4 style="color: white; text-align: center; text-indent: 30px;"><b>Empty Name cannot be entered</b></h4>
</div>"""

img_style = """<div style="background-color: black; width: 304px; border-radius: 15px;">
    <img src="https://i.ibb.co/YpvKQnc/CompLogo.jpg" alt="Logo" style=" border-radius: 10px; width: 150px; height: 100px; display: block; margin-left: auto; margin-right: auto;">
    </div><br>"""

warn_style = """<br><label style="font-size: 25px; font-weight: bold; background-image: linear-gradient(to right, #DA4453 ,#89216B); background-size: 100%;-webkit-background-clip: text;
  -webkit-text-fill-color: transparent; 
  -moz-background-clip: text;
  -moz-text-fill-color: transparent;">Avoid Special Characters</label>"""

war1_style = """<div style="background-image: linear-gradient(to right, #4b6cb7, #182848); padding: 5px; border-radius: 25px; width: 130%">
<h4 style="color: white; text-align: center;"><b>Customer not found in Database</b></h4>
</div>"""

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
st.sidebar.markdown(img_style, unsafe_allow_html=True)
option = st.sidebar.selectbox('Menu', ['Home', 'Operations'])
st.markdown(title_style,unsafe_allow_html=True)
if option == 'Home':
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div style="background-image: linear-gradient(to right, #334d50, #cbcaa5); padding: 1px; border-radius: 25px; width: 130%">
        <h2 style="color: white; text-indent: 35px;"><b>Homepage</b></h2>
        </div> <br>""",unsafe_allow_html=True)
    c1,c2 = st.beta_columns([0.5,1])
    c2.write(df)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div style="background-image: linear-gradient(to right, #1f4037, #99f2c8); padding: 1px; border-radius: 25px; width: 130%">
        <h2 style="color: white; text-indent: 35px;"><b>Statistics</b></h2>
        </div> <br>""",unsafe_allow_html=True)
    kpi1,kpi2,kpi3 = st.beta_columns(3)
    

    with kpi1:
        st.markdown("**No of person in queue**", unsafe_allow_html=True)
        number = df['Name'].count()-1
        st.markdown(f"<label style='display: block; font-weight: bold; text-align: center; text-indent: -70px; color: red; font-size: 20px;'>{number}</label>",unsafe_allow_html=True)
    
    with kpi2:
        st.markdown("**First Person**", unsafe_allow_html=True)
        st.markdown(f"<label style='display: block; font-weight: bold; text-align: center; text-indent: -70px; color: red; font-size: 20px;'>{df['Name'][0]}</label>",unsafe_allow_html=True)
        
    
    with kpi3:
        st.markdown("**Last Person**", unsafe_allow_html=True)
        st.markdown(f"<label style='display: block; font-weight: bold; text-align: center; text-indent: -70px; color: red; font-size: 20px;'>{df['Name'][df['Name'].count()-1]}</label>",unsafe_allow_html=True)

    st.markdown("<hr/>",unsafe_allow_html=True)
    kpi4,kpi5 = st.beta_columns(2)
    
    with kpi4:
        st.markdown("**Entry Time**",unsafe_allow_html=True)
        t01 = df['ArrTime'][0]
        z1 = 'AM'
        if dt.datetime.strptime(str(df['ArrTime'][0]),'%H:%M:%S') == dt.datetime.strptime('12:00:00', '%H:%M:%S'):
            z1 = 'PM'
        if dt.datetime.strptime(str(df['ArrTime'][0]),'%H:%M:%S') > dt.datetime.strptime('12:59:00', '%H:%M:%S'):
            z1 = 'PM'
            t01 = ((dt.datetime.strptime(str(df['ArrTime'][0]),'%H:%M:%S') - dt.datetime.strptime('12:00:00', '%H:%M:%S')) + dt.datetime.min).time()
        st.markdown(f"<label style='display: block; font-weight: bold; text-align: center; text-indent: -70px; color: red; font-size: 20px;'>{t01} {z1}</label>",unsafe_allow_html=True)

    with kpi5:
        st.markdown("**Exit Time**",unsafe_allow_html=True)
        t02 = df['ArrTime'][df['Name'].count()-1]
        z2 = 'AM'
        if dt.datetime.strptime(str(df['ArrTime'][df['Name'].count()-1]),'%H:%M:%S') > dt.datetime.strptime('12:59:00', '%H:%M:%S'):
            z2 = 'PM'
            t02 = ((dt.datetime.strptime(str(df['ArrTime'][df['Name'].count()-1]),'%H:%M:%S') - dt.datetime.strptime('12:00:00', '%H:%M:%S')) + dt.datetime.min).time()
        st.markdown(f"<label style='display: block; font-weight: bold; text-align: center; text-indent: -70px; color: red; font-size: 20px;'>{t02} {z2}</label>",unsafe_allow_html=True)

    st.markdown("<hr/>",unsafe_allow_html=True)

elif option == 'Operations':
    col1, col2, col3 = st.beta_columns([0.5,0.5,1])
    name_inp = st.sidebar.text_input("Enter name of user:")
    ret = check(name_inp)
    m = col1.button('Add Customer', key='a')
    p = col2.button('Cancel Booking', key='b')
    r = col3.button('Update Customer Timing', key='c')
    col4, col5 = st.beta_columns([0.5,1])
    if m:
        if len(name_inp)>0 and ret==0:
            df = add(name_inp)
            col5.write(df)
        elif len(name_inp)<=0:
            st.markdown(war_style, unsafe_allow_html=True)
        elif ret!=0:
            col5.markdown(warn_style, unsafe_allow_html=True)
    if p:
        if len(name_inp)>0 and ret==0:
            if name_inp not in df.values:
                st.markdown(war1_style, unsafe_allow_html=True)
            else:
                df = cancel(name_inp)
                col5.write(df)
        elif len(name_inp)<=0:
            st.markdown(war_style, unsafe_allow_html=True)
        elif ret!=0:
            col5.markdown(warn_style, unsafe_allow_html=True)
    if r:
        if len(name_inp)>0 and ret==0:
            if name_inp not in df.values:
                st.markdown(war1_style, unsafe_allow_html=True)
            else:
                df = update(name_inp)
                col5.write(df)
        elif len(name_inp)<=0:
            st.markdown(war_style, unsafe_allow_html=True)
        elif ret!=0:
            col5.markdown(warn_style, unsafe_allow_html=True)

