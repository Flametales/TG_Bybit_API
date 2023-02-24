from utils.http_manager import _V5HTTPManager
from utils.trade import Trade
from utils.position import Position
from utils.account import Account
from utils.market import Market

class TradeHTTP(_V5HTTPManager):
    def place_order(self, **kwargs):
        """
        This method supports creating orders for spot, spot margin, linear perpetual, inverse futures, and options.
        Required args:
            category (string): Product type. Unified account: spot, linear, option. Normal account: linear, inverse. Please note that category is not involved with business logic.
            symbol (string): Symbol name.
            side (string): Buy or Sell.
            orderType (string): Market or Limit.
            qty (string): Order quantity.
        Returns:
            Request results as dictionary.
        Additional information:
            https://bybit-exchange.github.io/docs/v5/order/create-order
        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Trade.PLACE_ORDER}",
            query=kwargs,
            auth=True,
        )
    
    def cancel_order(self, **kwargs):
            """Unified account covers: Spot / Linear contract / Options
            Normal account covers: USDT perpetual / Inverse perpetual / Inverse futures
            Required args:
                category (string): Product type Unified account: spot, linear, optionNormal account: linear, inverse. Please note that category is not involved with business logic
                symbol (string): Symbol name
                orderId (string): Order ID. Either orderId or orderLinkId is required
                orderLinkId (string): User customised order ID. Either orderId or orderLinkId is required
            Returns:
                Request results as dictionary.
            Additional information:
                https://bybit-exchange.github.io/docs/v5/order/cancel-order
            """
            return self._submit_request(
                method="POST",
                path=f"{self.endpoint}{Trade.CANCEL_ORDER}",
                query=kwargs,
                auth=True,
            )

class PositionHTTP(_V5HTTPManager):
    def get_positions(self, **kwargs):
        """Query real-time position data, such as position size, cumulative realizedPNL.
        Required args:
            category (string): Product type
                Unified account: linear, option
                Normal account: linear, inverse.
                Please note that category is not involved with business logic
        Returns:
            Request results as dictionary.
        Additional information:
            https://bybit-exchange.github.io/docs/v5/position
        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Position.GET_POSITION_INFO}",
            query=kwargs,
            auth=True,
        )
    
    def set_leverage(self, **kwargs):
        """
        Set the leverage
        Required args:
            category (string): Product type
                Unified account: linear
                Normal account: linear, inverse.
                Please note that category is not involved with business logic
            symbol (string): Symbol name
            buyLeverage (string): [0, max leverage of corresponding risk limit].
                Note: Under one-way mode, buyLeverage must be the same as sellLeverage
            sellLeverage (string): [0, max leverage of corresponding risk limit].
                Note: Under one-way mode, buyLeverage must be the same as sellLeverage
        Returns:
            Request results as dictionary.
        Additional information:
            https://bybit-exchange.github.io/docs/v5/position/leverage
        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Position.SET_LEVERAGE}",
            query=kwargs,
            auth=True,
        )
    
    def set_tp_sl_mode(self, **kwargs):
        """Set TP/SL mode to Full or Partial
        Required args:
            category (string): Product type
                Unified account: linear
                Normal account: linear, inverse.
                Please note that category is not involved with business logic
            symbol (string): Symbol name
            tpSlMode (string): TP/SL mode. Full,Partial
        Returns:
            Request results as dictionary.
        Additional information:
            https://bybit-exchange.github.io/docs/v5/position/tpsl-mode
        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Position.SET_TP_SL_MODE}",
            query=kwargs,
            auth=True,
        )
    
    def set_trading_stop(self, **kwargs):
        """Set the take profit, stop loss or trailing stop for the position.
        Required args:
            category (string): Product type
                Unified account: linear
                Normal account: linear, inverse.
                Please note that category is not involved with business logic
            symbol (string): Symbol name
        Returns:
            Request results as dictionary.
        Additional information:
            https://bybit-exchange.github.io/docs/v5/position/trading-stop
        """
        return self._submit_request(
            method="POST",
            path=f"{self.endpoint}{Position.SET_TRADING_STOP}",
            query=kwargs,
            auth=True,
        )
    
class AccountHTTP(_V5HTTPManager):
    def get_wallet_balance(self, **kwargs):
        """Obtain wallet balance, query asset information of each currency, and account risk rate information under unified margin mode.
        By default, currency information with assets or liabilities of 0 is not returned.
        Required args:
            accountType (string): Account type
                Unified account: UNIFIED
                Normal account: CONTRACT
        Returns:
            Request results as dictionary.
        Additional information:
            https://bybit-exchange.github.io/docs/v5/account/wallet-balance
        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Account.GET_WALLET_BALANCE}",
            query=kwargs,
            auth=True,
        )

class MarketHTTP(_V5HTTPManager):
    def get_tickers(self, **kwargs):
        """Query the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.
        Required args:
            category (string): Product type. spot,linear,inverse,option
        Returns:
            Request results as dictionary.
        Additional information:
            https://bybit-exchange.github.io/docs/v5/market/tickers
        """
        return self._submit_request(
            method="GET",
            path=f"{self.endpoint}{Market.GET_TICKERS}",
            query=kwargs,
        )

# market_http = MarketHTTP()
# payload_account = {"category": "linear", "symbol": "BTCUSDT"}
# last_price = market_http.get_tickers(**payload_account)
# last_price = last_price['result']['list'][0]['lastPrice']
# print(last_price)




# account_http = AccountHTTP()
# payload_account = {"accountType": "CONTRACT", "symbol": "USDT"}
# getBalance = account_http.get_wallet_balance(**payload_account)
# usdt_walletBalance = getBalance['result']['list'][0]['coin'][0]['walletBalance']
# print(usdt_walletBalance)

# symbol_pair = "BTCUSDT"
# orderLinkId = "Test_0001"
# position_http = PositionHTTP() 
# trade_http = TradeHTTP()

# # payload_leverage = {"category": "linear", "symbol": symbol_pair, "buyLeverage": "10", "sellLeverage": "10"}
# # payload_open_trade = {"category": "linear", "symbol": symbol_pair, "side": "Buy", "orderType": "Limit", "qty": "0.01", "price": "1000","positionIdx": 1, "orderLinkId": orderLinkId}
# payload_get_position = {"category": "linear", "symbol": symbol_pair}

# # # Try to change the leverage
# # try:
# #     setLeverage = position_http.set_leverage(**payload_leverage)
# #     print(setLeverage)
# #     print("New Leverage set")
# # except:
# #     print("Leverage already set and not changed")

# # # Call the Place Order Method, based on the Payload_trade dict.
# # setTrade = trade_http.place_order(**payload_open_trade)
# # print(setTrade)

# import numpy as np

# getPosition = position_http.get_positions(**payload_get_position)
# print(getPosition)
# marketPrice = float(getPosition['result']['list'][0]['markPrice'])
# print(marketPrice*1000.00)
