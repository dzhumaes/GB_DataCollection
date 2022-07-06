# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы получаем должность) с сайтов HH(обязательно) и/или Superjob(по желанию). Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:
# Наименование вакансии.
# Предлагаемую зарплату (разносим в три поля: минимальная и максимальная и валюта. цифры преобразуем к цифрам).
# Ссылку на саму вакансию.
# Сайт, откуда собрана вакансия. (можно прописать статично hh.ru или superjob.ru)
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение). Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas. Сохраните в json либо csv.

import requests
import json
import pandas as pd
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

pprint(vacancies_list)
print(len(vacancies_list))

with open('vacancies.json','w') as vcn:
  json.dump(vacancies_list,vcn)
pd.read_json('vacancies.json')

#Задание выполнено