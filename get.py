import requests
from bs4 import BeautifulSoup, element
import time
import json
from collections import OrderedDict

url = 'https://hougen.ajima.jp/gojyuon/'
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

elements_p = soup.find('div', class_='gojyuon_outer').find_all('a')

urls = []

for gojyuon in elements_p:
    urls.append(gojyuon.get('href'))

time.sleep(1)

json_list = []

for url in urls:
    time.sleep(2)
    url = 'https://hougen.ajima.jp' + url
    res = requests.get(url)
    soup = BeautifulSoup(res.content, "html.parser")
    elements_p = soup.find('ul', class_='list_hougen').find_all('div', class_='text')
    for text in elements_p:
        print(text.find('h1').get_text())
        data = OrderedDict()
        word = text.find('h1').get_text()
        meaning = text.find('div', class_='std').get_text()
        if len(word) <= 6:
            data["word"] = word
            data["meaning"] = meaning
            json_list.append(data)

    output_name = './output.json'
    with open(output_name, 'w') as file:
        json.dump(json_list, file, indent=4, ensure_ascii=False)
print(len(json_list))



    
