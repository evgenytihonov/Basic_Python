from requests import get, utils
from sys import argv

response = utils.get_unicode_from_response(get('http://www.cbr.ru/scripts/XML_daily.asp'))


def currency_rates(code):
    content = response.split('<Valute ID="')
    for i in content:
        if code.upper() in i:
            print(code.upper(), end=' ')
            return float(i.replace('/', '').split('<Value>')[-2].replace(',', '.'))


if __name__ == "__main__":
    word = argv[1]
    print(currency_rates(word))
