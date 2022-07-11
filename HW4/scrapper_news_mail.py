import requests
from pprint import pprint
from lxml import html

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
url = 'https://news.mail.ru/?_ga=2.77474517.116093320.1657515974-618168803.1623823529'
session = requests.Session()
response = session.get(url, headers = headers)

dom = html.fromstring(response.text)
items = dom.xpath(".//td[contains(@class, daynews)]|.//div[@class = 'cols__wrapper']|.//ul[contains(@class, 'list_type')]")

news_list = []
for item in items:
    news = {}
    name = item.xpath(".//a[contains(@class, 'js-topnews__item')]//text()|.//a[contains(@class, 'newsitem__title')]//text()|.//li[@class = 'list__item']//text()")
    link = item.xpath(".//a[contains(@class, 'js-topnews__item')]//@href|.//a[contains(@class, 'newsitem__title')]//@href|.//li[@class = 'list__item']//@href")

    news = {f"'name': {name}, 'link': {link} "}

    news_list.append(news)

pprint(news_list)
pprint(len(news_list))



# .//span[contains(@class,'breadcrumbs__item')]//span[@class='link__text']//text()
# .//span[@datetime]/@datetime

print()
# .//td[contains(@class, daynews)]//a[contains(@class, 'js-topnews__item')]/@href
# .//a[contains(@class, 'js-topnews__item')]/@href
#
# .//div[@class = 'cols__wrapper']//a[contains(@class, 'newsitem__title')]/@href
# .//a[contains(@class, 'newsitem__title')]/@href
#
# .//ul[contains(@class, 'list_type')]//li[@class = 'list__item']//@href
# .//li[@class = 'list__item']//@href