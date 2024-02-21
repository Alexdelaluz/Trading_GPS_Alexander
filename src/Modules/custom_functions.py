# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:09:29 2024

@author: alex_
"""

import os
import pandas as pd
import mplfinance as mpf

# Load stock data
def load_stock_data(directory_path):
    return {ticker[:-4]: pd.read_csv(os.path.join(directory_path, ticker)) for 
            ticker in os.listdir(directory_path)}


# Modify data and plot
def custom_plotting(stock_data, stock_name, save_plot=False, save_path=None):
    db_dict = {
        'c_adjusted_open': 'Open',
        'c_adjusted_high': 'High',
        'c_adjusted_low': 'Low',
        'm_adjusted_close': 'Close',
        'm_volume': 'Volume',
        'm_close': 'Adj Close',
        'c_relative_strength_index_14d': 'RSI'
    }
    
    # Get the DF of the stock and modify
    data = stock_data[stock_name].copy()
    data = data.rename(columns=db_dict)
    data['m_date'] = pd.to_datetime(data['m_date'])
    data.set_index('m_date', inplace=True)
    
    #RSI
    rsi = mpf.make_addplot(data['RSI'], color='darkorchid' , panel=2 )

    # Plot the stock
    fig, axes = mpf.plot(data,
                         type='candle',
                         volume=True,
                         style='yahoo', 
                         axtitle=f'{stock_name} Stock (2022-2024)',
                         mav=(21,63,252),
                         addplot=rsi,
                         tight_layout=True,
                         figsize=(12, 8),
                         returnfig=True
                         )
    
    # Save the plot
    if save_plot:
        if save_path is None:
            save_path = os.path.join('Output', f"{stock_name}_plot.png")
        else:
            save_path = os.path.join('Output', save_path)
        
        fig.savefig(save_path, bbox_inches='tight')
        


stock_data = load_stock_data('Input/Data_and_Features')
custom_plotting(stock_data, 'NFLX', save_plot=True)