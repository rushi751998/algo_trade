"""Error handling in order book if no order in order book it gives error 
        : None of [Index(['orderDateTime', 'id', 'side', 'segment', 'type', 'message', 'symbol',\n       'tradedPrice"""

import time
import gspread
import pandas as pd
import json
from time_manager import c_time

from login import fyers

gc = gspread.service_account(filename='sheet_auth.json')

positions =gc.open('Algo Dashboard').worksheet("positions")
orders =gc.open('Algo Dashboard').worksheet("orders")
log =gc.open('Algo Dashboard').worksheet("log")
alerts =gc.open('Algo Dashboard').worksheet("alerts")


def sheet_data():
    """It will give continue sheet data data"""
    while True:
    
        global switch_status,nf_sl,bnf_sl,position_sleep,orderbook_sleep
        nf_sl=float(positions.get("B3")[0][0])

        bnf_sl=float(positions.get("C3")[0][0])
        
        switch_status=positions.get("G1")[0][0]
        position_sleep=float(positions.get("G2")[0][0])
        orderbook_sleep=float(positions.get("G3")[0][0])
        print("Sheet data pull Sucessfuly ...",c_time())
        time.sleep(3)




class DataUpdate:
    """It will update positions and Orderbook"""

    def update_positions():
        
        """ It will continue update Positions to SpreadSheet"""
        while True:

            df_position = pd.DataFrame(fyers.positions()['netPositions'])
            df_positions = (df_position[['symbol','segment','qty','side','ltp','pl']])
            positions.update('A5',[df_positions.columns.values.tolist()] + df_positions.values.tolist())
            print("Positions updated Sucessfully.....!!!", c_time())
            time.sleep(10)
                


    def update_orderbook():
        """ It will continue update orderbook to SpreadSheet"""
        while True:
          
            df_orderbook = pd.DataFrame(fyers.orderbook()['orderBook'])
            df_orderbook = (df_orderbook[['orderDateTime','id','side','segment','type','message','symbol','tradedPrice']])
            orders.update("B3",[df_orderbook.columns.values.tolist()] + df_orderbook.values.tolist())
            print("Order updated Sucessfully",c_time())
                
            time.sleep(15)    

            
            
  
class Order_management :
    """ It will give list of positions under the plan"""
    
    def __init__(self,plan_no):
        self.plan_no=plan_no
    
    def check_plan():
        """ Select data From Spread sheet"""
        return positions.get('A6:H30')
    

    
    def get_symbol_list(self):
        """ It will give you list of symbols according to plan
        dtype : list
        """
        df = (pd.DataFrame(Order_management.check_plan()))
        df[[1,2,3,4,5,6]] = df[[1,2,3,4,5,6]].apply(pd.to_numeric)
        
        return (df[df[6]==self.plan_no][0])
    

# switch_status=positions.get("H1")[0][0]
# print(type(switch_status))