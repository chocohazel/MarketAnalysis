# MarketAnalysis

Author: Kshitij Kayastha, Joshua Weisberg
Date: 20 March 2019
Course: CS265
Description: Final Project


1. Project Description

Our project is based on scraping stock market data from Yahoo! Finance and analyzing (not much, very basic analysis) the data to inform the user if the price has jumped by a significant amount.

2. Files

a. get_stock:
        used - grep, sed and curl | defined functions | parameter expansions | tests |
        description - retrieves data from Yahoo! Finance, creates a new directory called StockInfo, and saves the data in a csv file in this directory.
b. input:
        description -  stack of symbols (stock) for input
c. main.py:
        dependecies: get_stock, input
        description - Main high level function. For each SYMBOL in input, it passes the SYMBOL as an argument to the get_stock file. It then creates a graph of that stock and saves it into the
        StockInfo directory as a png file.
d. mailParser:
        used - awk and mail | parameter expansion | tests |
        description - compares the open price of the current day with the close price of the previous day, and depending on the change in price, it triggers an email.
        The open price is on column 2 while the close price is on column 5. If the percentage change in the prices exceed +-20%, an email will be triggered to the user.
e. crontab:
        description - runs our scripts every day at 9am (NYSE opens at 9am)
        Here is our crontab contents:

        00 09 * * * cd /file/path/to/project/; make run-py
        00 09 * * * cd /file/path/to/project/; make mail-test
        The crontab needs to be editted by the user.
      
