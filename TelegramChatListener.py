import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
PeerChannel
)
import time
from pybit_def import TradeHTTP, PositionHTTP, AccountHTTP, MarketHTTP
import random
import numpy as np

config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)
phone = config['Telegram']['phone']
username = config['Telegram']['username']
user_input_channel = config['Telegram']['tg_channel']

# Import Bybit configuration
buyLeverage = config['bybit']['buyLeverage']
sellLeverage = config['bybit']['sellLeverage']
portfolioPercentage = config['bybit']['portfolioPercentage']
seconds_trade_open = config['bybit']['seconds_to_keep_trade_open']

takeProfit_long = config['bybit']['takeProfit_long']
stopLoss_long = config['bybit']['stopLoss_long']

takeProfit_short = config['bybit']['takeProfit_short']
stopLoss_short = config['bybit']['stopLoss_short']

withTimer = config['bybit']['withTimer']

if withTimer == "True":
    withTimer_bool = True
else:
    withTimer_bool = False

# Create the client and connect
client = TelegramClient(username, api_id, api_hash)
client.start()

buy_List = []
sell_List = []

@client.on(events.NewMessage(chats=user_input_channel))
async def newMessageListener(event):
    #Get text from the message
    newMessage = event.message.message
    print(newMessage)

    # Get USDT Balance for trades
    account_http = AccountHTTP()
    payload_account = {"accountType": "CONTRACT", "symbol": "USDT"}
    getBalance = account_http.get_wallet_balance(**payload_account)
    usdt_walletBalance = getBalance['result']['list'][0]['coin'][0]['walletBalance']
    amount_per_trade = float(usdt_walletBalance)*float(portfolioPercentage)
    amount_usdt_per_trade = round(amount_per_trade, 2)

    # IF statement for a LONG / BUY trade
    if re.match(r'^#\w{2,5}\s+buy\s+setup.*$', newMessage, re.IGNORECASE | re.DOTALL):
        firstpartpair_reg = re.search('[A-Za-z]+', newMessage)
        if firstpartpair_reg:
            firstpartpair = firstpartpair_reg.group(0)
        else:
            firstpartpair = None
        #ADD the second part of the symbol
        symbol_pair = (firstpartpair+"USDT").upper()
        buy_List.append(symbol_pair)

        # # Create orderLinkId, based on a randomInt
        # y = random.randint(5, 10000000)
        # orderLinkId = symbol_pair+"_"+str(y)

        # Create an instance of TradeHTTP
        position_http = PositionHTTP() 
        trade_http = TradeHTTP()

        # Get last price of token
        market_http = MarketHTTP()
        payload_account = {"category": "linear", "symbol": symbol_pair}
        ticker_info = market_http.get_tickers(**payload_account)
        last_price_symbol = ticker_info['result']['list'][0]['lastPrice']
        qty_per_trade = round(float(amount_usdt_per_trade)/float(last_price_symbol), 4)

        take_profit_long = round(float(last_price_symbol)*float(takeProfit_long), 6)
        stop_loss_long = round(float(last_price_symbol)*float(stopLoss_long), 6)

        # Define the payload
        payload_leverage = {"category": "linear", "symbol": symbol_pair, "buyLeverage": buyLeverage, "sellLeverage": sellLeverage}
        payload_open_trade = {"category": "linear", "symbol": symbol_pair, "side": "Buy", "orderType": "Market", "qty": str(qty_per_trade),"positionIdx": 0, "takeProfit": str(take_profit_long), "stopLoss": str(stop_loss_long) }
        payload_close_trade = {"category": "linear", "symbol": symbol_pair, "side": "Sell", "orderType": "Market", "qty": str(qty_per_trade),"positionIdx": 0, "reduceOnly": True}
        # payload_get_position = {"category": "linear", "symbol": symbol_pair}
        
        # Try to change the leverage
        try:
            setLeverage = position_http.set_leverage(**payload_leverage)
            print(setLeverage)
            print("New Leverage set")
        except:
            print("Leverage already set and not changed")

        # Call the Place Order Method, based on the Payload_trade dict.
        setTrade = trade_http.place_order(**payload_open_trade)
        print(setTrade)
        # If withTimer = True, wait for the time to pass and close the trade automatically. If False, trade will stay open.
        if withTimer_bool:
            try:
                time.sleep(int(seconds_trade_open))
            finally:
                trade_http = TradeHTTP()
                setTrade = trade_http.place_order(**payload_close_trade)
                print(setTrade)
                print("Trade is closed")
        else:
            print("Trade won't be closed by timer")

    # IF statement for a SHORT / SELL trade
    if re.match(r'^#\w{2,5}\s+short\s+setup.*$', newMessage, re.IGNORECASE | re.DOTALL):
        firstpartpair_reg = re.search('[A-Za-z]+', newMessage)
        if firstpartpair_reg:
            firstpartpair = firstpartpair_reg.group(0)
        else:
            firstpartpair = None
        #ADD the second part of the symbol
        symbol_pair = (firstpartpair+"USDT").upper()
        buy_List.append(symbol_pair)

        # # Create orderLinkId, based on a randomInt
        # y = random.randint(5, 10000000)
        # orderLinkId = symbol_pair+"_"+str(y)

        # Create an instance of TradeHTTP
        position_http = PositionHTTP() 
        trade_http = TradeHTTP()

        # Get last price of token
        market_http = MarketHTTP()
        payload_account = {"category": "linear", "symbol": symbol_pair}
        ticker_info = market_http.get_tickers(**payload_account)
        last_price_symbol = ticker_info['result']['list'][0]['lastPrice']
        qty_per_trade = round(float(amount_usdt_per_trade)/float(last_price_symbol), 4)

        take_profit_short = round(float(last_price_symbol)*float(takeProfit_short), 6)
        stop_loss_short = round(float(last_price_symbol)*float(stopLoss_short), 6)

        # Define the payload
        payload_leverage = {"category": "linear", "symbol": symbol_pair, "buyLeverage": buyLeverage, "sellLeverage": sellLeverage}
        payload_open_trade = {"category": "linear", "symbol": symbol_pair, "side": "Sell", "orderType": "Market", "qty": str(qty_per_trade),"positionIdx": 0, "takeProfit": str(take_profit_short), "stopLoss": str(stop_loss_short) }
        payload_close_trade = {"category": "linear", "symbol": symbol_pair, "side": "Buy", "orderType": "Market", "qty": str(qty_per_trade),"positionIdx": 0, "reduceOnly": True}
        # payload_get_position = {"category": "linear", "symbol": symbol_pair}
        
        # Try to change the leverage
        try:
            setLeverage = position_http.set_leverage(**payload_leverage)
            print(setLeverage)
            print("New Leverage set")
        except:
            print("Leverage already set and not changed")

        # Call the Place Order Method, based on the Payload_trade dict.
        setTrade = trade_http.place_order(**payload_open_trade)
        print(setTrade)
        
        if withTimer_bool:
            try:
                time.sleep(int(seconds_trade_open))
            finally:
                trade_http = TradeHTTP()
                setTrade = trade_http.place_order(**payload_close_trade)
                print(setTrade)
                print("Trade is closed")
        else:
            print("Trade won't be closed by timer")
            
with client:
    client.run_until_disconnected()