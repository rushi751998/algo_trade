import mysql.connector
import datetime
# from database import db
import yfinance as yf
# data = yf.download("TATAMOTORS.NS")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="ohlc"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE Orders (order_id INT,entry_timestamp VARCHAR(50), stratagy VARCHAR(50),symbol VARCHAR(50)),strike_price INT, option_type VARCHAR(10), entry_price INT(), exit_price INT(), PRIMERY KEY(order_id")

class db:
    def __init__(self,order_id :int,entry_timestamp:datetime.date,symbol:str,stratagy:str,strike_price:int,option_type:str,entry_price:float,exit_price:int):
        self.order_id = order_id                
        self.entry_timestamp = entry_timestamp
        self.stratagy = stratagy
        self.symbol = symbol
        self.strike_price = strike_price
        self.option_type = option_type
        self.entry_price = entry_price
        self.exit_price = exit_price
        
        

    def save_db(self):
        sql = "INSERT INTO Orders (order_id ,entry_timestamp , stratagy ,symbol ,strike_price , option_type , entry_price , exit_price)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.order_id,self.entry_timestamp,self.stratagy,self.symbol,self.strike_price,
        self.option_type,self.entry_price,self.exit_price)
        mycursor.execute(sql, val)
        mydb.commit()
        print(self.order_id, "id inserted.")


    def get_details(self,order_id):
        # return f"SELECT * FROM Orders WHERE order_id ={order_id}"

        mycursor = mydb.cursor()

        sql = f"SELECT * FROM customers WHERE order_id ='{order_id}'"

        mycursor.execute(sql)

        myresult = mycursor.fetchall()
        return myresult

        

    def modification_details(self):
        pass




# data base driver
# val = db(order_id=5 ,entry_timestamp="12-04-2021",stratagy= "nine fourty",
#         symbol= "Nifty",strike_price= 18700,option_type='CE',entry_price= 100,exit_price= 200)

# data = yf.download("TATAMOTORS.NS")
# print(data["Open"][::-1])

    
    
    