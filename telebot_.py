import telebot
from test_project import tittles_list


'''Creating the bot'''

api = '5871606488:AAG9Q014OrB75p_31zkFR3jWlErAHv28s7I'
bot = telebot.TeleBot(api)

@bot.message_handler(content_types='text')
def message_reply(message):
    
    if message.text == '/link':
        bot.send_message(message.chat.id, 'https://mangalib.me/?section=home-updates')
    
    elif message.text == '/list':
       for x in range(0, len(tittles_list), 4096):
            bot.send_message(message.chat.id, tittles_list[x:x+4096])
    
    elif message.text == '/l':
        bot.send_animation(message.chat.id, 'https://media.tenor.com/-IO8NDvwkDAAAAAC/walter-l-walter-white.gif')
    
    elif message.text in ['Привет', '/start', 'Hi', 'Хай']:
        bot.send_message(message.chat.id, 'Привет! Используй одну из команд:')

bot.infinity_polling()
