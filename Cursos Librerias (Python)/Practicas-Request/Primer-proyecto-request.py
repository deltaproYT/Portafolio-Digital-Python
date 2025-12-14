import requests as rq

html = rq.get('https://registronacionalinfielesecuador.com/')
print(html.json())