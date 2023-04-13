import requests

# telegrambot
def emergency_bot(bot_message):
  """ It is used for sending alert to Emergeny situation"""
  
  bot_token ='5122704517:AAHbcnci6KKkBR7taNaXwEYbXYMB7lU9lbE'
  bot_chatId = '644452386'
  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatId + '&parse_mode=Markdown&text=' + bot_message
  response = requests.get(send_text)
  return response.json()  


def alert_bot(bot_message):
    """ It is used for sending price alert"""
    bot_token ='5129893039:AAHp8vD1oo3IDhI3CQCtYvWzF72mK3F8I5Q'
    bot_chatId = '644452386'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatId + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

def order_manager(bot_message):
    """ It is used for sending order manangemant"""
    bot_token ='5195435501:AAHOn3mTR2GBdrcukx4qwCycqC2G3SY2UqU'
    bot_chatId = '644452386'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatId + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

# emergency_bot('bol radha bol')