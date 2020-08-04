import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/running/current.nhn'
respons = requests.get(url)
soup = BeautifulSoup(respons.text,'html.parser')
movie_list = soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li > dl > dt > a')
movies = []
for movie in movie_list :
    code = movie['href'].split('=')[1]
    name = movie.text
    movies.append({'title':name,'code':code})
for i in movies :
    print(i)