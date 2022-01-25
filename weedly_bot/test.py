import httpx


import httpx

url = 'http://127.0.0.1:5000/api/v1/users/106441967/feeds'
print(httpx.get(url))


url = 'http://127.0.0.1:5000/api/v1/users/106441967/feeds/8'
print(httpx.post(url))
