import yfinance as yf
import streamlit as st

st.write("""
# Current Stocks Price Quotes
Showing the stock closing price and volume of : 
""")

st.write("""
## Google Inc.
""")
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
         Google - Closing Prices
          """)
st.line_chart(tickerDf.Close)
st.write("""
         Google - Volume
          """)
st.line_chart(tickerDf.Volume)

st.write("""
## Apple Inc.
""")
tickerSymbol = 'AAPL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
         Apple - Closing Prices
          """)
st.line_chart(tickerDf.Close)
st.write("""
         Apple - Volume
          """)
st.line_chart(tickerDf.Volume)


st.write("""
## Tesla
""")
tickerSymbol = 'TSLA'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
         Tesla - Closing Prices
          """)
st.line_chart(tickerDf.Close)
st.write("""
         Tesla - Volume
          """)
st.line_chart(tickerDf.Volume)


st.write("""
## IBM
""")
tickerSymbol = 'IBM'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
         IBM - Closing Prices
          """)
st.line_chart(tickerDf.Close)
st.write("""
         IBM - Volume
          """)
st.line_chart(tickerDf.Volume)


st.write("""
## Microsoft
""")
tickerSymbol = 'MS'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
         Microsoft - Closing Prices
          """)
st.line_chart(tickerDf.Close)
st.write("""
         Microsoft - Volume
          """)
st.line_chart(tickerDf.Volume)
st.write("""
         [Powered by CarmelSoft](https://carmelsoft.netlify.app "CarmelSoft's Homepage")
          """)
