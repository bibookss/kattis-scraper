import requests
from auth import auth
from problems import get_submissions, get_problems
from dotenv import dotenv_values

def main():
	config = dotenv_values('.env')
	username = config['USERNAME']
	password = config['PASSWORD']

	user = auth(username, password)

	if user:
		get_problems(user)
		get_submissions(user)

if __name__ == '__main__':
	main()

