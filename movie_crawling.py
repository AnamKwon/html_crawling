import requests
from bs4 import BeautifulSoup
import csv
url = 'https://movie.naver.com/movie/running/current.nhn'
respons = requests.get(url)
soup = BeautifulSoup(respons.text,'html.parser')
movie_list = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li > dl > dt > a')
movies = []
for movie in movie_list :
    code = movie['href'].split('=')[1]
    name = movie.text
    movies.append({'title':name,'code':code})

with open('movie_list.csv','w') as f :
    field = ['title','code']
    csv_writer = csv.DictWriter(f,fieldnames=field,)
    csv_writer.writeheader()
    for i in movies :
        csv_writer.writerow(i)