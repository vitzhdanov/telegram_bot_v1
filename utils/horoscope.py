from bs4 import BeautifulSoup as bs

import requests

from aiogram.utils.markdown import hbold, hunderline

dict_hor = {}


def get_data():
    headers = {
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }
    # get_url = requests.get(url, headers).text

    # with open('url_text.html', 'w') as file:
    #     file.write(get_url)
    with open('D:/BOT_HARRY/utils/horoscope_dir/url_text.html') as file:
        text = file.read()

    soup = bs(text, 'lxml')
    url_horoscope = soup.find('strong').find_all('a')
    list_url = []
    for i in url_horoscope:
        list_url.append(('http://stoboi.ru/gorodaily/' + i.get('href')))

    for i in list_url:
        text_hor = requests.get(i).text
        soup = bs(text_hor, 'lxml')
        hor_sign_date_parse = soup.find(id="rightcolumn").find_all(align="center")
        hor_sign_parse = soup.find(id="rightcolumn").find_all('title')
        hor_sign_date = []
        hor_sign = []
        for s in hor_sign_parse:
            hor_sign.append(s.text.split()[2].lower())
        for sd in hor_sign_date_parse:
            hor_sign_date.append(sd.text)
        hor_res_text = soup.find(id="rightcolumn").find_all(align='left')
        hor_text = []
        for t in hor_res_text:
            hor_text.append(t.text)
        nl = '\n'.join(hor_text)
        dict_hor[' '.join(hor_sign)] = f"{hunderline(' '.join(hor_sign_date)).center(20)}\n\n{hbold(nl).center(40)}"