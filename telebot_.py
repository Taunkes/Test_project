import telebot
'''Creating the bot'''

api = '5871606488:AAGwfme2pM4XZKgX1efJQBFNA98O0zS0yzo'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['/start', 'Привет'])
def hello(message):
    bot.send_message(message.chat.id, 'Привет! Используй одну из команд:')

@bot.message_handler(content_types=['text'])
def words(message):
    if message == '/command1':
        bot.send_message(message.chat.id, 'Введите название(not работает)')
    elif message == '/command2':
        bot.send_message(message.chat.id, 'Пока не работает')
    else:
        'Пока что бот не распознаёт слова'

bot.polling(none_stop=True)