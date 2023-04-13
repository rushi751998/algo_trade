from login import fyers 
# from data import Order_management
import pandas as pd
import datetime



class broker:

    def fund():
        return print(pd.DataFrame(fyers.funds()['fund_limit']))

        # return fyers.funds()

    def market_status():
        return fyers.market_status()["marketStatus"][3]['status']
    
    
index = 0

class Positions : 

    def no_of_position():
        return len(fyers.positions())

    def all_position_details():
        """ It will give you all position details"""     
        return (pd.DataFrame(fyers.positions()['netPositions'])[['id','segment','netQty','side','ltp','buyAvg','sellAvg','pl']])
        # return (pd.DataFrame(fyers.positions()['netPositions']).columns) # don't delet it is uded for debuging

    def open_position_details(): 
        """ It will give you all open position details"""   
        all_positions = Positions.all_position_details() 
        return (all_positions[all_positions['side']!=0]) 


class Orderbook:
    # (['clientId', 'id', 'exchOrdId', 'qty', 'remainingQuantity', 'filledQty',
    #    'discloseQty', 'limitPrice', 'stopPrice', 'tradedPrice', 'type',
    #    'fyToken', 'exchange', 'segment', 'symbol', 'instrument', 'message',
    #    'offlineOrder', 'orderDateTime', 'orderValidity', 'pan', 'productType',
    #    'side', 'status', 'source', 'ex_sym', 'description', 'ch', 'chp', 'lp',
    #    'slNo', 'dqQtyRem', 'orderNumStatus', 'disclosedQty'],
    #   dtype='object') 
    def all_orders():
        all_orders = pd.DataFrame(data = fyers.orderbook()['orderBook'])[['orderDateTime','id','symbol','message','status','tradedPrice','remainingQuantity','limitPrice','stopPrice']]
        all_orders['orderDateTime'] = pd.to_datetime(all_orders['orderDateTime'])
        return all_orders.info()

    def Filled_orders():
        """It will give you Filled orders"""
        all_orders = Orderbook.all_orders()
        Filled_orders = all_orders[all_orders['status'] ==2]
        return Filled_orders

    def pending_orders():
        """It will give you Pending orders"""
        all_orders = Orderbook.all_orders()
        pending_order = all_orders[all_orders['status'] ==6]
        return pending_order

    
    def canceled_orders():
        """It will give you Canceled orders"""
        all_orders = Orderbook.all_orders()
        canceled_orders = all_orders[all_orders['status'] ==1]
        return canceled_orders

    def rejected_orders():
        """It will give you Rejected orders"""
        all_orders = Orderbook.all_orders()
        pending_order = all_orders[all_orders['status'] ==5]
        return pending_order



# orderId = "8102210246491"
# data = {"id":orderId}

# response = fyers.orderbook(data=data)
         
         



