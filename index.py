import requests
from itertools import groupby

def fetch_data():
  response = requests.get('https://mf-public-demo-files.s3.amazonaws.com/pos.json')
  return response.json()['purchaseOrders']

def grouped_orders(orders):
  if not orders or len(orders) == 0:
    return {}
  print(f'Number of orders: {len(orders)}')

  result = {}
  sort_fn = lambda x: x['id'].split('-')[0]
  orders = sorted(orders, key=sort_fn)
  for key, value in groupby(orders, key=sort_fn):
    result[key] = sorted(list(value), key=lambda y: y['cost'], reverse=True)
  return result

if __name__ == '__main__':
  orders = fetch_data()
  print(grouped_orders(orders))