from bs4 import BeautifulSoup
import urllib3

address = 'https://www.pcmag.com/news/rtx-3080-ti-founders-edition-was-in-very-short-supply-at-best-buys-across'
http = urllib3.PoolManager()
response = http.request('GET', address)
soup = BeautifulSoup(response.data,'html.parser')
# print(soup)
paragraph=soup.find_all('p')
with open('paragraph.txt','a',encoding="utf-8") as f:
    for i in paragraph:
        f.write(i.get_text())
        f.write('\n')

