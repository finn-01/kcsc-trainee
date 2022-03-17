import requests

headers = {
	'X-Forwarded-For': '192.168.1.1'
}

r = requests.get('http://challenge01.root-me.org/web-serveur/ch68/', headers=headers)

print(r.text)