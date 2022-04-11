from bs4 import BeautifulSoup
import requests


url = 'https://www.sulpak.kg/f/noutbuki'
HOST = 'https://www.sulpak.kg'
r = requests.get(url,verify=False)
soup = BeautifulSoup(r.text)

data = soup.find('ul',class_='goods-container').find_all('li',class_='tile-container')
for i in data:
    title = i.find('h3',class_='title')
    img = i.find('img',class_='image-size-cls')
    a = i.find('div',class_='goods-photo').find('a').get('href')
    print(title)
    print(HOST+a)
    print(img)