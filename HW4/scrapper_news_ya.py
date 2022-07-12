import requests
from pprint import pprint
from lxml import html

class YandexRuScrapper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'
        }
        self.url = 'https://yandex.ru/news/'
        self.storage = list()
        self.YaParse_news()

    def YaParse(self):
        self.storage.extend(self.YaParse_news())

    def YaParse_news(self):
        news_list = []

        session = requests.Session()
        response = session.get(self.url, headers=self.headers)

        dom = html.fromstring(response.text)
        items = dom.xpath("//div[contains(@class, 'mg-card_flexible')]")
        for item in items:
            news = {}
            name = item.xpath(".//h2[contains(@class, 'mg-card__title')]//text()")
            link = item.xpath(".//h2[contains(@class, 'mg-card__title')]//@href")
            source = item.xpath(".//span[contains(@class, 'source')]//text()")
            publication_date = item.xpath(".//span[contains(@class,'time')]//text()")

            news['name'] = name
            news['link'] = link
            news['source'] = source
            news['publication_date'] = publication_date

            news_list.append(news)

        return news_list

if __name__ == '__main__':
    parser = YandexRuScrapper()
    news_result = parser.YaParse_news()
    pprint(news_result)
    pprint(len(news_result))