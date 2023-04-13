'''{Ex}:{Ex_UnderlyingSymbol}{YY}{M}{dd}{Strike}{Opt_Type}
	NSE:NIFTY20O0811000CE,
    NSE:BANKNIFTY20N0525000PE,
    NSE:NIFTY20D1025000CE'''
import datetime
import math











class nine_fourty():
    """ This streatagy used for 9:40 time bank nifty """
    def __init__(self,ltp=float):
        self.ltp = ltp
        self.stratagy = 'nine_fourty'

    
    def ni_atm_strikes_ce(self):
        """it will returns atm ce strike"""

        atm_price = self.ltp%50 
        val2 = math.fmod(self.ltp, 50)
        if val2 >= 25:
            val3 = 50
        else:
            val3 = 0
        x = round(self.ltp - val2 + val3)
        return {"atm_price":x}

    def ni_atm_strikes_pe(self):
        """it will returns atm pe strike"""

        atm_price = self.ltp%50 
        val2 = math.fmod(self.ltp, 50)
        if val2 >= 25:
            val3 = 50
        else:
            val3 = 0
        x = round(self.ltp - val2 + val3)
        return {"atm_price":x}

    def bn_atm_strikes_ce(self):
        """it will returns atm ce strike"""

        atm_price = self.ltp%100 
        val2 = math.fmod(self.ltp, 100)
        if val2 <= 50:
            val3 = -0
        
        elif val2 >= 50:
            val3 = 100
        x = round(self.ltp - val2 + val3)
        return {"atm_price":x,"stratagy":self.stratagy}

    def bn_atm_strikes_pe(self):
        """it will returns atm pe strike"""

        atm_price = self.ltp%100 
        val2 = math.fmod(self.ltp, 100)
        if val2 <= 50:
            val3 = -0
        
        elif val2 >= 50:
            val3 = 100
        x = round(self.ltp - val2 + val3)
        return {"atm_price":x}


        
    


    


    def save_to_db(self):
        pass


# it requres updatation
class iron_condor:
    """This is used for ironcondor stratagy on Tue"""

    def __init__(self,ce =int , pe =int,hedge_ce = int,hedge_pe=int,ltp=float):
        self.pe = pe
        self.ce = ce
        self.hedge_ce = hedge_ce
        self.hedge_pe = hedge_pe
        self.ltp = ltp 

    def order_place(self):
        """It will place order"""

        data = {
            "symbol":f"NSE:{self.symbol.upper()}-EQ",
            "qty":self.qty,
            "type":1,
            "side":1,
            'type':2,
            "productType":"BO",
            "limitPrice":0,
            "stopPrice":0,
            "validity":"DAY",
            "disclosedQty":0,
            "offlineOrder":"False",
            "stopLoss":self.stoploss,
            "takeProfit":self.takeProfit
            }
        order_status = fyers.place_order(data)
        telegram_bot(str(order_status))
        return order_status


    