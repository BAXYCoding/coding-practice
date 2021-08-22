import requests
from bs4 import BeautifulSoup
with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')
print(soup.prettify())
