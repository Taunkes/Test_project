import requests
from bs4 import BeautifulSoup


url = 'https://mangalib.me/?section=home-updates'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') #Парсинг всей страницы
new_tittles = soup.findAll('h4', 'updates__name') #Находит всё названиях глав

tittles_list = []

for data in new_tittles: # НАЗВАНИЯ
    if page.status_code == 200: #Если страница рабочая
        if data.find('a', class_='link-default') is not None: #Если название не пустая
            tittles_list.append(data.text) #Добавление в список

tittles_list = list(map(lambda x: x.strip(), tittles_list)).replace('[', '').replace #Сортировка

print(f'tittles list = {tittles_list}') #Принт в консоль для проверки полученых файлов
