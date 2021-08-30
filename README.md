# Trading Bot

A trading bot who sends buy or sell signals.



# Description

 This is real-time Crypto Trading Bot using Binance API and Websockets.WebSocket is a computer communications protocol, providing full-duplex communication channels over a single TCP connection. 
In class Main we receive messages from Binance and print them in json format so we could read them better.After that we append the closing price in Info class from where the other classes will get the information.
This way we avoid circular dependancy.Indicator classes MA and SAR(Moving average, Parabolic Sar) will need the list of prices located in class Info because in indicator classes we use TA-Lib (technical analysis library).
This library actually has function for every indicator and takes different parameters.Every indicator has its own calculation and talib library does this calculations.
This is why in class Main we check the length of list of prices and if it is more than one , we can already have the parabolic  sar indicator shown.if the length is more than 20 talib will be able to calculate the 20 period moving average
indicator for us which is actually quite easy , it's just going to sum the last twenty closing prices and divide them by their count. Our second MA period is 50 , so the same thing ,but we have to collect 50 prices in our list to be able
to calculate 50 period MA.In this project , the bot will use two moving averages(20 and 50) and parabolic sar which helps us to see where to put our stop loss.Basically what this bot is going to do is it will wait until 20MA crosses 50MA and then
wait for correction and get in the market after the correction .

# Technology

Python 3.7

# How can we run it

First, download the source code . Go to the Windows command prompt. One option is to choose Run from the Windows Start menu, type cmd, and click OK.
Use the "cd" command to change to the folder containing the program you wish to run. Run the command line program by typing its name and pressing 'Enter'.

