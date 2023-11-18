import requests
URL='https://nbu.uz/uz/exchange-rates/json/'
import json
from aiogram import html
def get_currency():
    data= requests.get(url=URL)
    data = json.loads(data.text)
    text = ''
    for i in data:
        if i['title'] in ['Yevro','Rossiya rubli','AQSh dollari']:
          text+=(f"Nomi:{html.bold(i['title'])}\n"
                f"KODI:{html.bold(i['code'])}\n"
                f"Narx:{html.bold(i['cb_price'])}\n"
                f"Sotib olish:{html.bold(i['nbu_buy_price'])}\n"
                f"Sotish:{html.bold(i['nbu_cell_price'])}\n"
                f"Oxirgi yangilanish:{html.bold(i['date'])}\n\n")
    return text
