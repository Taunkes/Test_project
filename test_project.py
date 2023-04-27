import requests
from bs4 import BeautifulSoup
import telebot


api = '5871606488:AAGwfme2pM4XZKgX1efJQBFNA98O0zS0yzo'
url = 'https://mangalib.me/?section=home-updates'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') #Парсинг всей страницы
new_tittles = soup.findAll('h4', 'updates__name') #Находит всё названиях глав

tittles_list = []

for data in new_tittles: # НАЗВАНИЯ
    if page.status_code == 200: #Если страница рабочая
        if data.find('a', class_='link-default') is not None: #Если название не пустая
            tittles_list.append(data.text) #Добавление в список

tittles_list = list(map(lambda x: x.strip(), tittles_list)) #Сортировка

# print(f'tittles list = {tittles_list}') #Принт в консоль для проверки полученых файлов


def searching(user_inp):
    if str(user_inp) in tittles_list:
        return 'Вышла новая глава'
    else:
        return 'Новой главы не обнаруженно'

