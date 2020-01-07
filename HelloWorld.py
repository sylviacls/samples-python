import requests

msg = 'Hellow Python'
print(msg)

r = requests.get('https://www.google.com')
print (r.status_code)

