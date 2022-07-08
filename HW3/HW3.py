# 1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, которая будет добавлять только новые вакансии/продукты в вашу базу.
# 2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы (необходимо анализировать оба поля зарплаты).
# То есть цифра вводится одна, а запрос проверяет оба поля

import sys
from pymongo import MongoClient
from pymongo import errors
from pprint import pprint

def main():
   client = MongoClient('127.0.0.1', 27017)
   db = client['vacancies20220708']
   analytics = db.analytics

   scrapper =



