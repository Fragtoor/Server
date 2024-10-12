import requests

url = 'http://127.0.0.1:5000/find_toponym'
cord_user = '60.646765, 56.812217'
request = 'Парк Маяковского'
files = {
    'coordinates': cord_user,
    'request':  request
}

response = requests.post(url, json=files)

print(response.json())
