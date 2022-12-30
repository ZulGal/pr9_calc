import telebot
import func


token = '5928963539:AAEdBTpMcckQg_l1ZtGi-Ju2VTDq5lTlkU0'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, '/help\n/calc\n/')

@bot.message_handler(commands=['calc'])
def help_message(message):
    bot.send_message(message.chat.id, 'Введите арифметическое выражение:')    

@bot.message_handler(content_types=['text'])
def repeat_all_message(message):
    
    s = message.text
    result = func.calc_(s)

    bot.send_message(message.chat.id,result) 

bot.polling()  
