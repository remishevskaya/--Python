import requests
from decimal import Decimal

response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates(currency):
    if currency.upper() not in response.text:
        print('None')
    else:
        course = response.text[response.text.find('<Value>', response.text.find(currency.upper())) + 7:
                               response.text.find('<Value>', response.text.find(currency.upper())) + 14]
        course = course.replace(',', '.')
        return Decimal(course)


print('Курс доллара США:', currency_rates('usd'))
print('Курс евро:', currency_rates('eur'))
