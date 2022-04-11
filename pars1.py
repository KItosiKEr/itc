from webbrowser import get
from bs4 import BeautifulSoup
import requests
import csv

CSV = 'sulpak.csv'
HOST = 'https://www.sulpak.kg'
URL = 'https://www.sulpak.kg/f/noutbuki'
HEADERS = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

def get_html(URL, params = ''):
    r = requests.get(URL, headers=HEADERS, params=params, verify=False)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_= 'goods-tiles')
    comps = []

    for item in items:
        comps.append({
            'Название ноутбука' :
            item.find('div', class_ = 'product-container-right-side').find('h3',
            class_='title'),

            'Ссылка на ноутбук' : HOST +
            item.find('div',
            class_ = 'product-container-right-side').find('a').get('href'),

            'Цена Ноутбука': item.find('div',
            class_ = 'product-container-right-side').find('div',
            class_ = 'price')
        })
    return comps

def save(items, path):
    with open(path, 'a') as file:
        writer = csv.writer(file, delimiter = ';')
        writer.writerow(['Название', 'Ссылка','Цена'])
        for item in items:
            writer.writerow([item['Название ноутбука'], item['Ссылка на ноутбук'], item['Цена Ноутбука']])

def pagination():
    PAGINATION = input('Введите кол-во страниц ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        items = []
        for page in range(1, PAGINATION + 1):
            print(f"Страница №{page} готова")
            html = get_html(URL, params={'page' : page})
            items.extend(get_content(html.text))
        save(items, CSV)
        print("parsing is done!")
    else:
        print("Error")
pagination()



#**********************************************************************************
# from bs4 import BeautifulSoup
# import requests


# url = 'https://www.sulpak.kg/f/noutbuki'
# HOST = 'https://www.sulpak.kg'
# soup = BeautifulSoup(r.text)

# def get_html(url):
#     r = requests.get(url,verify=False)
#     return r.text

# def get_content(html):
#     soup = BeautifulSoup(html)
#     items = soup.find_all('div',class_='goods-tiles')


#     comps = []

#     for item in items:
#         comps.append({
#             'name':item.find('div',class_='title'),
#             'price':item.find('div',class_='price'),
#             'link':item.find('div',class_='goods-photo').find('a').get('href')
#         })
#     print(comps)
