# import pymongo
# from pymongo import MongoClient
# from pprint import pprint
#
# client = MongoClient('127.0.0.1', 27017)
# db = client['vacancies20220709']
# analytics = db.analytics
#
# # doc = {"author": "Peter2",
# #        "age": 38,
# #        "text": "is cool! Wildberry",
# #        "tags": ['cool', 'hot', 'ice'],
# #        "date": '14.06.1983'}
# #
# # analytics.insert_one(doc)
# #
# # for item in analytics.find({}):
# #     pprint(item)
#
# analytics.delete_many({})
# for item in analytics.find({}):
#     pprint(item)

import re
import requests
from pymongo import MongoClient
from pprint import pprint
from bs4 import BeautifulSoup as bs
#
# _SEARCH_STR = 'бизнес-аналитик'
#
# def isint(s):
#     try:
#         int(s)
#         return True
#     except ValueError:
#         return False
#
# class VacancyScrapper:
#     def __init__(self, search_str):
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'
#             }
#         self.url = 'https://moscow.hh.ru/search/vacancy'
#         self.storage = list()
#         self._SEARCH_STR = search_str
#         self.parse_vacancy()
#     def parse_vacancy(self):
#         self.storage.extend(self.parse_hh())
#     def parse_hh(self):
#         vacancies_list = []
#         params = {
#             'search_field': ['company_name','description', 'name'],
#             'text': self._SEARCH_STR,
#             'search_field': 'name',
#             'items_on_page': '20',
#             'page': '0',
#             'hhtmFrom': 'vacancy_search_list',
#             'showClusters': 'true'
#         }
#         session = requests.Session()
#         response = session.get(self.url, headers=self.headers, params=params)
#         dom = bs(response.text, 'html.parser')
#         last_page_text = dom.find('a', {'data-qa': 'pager-next'}).previous_sibling.text
#         last_page = last_page_text[3:]
#
#         for i in range(0, int(last_page)):
#             print(f'Please wait. In progress... scrapping page {i}')
#             params['page'] = i
#             response = session.get(self.url, headers=self.headers, params=params)
#             dom = bs(response.text, 'html.parser')
#             vacancies = dom.find('div', {'data-qa': 'vacancy-serp__results'}) \
#                                 .find_all('div', {'class': 'vacancy-serp-item'})
#             for vacancy in vacancies:
#                 vacancies_list.append(self.parse_vacancy_hh(vacancy))
#         return vacancies_list
#     def parse_vacancy_hh (self, vacancy):
#         vacancy_data = {}
#         main_info = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-title'})
#         name = main_info.getText().replace(u'\xa0', u' ')
#         href = main_info.get('href')
#         salary = vacancy.find('span', {'data-qa': 'vacancy-serp-item__compensation'})
#         if not salary:
#             salary_min = None
#             salary_max = None
#             salary_currency = None
#         else:
#             salary = salary.getText().replace(u'\xa0', u' ')
#             salary = re.split(r'\s|<|>', salary)
#             if salary[0] == 'до':
#                 salary_min = None
#                 if isint(salary[1]) and isint(salary[2]):
#                     salary_max = int("".join([salary[1], salary[2]]))
#                     salary_currency = salary[3]
#                 else:
#                     salary_max = int(salary[1])
#                     salary_currency = salary[2]
#             elif salary[0] == 'от':
#                 if isint(salary[1]) and isint(salary[2]):
#                     salary_min = int("".join([salary[1], salary[2]]))
#                     salary_currency = salary[3]
#                 else:
#                     salary_min = int(salary[1])
#                     salary_currency = salary[2]
#                 salary_max = None
#             else:
#                 if isint(salary[0]) and isint(salary[1]):
#                     salary_min = int("".join([salary[0], salary[1]]))
#                     if isint(salary[3]) and isint(salary[4]):
#                         salary_max = int("".join([salary[3], salary[4]]))
#                         salary_currency = salary[5]
#                     else:
#                         salary_max = int(salary[10])
#                         salary_currency = salary[4]
#                 else:
#                     salary_min = int(salary[0])
#                     if isint(salary[2]) and isint(salary[3]):
#                         salary_max = int("".join([salary[2], salary[3]]))
#                         salary_currency = salary[4]
#                     else:
#                         salary_max = int(salary[2])
#                         salary_currency = salary[3]
#
#         employer_name = vacancy.find('a', {'data-qa': 'vacancy-serp__vacancy-employer'}).getText().replace(u'\xa0', u' ').split(', ')[0]
#
#         city = vacancy.find('span', {'data-qa': 'vacancy-serp__vacancy-address'}).getText().split(', ')[0]
#
#         metro_name = vacancy.find('span', {'class': 'metro-station'})
#         if not metro_name:
#             metro_name = None
#         else:
#             metro_name = metro_name.getText()
#
#         vacancy_data['name'] = name
#         vacancy_data['link'] = href
#         vacancy_data['salary_min'] = salary_min
#         vacancy_data['salary_max'] = salary_max
#         vacancy_data['salary_currency'] = salary_currency
#         vacancy_data['employer_name'] = employer_name
#         vacancy_data['city'] = city
#         vacancy_data['metro_name'] = metro_name
#
#         return vacancy_data

client = MongoClient('127.0.0.1', 27017)
db = client['vacancies20220709']
analytics = db.analytics

# scrapper = VacancyScrapper(_SEARCH_STR)
# analytics.insert_many(scrapper.storage)




for item in analytics.find({}):
    pprint(item)
print()