import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
Stock Price Application

Shown are the stock closing price and volume of DAIMLER  

""")
tickerSymbol = 'DDAIF'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2008-1-1', end='2021-11-30')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)