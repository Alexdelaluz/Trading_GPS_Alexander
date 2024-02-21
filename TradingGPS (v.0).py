# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 21:26:10 2024

@author: alex_
"""
from src.Modules import custom_functions as fn
import os

#Set Working Environment for the Console
os.chdir('C:\\Users\\alex_\\OneDrive\\Escritorio\\KaxaNuk\\Trading_GPS_Alex')


#Load the data
fn.stock_data = fn.load_stock_data('Input/Data_and_Features')

#List of Stocks to plot and plotting
list_of_stocks = ['NFLX', 'AAPL', 'EA', 'FOX']

for stock_name in list_of_stocks: 
    fn.custom_plotting(fn.stock_data, stock_name, save_plot=True)