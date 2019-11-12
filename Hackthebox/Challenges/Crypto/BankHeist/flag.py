import requests
import json

headers = {
    'authority': 'www.dcode.fr',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'origin': 'https://www.dcode.fr',
    'x-requested-with': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
}

data = {
  'tool': 'multitap-abc-cipher',
  'ciphertext': '444333 99966688 277733 7773323444664 84433 22244474433777, 99966688 277733 666552999. 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733. 84433 5533999 8666 84433 55566622255 4447777 22335556669. 4666 8666 727774447777.\n\n47777888 995559888 4555 47777888 44999988 666555997 : 8555444888477744488866888648833369',
  'dico': 'DICO_EN',
  'bruteforce': 'false'
}

response = requests.post('https://www.dcode.fr/api/', headers=headers, data=data)
print json.loads(response.text)['results']

# Send the Obtained Text to http://rumkin.com/tools/cipher/atbash.php to decode
