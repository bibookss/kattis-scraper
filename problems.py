import requests
from utils import html_page

def get_submissions(user):
    index = 0

    while True:
        url = f'https://open.kattis.com/users/{user.user}?page={index}'		
        page = html_page(requests.get(url, data={'script': 'true'}, cookies=user.cookie))

        print(f'Scraping page {index + 1} of submissions...')

        # check if there are no more submissions
        table = page.find('tbody')
        is_empty = len(table.find_all('tr')) == 0

        if is_empty:
            break

        # get all submissions
        rows = table.select('tr[data-submission-id]')
        for row in rows:
            time = row.find('td', {'data-type': 'time'}).text.strip()
            problem = row.find('td', {'data-type': 'problem'}).text.strip()
            language = row.find('td', {'data-type': 'lang'}).text.strip()
            status = row.find('td', {'data-type': 'status'}).div.text.strip()

            # add to user submissions
            user.submissions.append({
                'time': time,
                'problem': problem,
                'language': language,
                'status': status
            })

        # get next page
        index += 1
		
def get_problems(user):
    print('Scraping problems solved...')
    
    index = 0
    while True:
        url = f'https://open.kattis.com/problems?show_solved=on&show_partial=off&show_tried=off&show_untried=off&page={index}'
        page = html_page(requests.get(url, data={'script': 'true'}, cookies=user.cookie))

        # check if there are no more problems
        table = page.find('tbody')
        is_empty = len(table.find_all('tr')) == 0

        if is_empty:
            break

        # get all problems
        for row in table.find_all('tr'):
            problem_name = row.find('td').a.text.strip()

            # find the problem difficulty
            difficulty_span = row.find('span', class_='difficulty_number-problems_table')
            problem_difficulty = difficulty_span['class'][2].split('_')[-1]

            # add to user problems
            user.problems.append({
                'name': problem_name,
                'difficulty': problem_difficulty
            })

        # get next page
        index += 1

    print('Scraping problems finished...')