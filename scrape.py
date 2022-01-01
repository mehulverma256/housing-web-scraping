from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a', class_="search-list__item search-list__item--listing").text.replace('\n', '')
        location = list.find('div', class_="listing-search-item__label").text.replace('\n', '')
        
        info = [title, location]
        thewriter.writerow(info)