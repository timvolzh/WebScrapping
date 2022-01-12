import requests
import bs4
from headers import headers

habr_url = 'https://habr.com/'
# определяем список ключевых слов
KEYWORDS = {'SQL','дизайн', 'фото', 'web', 'python','PHP','Химия','Big Data'}

# получение содержимого страницы
response = requests.get('https://habr.com/ru/all/', headers=headers)
response.raise_for_status()
response_text = response.text
soup = bs4.BeautifulSoup(response_text, 'html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')


for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = set(hub.find('span').text for hub in hubs)

    if KEYWORDS & hubs:
        date = article.find('time').text
        title = article.find('a', class_='tm-article-snippet__title-link')
        title_text = title.text
        title_url = habr_url + title['href']
        print(f'{date}\n{title_text}\n{title_url}\n')
