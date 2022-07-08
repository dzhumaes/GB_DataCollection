import requests
from bs4 import BeautifulSoup
from pprint import pprint

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
url = 'https://gb.ru'
params = {'page': '1'}

session = requests.Session()
response = session.get(url+'/posts', headers = headers, params=params)

dom = BeautifulSoup(response.text, 'html.parser')
articles = dom.find_all('div', {'class': 'post-item'})
last_page = dom.find('li', {'class': 'page'}).previous_sibling.text
articles_list = []

for i in range(1, int(last_page)+1):
    print(f'Please wait. In progress... scrapping page {i}')
    params ['page'] = i
    response = session.get(url + '/posts', headers=headers, params=params)
    dom = BeautifulSoup(response.text, 'html.parser')
    articles = dom.find_all('div', {'class': 'post-item'})
    for article in articles:
        article_data = {}
        name = article.find('a', {'class': 'post-item__title'})
        href = url + name.get('href')
        name = name.text
        date = article.find('div', {'class': 'small m-t-xs'}).text

        data = article.find_all('div', {'class': 'post-counter'})
        views = int(data [0].findChildren(recursive=False)[1].text)
        comments = int(data[1].findChildren(recursive=False)[1].text)

        # counters = article.find_all('span')
        # views = counters[1].text
        # comments = counters[2].text

        article_data['name'] = name
        article_data['href'] = href
        article_data['date'] = date
        article_data['views'] = views
        article_data['comments'] = comments

        articles_list.append(article_data)

pprint(articles_list)
print(len(articles_list))