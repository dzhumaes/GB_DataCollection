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

    def mailParse(self) -> list:
        self.storage.extend(self.mailParse_news())

    def mailParse_news(self) -> list:
        news_list = []

        session = requests.Session()
        response = session.get(self.url, headers = self.headers)

        dom = html.fromstring(response.text)
        items = dom.xpath(".//div[@data-logger-parent='content']")
        for item in items:
            main_info = item.xpath(".//ul[contains(@class, 'list_type')]//a[contains(@class, 'link_flex')]|.//ul[contains(@class, 'list_type')]//li[@class = 'list__item']|.//a[contains(@class, 'js-topnews__item')]")
            for element in main_info:
                news = {
                    'name': str(element.xpath(".//text()")[0]),
                    'link': str(element.xpath(".//@href")[0])
                }
                news = self._extend(news)
                news_list.append(news)
        return news_list

    def _extend(self, news: dict) -> dict:
        response = requests.get(news['link'], headers=self.headers)
        dom = html.fromstring(response.text)
        news['source'] = dom.xpath(".//span[contains(@class,'breadcrumbs__item')]//span[@class='link__text']//text()")
        news['publication_date'] = dom.xpath(".//span[@datetime]/@datetime")
        return news

if __name__ == '__main__':
    parser = MailRuScrapper()
    news_result = parser.mailParse_news()
    pprint(news_result)
    pprint(len(news_result))

# //div[@data-logger-parent='content']

# //ul[contains(@class, 'list_type')]//a[contains(@class, 'link_flex')]
# //ul[contains(@class, 'list_type')]//li[@class = 'list__item']
# //a[contains(@class, 'js-topnews__item')]