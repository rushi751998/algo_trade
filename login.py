from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fyers_api import fyersModel
from fyers_api import accessToken
import time
import datetime

# Suvarna More
client_id = 'E6SDMQLCWS-100'
secret_url = 'Y4FQNG2DMM'
redirect_uri = 'http://127.0.0.1:5000'

date = datetime.datetime.today().date()

uri = "mongodb+srv://rushi7519998:admin@cluster0.7ytpulb.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
database = client['trading_logins']
collection = database['access_tocken']

a =collection.find()
def login():
    if  str(date) not in a:
        """this function acivate auth code and login"""
        session = accessToken.SessionModel(client_id=client_id, secret_key=secret_url,
                                            redirect_uri=redirect_uri, response_type='code', grant_type='authorization_code')
        response = session.generate_authcode()
        print(response)
        session.set_token(input("Enter Auth Code :- "))
        access_token = session.generate_token()['access_token']
        # data= {str(date): {'access_token':access_token}}
        data= {'date': {str(date):{'access_token':access_token}}}
        collection.insert_one(data)
        
    else:
        access_token = (a[str(date)]['access_token'])
        
    return access_token
            
# collection.delete_many()
# data= {'date': {'11-1-2005':{'access_token':"nkb jgbf65846775rv"}}}
# collection.insert_one(data)
# a = collection.find()
# print(list(a)[0]['date']=='1234')
# for i in a:
#     # if (i['date'])=='11-1-2005':
#     print(i.keys())
# collection.delete_many()

# print(dir(a[0]['date']))
# print((a[0]['date']).keys())
 
print(database.collection.find({'date':{'$eq':'11-1-2005'}}))


# fyers = fyersModel.FyersModel(client_id=client_id, token=login(), log_path="")





















# from fyers_api import fyersModel
# from fyers_api import accessToken
# import time
# import os

# import datetime

# # # Rushikesh More Account


# # client_id = 'KTCMGLWOAD-100'
# # secret_url = 'XJZ69CL3FP'
# # redirect_uri = 'http://127.0.0.1:5000'


# # Suvarna More
# client_id = 'E6SDMQLCWS-100'
# secret_url = 'Y4FQNG2DMM'
# redirect_uri = 'http://127.0.0.1:5000'


# date = datetime.datetime.today().date()

# def login():
#     """this function acivate auth code and login"""

#     if not os.path.exists(f'key/{date}'):
#         session = accessToken.SessionModel(client_id=client_id, secret_key=secret_url,
#                                            redirect_uri=redirect_uri, response_type='code', grant_type='authorization_code')
#         response = session.generate_authcode()
#         print(response)
#         session.set_token(input("Enter Auth Code :- "))
#         access_token = session.generate_token()['access_token']
#         print("**************************\n\n                  Login Sucesfully With token \n\n                           **************************")
#         with open(f'key/{date}', 'w') as f:
#             f.write(access_token)

#     else:
#         with open(f'key/{date}', 'r') as f:                   
#             access_token = f.read()
#             print("**************************\n\n                  Login Sucesfully\n\n                           **************************")
            

#     return access_token



# fyers = fyersModel.FyersModel(client_id=client_id, token=login(), log_path="")

