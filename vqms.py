import streamlit as st
import datetime as dt
import re
import numpy as np
import pandas as pd


df = pd.read_excel('Vedanta_DB.xlsx')
df = pd.DataFrame(df)
 

@st.cache(allow_output_mutation=True)
def get_data():
    return []

def check(string_inp):
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if(regex.search(string_inp) != None):
        st.sidebar.error("Invalid Input")
        return 1
    else:
        return 0

def update(nam_inp):
    global df
    count=0
    t2 = dt.datetime.strptime('00:30:00', '%H:%M:%S')
    t3 = dt.datetime.strptime('00:15:00', '%H:%M:%S')
    time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
    endc =int(df['Name'].count())
    for i in range(0,endc-1):
        nm = str(df['Name'][i])
        if(nam_inp == nm):
            for j in range(i,endc-1):
                ti = dt.datetime.strptime(str(df['ArrTime'][j]),'%H:%M:%S') - time_zero + t2
                ti2 = dt.datetime.strptime(str(df['ArrTime'][j+1]),'%H:%M:%S')
                if(ti == ti2):
                    count += 1
                elif((ti2 - ti + dt.datetime(1900,1,1)) >= t2):
                    st.write("Found an empty slot at", ti.time(), "\nAdding to time slot...")
                    time_inp = ti.time()
                    up_hlf = [*range(0, j+1, 1)]
                    low_hlf = [*range(j+1, df.shape[0],1)]
                    low_hlf = [x.__add__(1) for x in low_hlf]
                    ind = up_hlf + low_hlf
                    df.index = ind
                    df.loc[j+1] = [nam_inp, time_inp]
                    for k in range(j,endc):
                        t4 = ((dt.datetime.strptime(str(df['ArrTime'][k]),'%H:%M:%S') - t3) + dt.datetime.min).time()
                        df['ArrTime'][k] = t4
                    df.drop([i], inplace=True)
                    df.sort_index(inplace=True)
                    
                    break
            if(count == endc-1-i):
                df.drop([i], inplace=True)
                st.write('No slots found in between, adding slot at the end')
                st.write('Adding new timestamp...')
                time_inp = (dt.datetime.strptime(str(df['ArrTime'][endc-1]), '%H:%M:%S') - time_zero + t2).time()
                df.loc[len(df.index)+1] = [nam_inp, time_inp]
                for j in range(i+1,endc+1):
                    t4 = ((dt.datetime.strptime(str(df['ArrTime'][j]),'%H:%M:%S') - t3) + dt.datetime.min).time()
                    df['ArrTime'][j] = t4
            df.reset_index(drop=True,inplace=True)
            break
    return df


def cancel(nam_inp):
    global df
    t2 = dt.datetime.strptime('00:15:00', '%H:%M:%S')
    st.write('Cancelling Booking... \nAssigning new time to users...')
    for i in range(0,df['Name'].count()):
        if(nam_inp == df['Name'][i]):
            df.drop([i], inplace=True)
            df.reset_index(drop=True, inplace=True)
            for j in range(i,df['Name'].count()):
                ti = ((dt.datetime.strptime(str(df['ArrTime'][j]),'%H:%M:%S') - t2) + dt.datetime.min).time()
                df['ArrTime'][j] = ti
            break
    return df


def add(nam_inp):
    global df
    #name_inp = str(input('Enter name of user: '))
    st.write('Adding to existing queue...')
    t2 = dt.datetime.strptime('00:30:00', '%H:%M:%S')
    time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
    time_inp = (dt.datetime.strptime(str(df['ArrTime'][len(df.index)-1]), '%H:%M:%S') - time_zero + t2).time()
    get_data().append({"Name": nam_inp, "ArrTime": time_inp})
    if(len(get_data())>1):
        for i in range(len(get_data())-1, 0, -1):
            get_data()[i]['ArrTime'] = (dt.datetime.strptime(str(get_data()[i-1]['ArrTime']), '%H:%M:%S') - time_zero + t2).time()
    df = df.append(pd.DataFrame(get_data()))
    get_data().clear()
    df.reset_index(drop=True, inplace=True)
    return df
        
