import pymongo
from pymongo import MongoClient
from pymongo import errors
from pprint import pprint

client = MongoClient('127.0.0.1', 27017)

db = client['users0507']
db2 = client['users2']
persons = db.persons       
books = db.books

doc = {"author": "Peter2",
       "age": 38,
       "text": "is cool! Wildberry",
       "tags": ['cool', 'hot', 'ice'],
       "date": '14.06.1983'}

persons.insert_one(doc)


# doc = {"_id": 13589516354,
#        "author": "Peter2",
#        "age": 38,
#        "text": "is cool! Wildberry",
#        "tags": ['cool', 'hot', 'ice'],
#        "date": '14.06.1983'}
#
# try:
#     persons.insert_one(doc)
# except errors.DuplicateKeyError:
#     print(f"Document with id = {doc['_id']} is already exists")


# authors_list = [{"author": "John",
#                "age" : 29,
#                "text": "Too bad! Strawberry",
#                "tags": 'ice',
#                "date": '04.08.1971'},
#
#                     {"_id": 123,
#                         "author": "Anna",
#                "age" : 36,
#                "title": "Hot Cool!!!",
#                "text": "easy too!",
#                "date": '26.01.1995'},
#
#                    {"author": "Jane",
#                "age" : 43,
#                "title": "Nice book",
#                "text": "Pretty text not long",
#                "date": '08.08.1975',
#                "tags":['fantastic', 'criminal']}]
#
#
# persons.insert_many(authors_list)



# item = persons.find_one({})
# pprint(item)

# for item in persons.find({'$or':
#                               [{'author': 'Peter2'},
#                                {'age': 29}
#                                ]}):
#     pprint(item)


# for item in persons.find({'age': {'$gte': 29}}):
#     pprint(item)

# for item in persons.find({'author': {'$regex': '^Pet$'}}):
#     pprint(item)


persons.create_index([('author', pymongo.TEXT)], name='search_index', unique=True)

new_data = {
    "author": "Andrey",
               "age" : 28,
               "text": "is hot!",
               "date": '11.09.1991'}

# persons.update_one({'author': 'Andrey'}, {'$set': new_data})                # update_many()
# persons.update_one({'author': 'Andrey'}, {'$unset': {'tags': ''}})
# result = persons.replace_one({'author': 'Peter21'}, new_data)                           # replace_many()
# print(result.raw_result)


# persons.delete_one({'author': 'John'})
# persons.delete_many({})

for item in persons.find({}):
    pprint(item)

# db.drop_collection('persons')