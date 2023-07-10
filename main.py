import requests
from auth import auth
from problems import get_submissions, get_problems
from dotenv import load_dotenv

def main():
	config = load_dotenv('.env')
	username = config['USERNAME']
	password = config['PASSWORD']

	user = auth(username, password)

	if user:
		get_problems(user)
		get_submissions(user)

if __name__ == '__main__':
	main()

