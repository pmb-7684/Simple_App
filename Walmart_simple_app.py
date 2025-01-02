import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
    ## Simple Stock Price App
         
    Shown are stock opening price, closing price, volume sold, and dividends paid for **Walmart**.

""")


symbol = 'WMT'
# call Ticker in yfinance
tickerInfo = yf.Ticker(symbol)
# Get historical data for the past 10 years
tickerDF = tickerInfo.history(period='1d', start = '2014-12-01', end='2024-12-01')

st.write(""" 
         #### Opening Price
         """)
st.line_chart(tickerDF.Open)
st.write(""" 
         #### Closing Price
         """)
st.line_chart(tickerDF.Close)
st.write(""" 
         #### Volume Sold
         """)
st.line_chart(tickerDF.Volume)
st.write(""" 
         ####  Dividends Paid
         """)
st.line_chart(tickerDF.Dividends)
