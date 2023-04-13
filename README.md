# exicuation proces
- Time ==9:20
- get atm 
- get qty =25
- get side =-1
- get nearest expiry 
- Put sl according to day's for expiry
- put order type ==2('market order')
- make symbol 
> ('NSE:BANKNIFTY{Expiry}{ATM strike}{CE|PE}')

- append symboles to nine_twenty list
> nine_twenty  = [{'NSE:BANKNIFTY{Expiry}{ATM strike}{CE}'}  ,  {'NSE:BANKNIFTY{Expiry}{ATM strike}{PE}'}]

- execute both leg using basket order
> data = fyers.place_basket_orders(nine_twenty)

- Put sl on legs on atm legs

make df for atm runing trades



# task pending
- modify order
- trailing sl

for trailing keep tracking pending order

## follow link for algo execuation
https://www.youtube.com/watch?v=tfICrwc9WiM&list=PLBxEQPBjwdGhyowU_mki3XUopSY5dqmKn&index=22

Store trades in mongoDB with add parameter sl_hit