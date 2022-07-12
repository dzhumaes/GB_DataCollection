# Урок 4. Система управления базами данных MongoDB в Python
# Написать приложение, которое собирает основные новости с сайта на выбор news.mail.ru, lenta.ru, yandex-новости.
# Для парсинга использовать XPath.
# Структура данных должна содержать:
#       название источника;
#       наименование новости;
#       ссылку на новость;
#       дата публикации.
# Сложить собранные новости в БД
# Минимум один сайт, максимум - все три

import sys
from pymongo import MongoClient
from pprint import pprint
from scrapper_news_mail import MailRuScrapper
from scrapper_news_ya import YandexRuScrapper

def show_news(collection):
    result = collection.find({})
    for item in result:
        pprint(item)

def save_records(new_resault, collection):
    collection.insert_many(new_resault)

def main():
    client = MongoClient('127.0.0.1', 27017)
    db = client['news']
    mail_news = db.mail_news

    new_result = MailRuScrapper().mailParse_news()
    new_result += YandexRuScrapper().YaParse_news()

    save_records(new_result, mail_news)
    show_news(mail_news)

if __name__ == '__main__':
    sys.exit(main())