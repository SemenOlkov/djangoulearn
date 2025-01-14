import requests
from xml.etree import ElementTree
from datetime import datetime, timedelta


def parse_currencies(date):
    get = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')
    if get.status_code == 200:
        root = ElementTree.fromstring(get.content)
        for currency in root.findall('.//Valute'):
            curr = currency.find('CharCode').text
            if curr in currency_list:
                currency_data[date][curr] = round(float(currency.find('Value').text.replace(',', '.')) / int(currency.find('Nominal').text), 9)


currency_list = ['BYR', 'USD', 'EUR', 'KZT', 'UAH', 'AZN', 'KGS', 'UZS', 'GEL']
start_date = datetime(2003, 1, 1)
end_date = datetime(2024, 11, 30)
all_dates = [(start_date + timedelta(days=i)).strftime('%d/%m/%Y') for i in range((end_date - start_date).days + 1)]
currency_data = {date: {currency: None for currency in currency_list} for date in all_dates}
for date in all_dates:
    parse_currencies(date)

with open('currency.csv', 'w') as file:
    file.write('date,' + ','.join(currency_list) + '\n')
    for date in all_dates:
        formatted_date = date.split('/')
        file.write(','.join([f"{formatted_date[0]}-{formatted_date[1]}-{formatted_date[2]}"] + [str(currency_data[date][currency]) if currency_data[date][currency] is not None else '' for currency in currency_list]) + '\n')
