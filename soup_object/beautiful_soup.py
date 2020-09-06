import requests
from bs4 import BeautifulSoup

res =  requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.title)

# print(soup.a)
# print(soup.find('a'))

# print(soup.find(id='score_20514755'))

# print(soup.body.contents)

# print(soup.find_all('div'))

# print(soup.find_all('a'))