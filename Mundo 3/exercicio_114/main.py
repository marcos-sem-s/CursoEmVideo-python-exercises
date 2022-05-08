import requests

r = requests.get('https://github.com/Ninniet5670')

print(r)
if r.status_code == 200:
    print('Site está acessível')
elif r.status_code == 404:
    print('Site não está acessível')
