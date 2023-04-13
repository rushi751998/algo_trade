import datetime
from pytz import timezone
import time



def c_time():
    """ It will give time accorring to india zone in Hour , Minute, Second
    HOUR : int    
    MINUTE : int    
    SECONDS : int    
    
    """
    HOUR        = datetime.datetime.now(timezone("Asia/Kolkata")).hour
    MINUTE      = datetime.datetime.now(timezone("Asia/Kolkata")).minute
    SECONDS     = datetime.datetime.now(timezone("Asia/Kolkata")).second
    return HOUR,MINUTE,SECONDS
    # print(SECONDS)

def sleep_timer(seconds):
    time.sleep(seconds)
    





# import threading                                                                                                                                        
# class aa:    
#     def t1():
#         while True:
            
#             print("Thread---1     ",c_time())
#             time.sleep(10)
        
#     def t2():
#         while True:
            
#             print("Thread-----2     ",c_time())
#             time.sleep(2)

    

# t1 = threading.Thread(target=aa.t1)
# t2 = threading.Thread(target=aa.t2)


# t1.start()
# t2.start()

