import requests


data = {
	'score': '1000000000',
	'generate': 'Give a try!'
}
r = requests.post('http://challenge01.root-me.org/web-serveur/ch56/', data=data)


print(r.text)