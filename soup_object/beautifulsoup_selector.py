import requests
from bs4 import BeautifulSoup

res =  requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.select('.score'))

# print(soup.select('#score_20514755'))

print(soup.select('.storylink')[0])
