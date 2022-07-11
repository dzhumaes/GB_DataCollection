import requests
from lxml import html

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
url = 'https://yandex.ru/news/'
session = requests.Session()
response = session.get(url, headers = headers)

dom = html.fromstring(response.text)
items = dom.xpath("//div[contains(@class, 'mg-card_flexible')]")

news_list = []
for item in items:
    news = {}
    name = item.xpath(".//h2[contains(@class, 'mg-card__title')]//text()")
    link = item.xpath(".//h2[contains(@class, 'mg-card__title')]//@href")
    source = item.xpath(".//span[contains(@class, 'source')]//text()")
    publication_date = item.xpath(".//span[contains(@class,'time')]//text()")

    # name = name.getText('name').replace(u'\xa0', u' ')

    news['name'] = name
    news['link'] = link
    news['source'] = source
    news['publication_date'] = publication_date

    news_list.append(news)