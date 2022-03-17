import requests

r = requests.head('http://mercury.picoctf.net:45028/index.php?')

print(r.headers)