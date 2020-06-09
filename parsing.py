from bs4 import BeautifulSoup
import urllib.request
import time
from termcolor import colored
from urllib.request import urlopen, Request

req = urllib.request.urlopen('https://www.ua-football.com/sport')
html = req.read()
print(html)

soup = BeautifulSoup(html, 'html.parser')


news = soup.find_all('li', class_ = 'liga-news-item')


results = []

for item in news:
    title = item.find('span', class_ = 'd-block').get_text(strip = True)
    print(colored(title, 'green'))
    desc = item.find('span', class_='name-dop').get_text(strip = True)
    print(colored(desc, 'red'))
    href = item.a.get('href')
    print(colored(href, 'blue'))
    results.append({
    'title': title,
    'desc': desc,
    'href': href,
    })


fout = open('parsingsites.txt', 'w', encoding='utf-8')

i = 1
for item in results:
    fout.write(f'Новость номер: {i}\n\nНазвание: {item["title"]}\
                                        \nОписание: {item["desc"]}\
                                        \nСсылка: {item["href"]}\n\n\n')
    i += 1
fout.close()
