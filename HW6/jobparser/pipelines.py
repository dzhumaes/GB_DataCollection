# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient

class JobparserPipeline:
    def __init__(self):
        client = MongoClient('127.0.0.1', 27017)
        self.mongo_base = client.vacancies2607

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]

        item['salary'] = self.process_salary(item['salary'])
        item['metro_name'] = self.process_metro(item['metro_name'])
        item['name'] = item['name'].replace(u'\xa0', u' ')
        item['site'] = 'https://hh.ru'
        item['url'] = item['url'][:item['url'].find('?')]

        collection.insert_one(item)
        return item

    def process_salary(self, salary):
        salary_list = []
        for _ in salary:
            s = _.replace(" ", "").replace("\xa0", "")
            salary_list.append(s)
        salary = salary_list
        if salary[0] == 'от':
            salary_min = int(salary[1])
            if salary[2] == 'до':
                salary_max = int(salary[3])
                salary_currency = salary[5]
            else:
                salary_max = 'NA'
                salary_currency = salary[3]
        elif salary[0] == 'до':
            salary_min = 'NA'
            salary_max = int(salary[1])
            salary_currency = salary[3]
        elif salary[0] == 'з/пнеуказана':
            salary_min = 'NA'
            salary_max = 'NA'
        else:
            salary_min = 'wrong'
            salary_max = 'wrong'
        del salary
        return salary_min, salary_max, salary_currency

    def process_metro(self, metro_name):
        if not metro_name:
            metro_name = None
        else:
            metro_name = metro_name.getText()
        return metro_name
