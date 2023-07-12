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

def most_succesful_language(user):
    df = pd.DataFrame(user.submissions)
    
    accepted_df = df[df['status'] == 'Accepted']    
    not_accepted_df = df[df['status'] != 'Accepted']
    
    accepted_counts = accepted_df['language'].value_counts()
    not_accepted_counts = not_accepted_df['language'].value_counts()
    
    normalized_counts = accepted_counts / (accepted_counts + not_accepted_counts)
    
    plt.bar(normalized_counts.index, normalized_counts.values * 100)
    plt.xlabel('Programming Language')
    plt.ylabel('Acceptance Rate in Percentage')
    plt.title('Most Successful Language')
    plt.show()
