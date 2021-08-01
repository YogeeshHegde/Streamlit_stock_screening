import pandas as pd
import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
from symlist import *

df = pd.read_csv('NSE_Bhavcopy.csv')
df['TIMESTAMP']= pd.to_datetime(df['TIMESTAMP'])

st.title('Stock Technical Analysis')
st.sidebar.title("Stock Technical Analysis")
select_type = st.sidebar.selectbox('Select Type',['All','CN100'] )
select = 'ITC'
if select_type == 'All':
    select = st.sidebar.selectbox('Select SYMBOL',All)
elif select_type == 'CN100':
    select = st.sidebar.selectbox('Select SYMBOL',CN100)

#Simple Moving average calculation
df_for_plot = df.loc[(df['SYMBOL'] == select) & (df['SERIES'] == 'EQ')]
df_for_plot['SMA44'] = df_for_plot['CLOSE'].rolling(44).mean()
df_for_plot['SMA10'] = df_for_plot['CLOSE'].rolling(10).mean()
df_for_plot['SMA20'] = df_for_plot['CLOSE'].rolling(20).mean()

#Data for plotting
data1 = { 'x': df_for_plot.TIMESTAMP, 
		'open': df_for_plot.OPEN, 
		'close': df_for_plot.CLOSE, 
		'high': df_for_plot.HIGH, 
		'low': df_for_plot.LOW, 
		'type': 'candlestick',}
		
data2 = { 'x': df_for_plot.TIMESTAMP, 
		'y': df_for_plot.SMA44, 
		'type': 'scatter', 
		'mode': 'lines', 
		'line': { 'width': 1, 'color': 'blue' },
		'name': 'SMA 44'}
		
data3 = { 'x': df_for_plot.TIMESTAMP, 
		'y': df_for_plot.SMA20, 
		'type': 'scatter', 
		'mode': 'lines', 
		'line': { 'width': 1, 'color': 'red' },
		'name': 'SMA 20'}
		
data4 = { 'x': df_for_plot.TIMESTAMP, 
		'y': df_for_plot.SMA10, 
		'type': 'scatter', 
		'mode': 'lines', 
		'line': { 'width': 1, 'color': 'green' },
		'name': 'SMA 10 periods'}
data = [data1, data2, data3, data4]
fig = go.Figure(data=data)

#update figure layout
fig.update_layout(
    title={
        'text': "SYMBOL = " + select,
        'xanchor': 'left',
        'yanchor': 'top'}
)

st.subheader('Candlestick chart with SMA curves')
st.write('Data Range: 04/01/2021 to 30/07/2021')
st.plotly_chart(fig)