from bs4 import BeautifulSoup
import urllib.request
import time
from termcolor import colored
from urllib.request import urlopen, Request

headers = {'User-Agent': 'Safari/537.3'}
reg_url = 'https://bitexpert.io'
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()


soup = BeautifulSoup(html, 'html.parser')


news = soup.find_all('div', class_ = 'post__wrap')



results = []

for item in news:
    title = item.find('a', text = True).get_text(strip = True)
    print(colored(title, 'green'))
    date = item.find('span', class_='post__date').get_text(strip = True)
    print(colored(date, 'red'))
    href = item.a.get('href')
    print(colored(href, 'blue'))
    views = item.find('span', class_='post__views').get_text(strip = True)
    print(colored(views, 'magenta'))
    author = item.find('span', class_='post__author').get_text(strip = True)
    print(colored(author, 'yellow'))
    results.append({
    'title': title,
    'date': date,
    'href': href,
    'views': views,
    'author': author
    })


fout = open('parsingsites.txt', 'w', encoding='utf-8')

i = 1
for item in results:
    fout.write(f'Номер новости: {i}\n\nНазвание: {item["title"]}\
                                        \nДата: {item["date"]}\
                                        \nПросмотры: {item["views"]}\
                                        \nАвтор: {item["author"]}\
                                        \nСсылка: {item["href"]}\n\n\n')
    i += 1
fout.close()
