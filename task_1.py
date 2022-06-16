from urllib import request
from os import path
import requests
from bs4 import BeautifulSoup

req = requests.get("https://xkcd.com/archive/")

soup = BeautifulSoup(req.content, "html.parser")

div_bs4 = soup.find('div', id='middleContainer')

base_url = 'https://imgs.xkcd.com/comics/'

for link in div_bs4.find_all('a'):
    link = link.get('href')
    new_link = 'https://xkcd.com/' + link

    new_req = requests.get(new_link)
    soup = BeautifulSoup(new_req.content, "html.parser")

    div_bs = soup.find('div', id='middleContainer')
    first_link = div_bs.find_all('a', recursive=False)[1].get('href')
    fileName = path.basename(first_link)
    request.urlretrieve(first_link, fileName)
