import matplotlib.pyplot as plt
import pandas as pd

def submissions_over_time(user):
	pass

def problem_difficulty(user):
	pass

def ave_tries_per_problem(user):
	pass

def language_used(user):
    	df = pd.DataFrame(user.submissions)

    	language_counts = df['language'].value_counts()

    	plt.bar(language_counts.index, language_counts.values)
    	plt.xlabel('Programming Language')
    	plt.ylabel('Frequency')
    	plt.title('Language Usage')
    	plt.show()

def most_successful_language(user):
	pass
