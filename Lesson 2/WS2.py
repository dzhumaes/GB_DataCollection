import requests
from bs4 import BeautifulSoup
from pprint import pprint

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.3.684 Yowser/2.5 Safari/537.36'}
url = 'https://www.pik.ru/search/lospark?rooms=1'

session = requests.Session()
response = session.get(url)

dom = BeautifulSoup(response.text, 'html.parser')
# print(dom)

tag_a = dom.find('a', {'data-id': '797317'})
# print(tag_a)
# print(tag_a.text)
print(tag_a.get('href'))

# tags = dom.find_all('a')
# pprint(tags)

tag = dom.find_all('a', {'class': 'sc-jBoNkH eHkLgQ'})
pprint(tag)