import requests
from bs4 import BeautifulSoup
url = 'http://news.ncu.edu.cn/'
res = requests.get(url)
res.encoding = 'UTF-8'
soup = BeautifulSoup(res.text,'html.parser')
for news in soup.select('.news-item'):
    h2 = news.select('h2')
    if len(h2) > 0:
        title = h2[0].text
        print(title)
