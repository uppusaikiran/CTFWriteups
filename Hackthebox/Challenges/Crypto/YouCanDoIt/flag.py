import requests

headers = {
    'authority': 'www.dcode.fr',
    'origin': 'https://www.dcode.fr',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'dnt': '1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

data = {
  'tool': 'caesar-box-cipher',
  'ciphertext': 'YHAOANUTDSYOEOIEUTTC!',
  'punctuation': 'false',
  'mode': 'bruteforce',
  'size': ''
}

response = requests.post('https://www.dcode.fr/api/', headers=headers, data=data)
print response.json()['results']
