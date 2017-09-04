import requests
import json

url_dicas = requests.get('https://api.familink.com.br/rest/dicas').json()

for dica in url_dicas:
    print dica['id']


arquivo = open("dicas.json", "r+")
for dica in json.load(arquivo):
    print dica['titulo']