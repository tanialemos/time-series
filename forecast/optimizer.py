import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import riskfolio as rf

def download_prices(tickers_list, start_date, end_date):
    data = yf.download(tickers_list, start = start_date, end = end_date)
    data = data.loc[:,("Adj Close")]
    data.columns = tickers_list
    data = data.reset_index()
    #data_resample = data.resample("D", on = "Date").last() # TODO according to user input
    #data_resample = data_resample.dropna()
    #data_resample = data_resample.reset_index()
    print(data)

def optimize(tickers_list, start_date, end_date):
    download_prices(tickers_list, start_date, end_date)