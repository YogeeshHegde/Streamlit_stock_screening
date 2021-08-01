# Streamlit_stock_screening
Streamlit webapp to screen Indian stocks from NSEbhavcopy data.

# Overview
Hobby project which aids in screening the stocks from Indian market.
Currently, this webapp consists of candle stick charts along with simple moving average (10, 20 and 44).
Selection of stocks can be made via selection types like All, CN100 etc.

![Streamlit webapp Overview](./screeshots/Webapp_overview.png) 

# Stock Data
Stock data (Bhavcopy) are downloaded from www.nseindia.com and consolidated as a csv file - "NSE_Bhavcopy.csv".

# How to run?
- Install all the necessary dependencies
- Run command: "streamlit run Stock_screening.py" in cmd/Terminal

# TODO
- Add selection types such as NSE CN200, CN500 etc 
- Add Selection types based on sectors (Bank, IT, Pharma etc)
- Consolidate Stock data from previous years
- Add screeners
