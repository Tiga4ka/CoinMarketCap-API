from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'c540f1fc-2dce-4ae0-a454-8d0ebfbf51b2',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
  
  
#   Приводим в нормальный вид (для Jupyter Notebook)
import pandas as pd
pd.set_option('display.max_columns', None)

pd.json_normalize(data['data'])

# Записываем в json
with open('CMC_json.json', 'w') as outfile:
    json.dump(data, outfile)
