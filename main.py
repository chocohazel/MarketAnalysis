#!/usr/bin/env python3

import os
import sys
import subprocess
import pandas as pd
import matplotlib.pyplot as plot


# Opens the input file and parses the data into a list
def open_file( filepath ):
    symbol_list = []
    with open(filepath) as f:
        f = f.readlines()
    for symbol in f:
        symbol_list.append(symbol.strip())
    return symbol_list

# Runs the get_stock (bash script) file
def get_stock_info(SYMBOL):
    print(SYMBOL)
    infile = os.getcwd() + '/get_stock'
    subprocess.check_call([infile, SYMBOL])

# Makes a graph by analyzing the adjusted close price of a stock
def graph_adjusted_close_price(SYMBOL):
    stock = os.getcwd() + '/StockInfo/' + SYMBOL
    stock_data = pd.read_csv(stock + '.csv')
    df = pd.DataFrame(stock_data)
    df["Adj Close"].plot(grid=True)
    plot.xlabel('Time')
    plot.ylabel('Price')
    plot.savefig(stock + '.png')
    print ("Graph saved to %s.png" % SYMBOL)


if __name__ == "__main__":
    inf = sys.argv[1]
    infile = os.getcwd() + '/' + inf
    symbol_list = open_file(infile)
    for SYMBOL in symbol_list:
        print (SYMBOL)
        get_stock_info(SYMBOL)
        graph_adjusted_close_price(SYMBOL)
