import requests
from user import User

def auth(username, password):
	url = 'https://open.kattis.com/login/email?'

	login = {
		'user': username,
		'password': password,
		'script': 'true'
	}
	
	res = requests.post(url, data=login)	
	
	cookies = res.cookies
	cookie = { 'EduSiteCookie': cookies['EduSiteCookie'] }
	
	if res.status_code == 200:
		print('Login successful')
		return User(username, cookie)
	
	print('Login failed')
	return None