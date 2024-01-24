import requests
from bs4 import BeautifulSoup as bs
'''Kommentti lisätty'''
url = "https://sedu.fi/kampus/sedu-seinajoki-suupohjantie/#ruokalista"
response = requests.get(url)
soup = bs(response.content, 'html.parser')
header = soup.find(lambda tag:tag.name=="h1" and "Viikon ruokalista" in tag.text)
element = soup.find(id='ruokalista')
text = element.text
lines = text.split('\n')
weekdays = ['Maanantai', 'Tiistai', 'Keskiviikko', 'Torstai', 'Perjantai']

directory_path = "C:\\Users\\Janne\\Desktop\\"

with open(f'{directory_path}/Ruokalista.txt', 'w') as f:# Open the file in write mode ('w')
    for line in lines:
        if line.strip():
            if any(line.startswith(weekday) for weekday in weekdays):
                f.write('\n')  # Write an empty line before the weekday
            f.write(line + '\n')  # Write the line to the file
