
from telegram_bot import order_manager
import datetime
from login import fyers


class OrderExicuation:
    def __init__(self, symbol=str, qty=int,order_id = None,side = None,avg_price = 0,sl_percentage = None):
        self.symbol = symbol
        self.qty = qty
        self.order_id = order_id
        self.side = side
        self.avg_price = round(0.05*round(avg_price/0.05),2)
        self.sl_percentage = sl_percentage

    def order_place(self):
        """It will place order using broker terminal"""
        data = {
            "symbol": self.symbol,
            "qty": self.qty,
            "type": 2,
            "side": self.side,
            "productType": "INTRADAY",
            "limitPrice": 0,
            "stopPrice": 0,
            "validity": "DAY",
            "disclosedQty": 0,
            "offlineOrder": "False",
            "stopLoss": 0,
            "takeProfit": 0
        }
        return (fyers.place_order(data)['message'])

    def exit_position(self):
        """ it will exit position based on order id"""
        return fyers.exit_positions(data={'id':f'{self.order_id}-INTRADAY'})['message']

    def place_limit_sl(self):
        """ it will place sl order with percentage 
        input : Side ,Average Price, Stop_Percentage
        """
        if self.side ==1:
            self.side = -1
            stoploos = round(self.avg_price*((100-self.sl_percentage)/100))
            limit_price =(stoploos)-0.05 # 0.05 is the diffrance betweeen limit price and trigger price

        elif self.side ==-1:
            self.side = 1
            stoploos = round(self.avg_price*((100+self.sl_percentage)/100))
            limit_price =(stoploos)-0.05 # 0.05 is the diffrance betweeen limit price and trigger price
        else:
            pass

        data = {
            "symbol": self.symbol,
            "qty": self.qty,
            "type": 4,
            "side": self.side,
            "productType": "INTRADAY",
            "limitPrice": limit_price,# for only limt-stop it reqired
            "stopPrice": stoploos, # it shoud be grater than limit
            "validity": "DAY",
            "disclosedQty": 0,
            "offlineOrder": "False",
            "stopLoss": 0,
            "takeProfit": 0
        }

        print(self.side,stoploos,limit_price)
        return (fyers.place_order(data)['message'])


    def modify_order(self):
        """ IT will modify orders. Pass trades """
        if self.side ==1:
            self.side = -1
            stoploos = round(self.avg_price*((100-self.sl_percentage)/100))
            limit_price =(stoploos)-0.05 # 0.05 is the diffrance betweeen limit price and trigger price

        elif self.side ==-1:
            self.side = 1
            stoploos = round(self.avg_price*((100+self.sl_percentage)/100))
            limit_price =(stoploos)-0.05 # 0.05 is the diffrance betweeen limit price and trigger price
        else:
            pass

        data = {
        "id":self.order_id,   
        "type":4, 
        "limitPrice": limit_price,# for only limt-stop it reqired
        "stopPrice": stoploos, # it shoud be grater than limit
        "qty":1
        }
        return fyers.modify_order(data=data)

    def is_sl_hit(order_id):
        return order_status(order_id) =='completed'


# time.sleep(5)
# print(OrderExicuation('sbin',order_id = 'NSE:SBIN-EQ-INTRADAY').exit_position())

