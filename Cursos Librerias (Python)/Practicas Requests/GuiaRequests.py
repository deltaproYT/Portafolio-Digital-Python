import requests as rq

response = rq.get('https://jsonplaceholder.typicode.com/posts')

print(response.status_code)
print(response.json())
#print(response.text)