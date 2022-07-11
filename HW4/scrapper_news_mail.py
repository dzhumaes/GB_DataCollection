import requests
from pprint import pprint
from lxml import html

class MailRuScrapper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'
            }
        self.url = 'https://news.mail.ru/?_ga=2.77474517.116093320.1657515974-618168803.1623823529'
        self.storage = list()
        self.mailParse_news()
        # self.attributes = (".//a[contains(@class, 'js-topnews__item')]",
        #                    ".//a[contains(@class, 'newsitem__title')]",
        #                    ".//li[@class = 'list__item']")

    def mailParse_news(self):
        self.storage.extend(self.mailParse_topnews())
        self.storage.extend(self.mailParse_newsitem())
        self.storage.extend(self.mailParse_newslist())

    def mailParse_topnews(self) -> list:
        topnews_list = []
        session = requests.Session()
        response = session.get(self.url, headers = self.headers)

        dom = html.fromstring(response.text)
        items = dom.xpath(".//td[contains(@class, 'daynews')]")
        for item in items:
            topnews_list.append(self.parse_news(item))
        return topnews_list

    def mailParse_newsitem(self) -> list:
        newsitem_list = []
        session = requests.Session()
        response = session.get(self.url, headers=self.headers)

        dom = html.fromstring(response.text)
        items = dom.xpath(".//div[@class = 'cols__wrapper']")
        for item in items:
            newsitem_list.append(self.parse_news(item))
        return newsitem_list

    def mailParse_newslist(self) -> list:
        newslist_list = []
        session = requests.Session()
        response = session.get(self.url, headers=self.headers)

        dom = html.fromstring(response.text)
        items = dom.xpath(".//ul[contains(@class, 'list_type')]")
        for item in items:
            newslist_list.append(self.parse_news(item))
        return newslist_list

    def parse_news(self, item) -> list:
        topnews_data = []

        # for element in self.attributes:
        #     main_info = item.xpath(f"{element}")
        #     for element in main_info:
        #         news = {
        #             'name': element.xpath(".//text()"),
        #             'link': element.xpath(".//@href")
        #             }
        #         news = self._extend(news)
        #         topnews_data.append(news)
        # return topnews_data

        # main_info = item.xpath[".//a[contains(@class, 'js-topnews__item')] | .//a[contains(@class, 'newsitem__title')] | .//li[@class = 'list__item']"]

        main_info = item.xpath[".//a[contains(@class, 'js-topnews__item')]"]

        for element in main_info:
            news = {
                'name': str(element.xpath(".//text()")[0]),
                'link': str(element.xpath(".//@href")[0])
                }
            news = self._extend(news)
            topnews_data.append(news)
        return topnews_data

    def _extend(self, news: dict) -> dict:
        response = requests.get(news['url'], headers=self.headers)
        dom = html.fromstring(response.text)
        news['source'] = dom.xpath("//span[contains(@class,'breadcrumbs__item')]//span[@class='link__text']//text()")
        news['publication_date'] = dom.xpath(".//span[@datetime]/@datetime")
        return news

if __name__ == '__main__':
    parser = MailRuScrapper()
    news_result = parser.mailParse_news()
    pprint(news_result)