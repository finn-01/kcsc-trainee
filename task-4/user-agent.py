import requests

headers = {
	'User-Agent': 'Admin'
}

r = requests.get('http://challenge01.root-me.org/web-serveur/ch2/', headers=headers)

print(r.text)