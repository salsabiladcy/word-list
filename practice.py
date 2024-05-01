import requests

api_key = '691c671f-2880-4809-a4ca-c8f0b1f75cad'
word = 'Potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)