from fyers_api.Websocket import ws
from login import login,fyers


class live_data:
    """It will give live data by giving Symbol"""
    def __init__(self,symbol,year = None,month = None,day = None):
       
        self.symbol = symbol
        self.day = day
        self.month = month
        self.year = year

    def equity_ltp(self):
        """ it wil give you Stock LTP data
            dtype : int
        """
        data = {"symbols":f"NSE:{self.symbol.upper()}-EQ"}
        return(fyers.quotes(data)["d"][0]['v']['lp'])

    def index_ltp(self):
        """ it wil give you index LTP data
            dtype : int
        """
        data = {"symbols":f"NSE:{self.symbol.upper()}-INDEX"}
        # return(fyers.quotes(data)["d"][0]['v']['lp'])
        return(fyers.quotes(data)["d"][0]['v']['lp'])

    def future_ltp(self):
        """ it wil give you Future LTP data
            dtype : int
        """
        data = {"symbols":f"NSE:{self.symbol.upper()}{self.year}{self.month.upper()}FUT"}
        return(fyers.quotes(data)['d'][0]['v']['lp'])

    def mcx_ltp(self):
        """ it wil give you MCX LTP data
            dtype : int
        """
        data = {"symbols":f"MCX:{self.symbol.upper()}{self.year}{self.month.upper()}FUT"}
        return(fyers.quotes(data)['d'][0]['v']['lp'])

    def atm_strike(self):
        """ it wil give you ATM strike Price
            dtype : int
        """
        atm_data = self.index_ltp()
        base = 100
        atm = base*round(atm_data/base)
        
        return atm



#  (This is the custom message function which we need to have in order to receive the Symbol/order update and accordingly you can manipulate the data you receive through this function  )

"""


def custom_message(msg):
    print(f"Custom:{msg}")


ws.websocket_data = custom_message
feed_token = client_id+":"+login()

fyersSocket = ws.FyersSocket(
    access_token=feed_token, run_background=False, log_path="logpath")
fyersSocket.subscribe(symbol=symbol, data_type="symbolData")
"""
#  If run_background Process is set to True. Then while running the orderUpdate over  the logs you can also be able to call the other calls too in the following manner

# print(fyers.get_profile())
# print(fyers.tradebook()['tradeBook'][0]['orderNumber'])
# print(fyers.tradebook()['tradeBook'][1]['orderNumber'])


# print(fyers.positions()['netPositions'][0])


# {This is used in order to keep your Websocket Thread Open and also do the remaining functionality as expected or other method calls}
# fyersSocket.keep_running()
