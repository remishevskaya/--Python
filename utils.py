import requests
import datetime
from decimal import Decimal
from datetime import datetime


def currency_rates(currency):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if currency.upper() not in response.text:
        print('None')
    else:
        course = response.text[response.text.find('<Value>', response.text.find(currency.upper())) + 7:
                               response.text.find('<Value>', response.text.find(currency.upper())) + 14]
        course = course.replace(',', '.')
        date_request = response.text[response.text.find('Date') + 6:response.text.find('Date=') + 16]
        print('Курс валюты:', Decimal(course), '\n',
              'Дата:', datetime.date(datetime.strptime(date_request, "%d.%m.%Y")))