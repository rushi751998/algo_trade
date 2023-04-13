
# pip freeze >> requiremants.txt   # To creat requremants.txt
#  pip install -r .\requirements.txt  # To install all packages

import time
import datetime
import threading
import re

from time_manager import c_time
# from data import *
from telegram_bot import *
from ticker_data import live_data
from exicuation import OrderExicuation
from login import fyers
from broker import *

c_time()

day_start = (9, 18, 00)
day_end = (20, 29, 59)

# thread1 = threading.Thread(target=DataUpdate.update_positions)     #position update thread
# thread2 = threading.Thread(target=DataUpdate.update_orderbook)     #Orderbook update thread
# thread3 = threading.Thread(target=sheet_data)                      #geting sheet variables thread
# thread1.start()
# thread2.start()
# thread3.start()

instrument = 'itc'
sl_percentage = 0.4


# print(live_data('niftybank').index_ltp())
# print(live_data('niftybank').atm_strike())


# a = OrderExicuation(symbol = 'NSE:ITC-EQ',qty = 1 ,side = 1,avg_price =529.57,sl_percentage = sl_percentage ).place_limit_sl()
# print(a)
# print(OrderExicuation( symbol= f"NSE:{instrument.upper()}-EQ",qty = 1,side = 1).order_place())
# print(OrderExicuation( symbol= f"NSE:{instrument.upper()}-EQ",qty = 1).place_sl())


# while True:


#     if c_time() <= day_end:
#         ltp = live_data(symbol = instrument).index_ltp()
#         print(ltp)
#         time.sleep(1)

    
nine_twenty = ['NSE:NIFTY2342017600CE','NSE:NIFTY2342018300CE']
# eleven_ten = ['NSE:NIFTY2342018000CE','NSE:NIFTY2342016000PE']

def tril_sl(ls_trades):
    """It will  trail sl of other leg if one leg sl hit """
    open_position = Positions.open_position_details()
    # print(open_position)
    active_trades_ls = (open_position['id'].apply(lambda x:x.split('-')[0]).values)
    print(active_trades_ls,"\n")

    for i in ls_trades :
        if i not in  active_trades_ls:
            ls_trades = ls_trades.remove(i)
            print(ls_trades)
            # open_trade_df= open_position[open_position['id'] ==f'{ls_trades[0]}-MARGIN'] # it will give you open trade dataframe 
            # entry_price = open_trade_df['sellAvg'].values[0] # it will give you entry price of open trades
            # print(open_trade_df) 
        
# tril_sl(nine_twenty)
# tril_sl(eleven_ten)
# print(fyers.orderbook()['orderBook'])
# print(pd.DataFrame(fyers.orderbook()['orderBook']).columns)

print(Orderbook.all_orders(),"\n\n")
print(Orderbook.pending_orders())