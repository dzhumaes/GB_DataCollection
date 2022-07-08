import requests
import json
import pandas as pd
import pymongo
from pymongo import MongoClient
from pymongo import errors
from bs4 import BeautifulSoup as bs
from pprint import pprint

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
url = 'https://hh.ru'
search_str = 'бизнес-аналитик'
params = {'page': '0', 'hhtmFrom': 'vacancy_search_list'}

session = requests.Session()
response = session.get(url+'/search/vacancy?area=1&industry=7.539&search_field=name&search_field=company_name&search_field=description&text='+search_str+'&showClusters=true', headers = headers, params=params)



dom = bs(response.text, 'html.parser')
vacancies = dom.find_all('a', {'data-qa': 'vacancy-serp__vacancy-title'})
last_page_text = dom.find('a', {'data-qa': 'pager-next'}).previous_sibling.text
last_page = last_page_text[3:]

class VacancyScrapper:

   def parse_vacancy_hh (self)
      vacancies_list = []
         for i in range(0, int(last_page)):
            print(f'Please wait. In progress... scrapping page {i}')
            params['page'] = i
            response = session.get(url + '/search/vacancy?area=1&industry=7.539&search_field=name&search_field=company_name&search_field=description&text=бизнес-аналитик', headers=headers, params=params)
            dom = bs(response.text, 'html.parser')
            vacancies = dom.find_all('span',{'class':'g-user-content'})

         for vacancy in vacancies:
            vacancy_data = {}
            main_info = vacancy.findChild()
            href = main_info.get('href')
            name = main_info.getText()
            salary = vacancy.find('div',{'class':'vacancy-serp-item__compensation'})
            if not salary:
               salary_min=0
               salary_max=0
            else:
               salary=salary.getText().replace(u'\xa0', u' ')
               salaries=salary.split('-')
               salary_min=salaries[0]
               if len(salaries)>1:
                  salary_max=salaries[1]
               else:
                  salary_max=''
            vacancy_data['name'] = name
            vacancy_data['salary_min'] = salary_min
            vacancy_data['salary_max'] = salary_max
            vacancy_data['link'] = href

            vacancies_list.append(vacancy_data)