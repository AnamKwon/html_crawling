
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
    headers = {
        'authority': 'movie.naver.com',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Mobile Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=188909',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'NNB=FAMNODEAF37V4; NRTK=ag#all_gr#4_ma#2_si#2_en#2_sp#2; MM_NEW=1; NFS=2; MM_NOW_COACH=1; nx_ssl=2; _ga=GA1.2.268620099.1596596906; csrf_token=3adba57a-fd41-4000-8d86-48893db6453f',
    }

    params = (
        ('code', code),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
    )

    response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)

    soup = BeautifulSoup(response.text, 'html.parser')
    selector = soup.select('body > div > div > div.score_result > ul > li')
    print(name, '\t', code)
    for i in selector :
        star_score = i.select('div.star_score > em')[0].text
        if i.select('div.score_reple > p > span > span > a', onclick=True) == [] :
            review = i.select('div.score_reple > p > span')[-1].text.strip()
        else :
            review = i.select('div.score_reple > p > span > span > a', onclick=True)[0]
            review = str(review).split('"')[1]
        print(star_score, review)

        