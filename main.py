import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Java']
KEYWORDS = set(KEYWORDS)

responce = requests.get('https://habr.com/ru/all/')

text = responce.text
soup = BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    a = article.text.strip().split()
    a = set(a)
    if a & KEYWORDS:
        result_data = article.find('span', class_='post__time').text  # Ищем дату интересующей статьи
        result_tittle = article.find('a', class_='post__title_link').text  # Ищем заголовок интересующей статьи
        result_link = article.find('a', class_='post__title_link').attrs.get('href')  # Ищем ссылку интересующей статьи
        print(f'{result_data} - {result_tittle} - {result_link}')
