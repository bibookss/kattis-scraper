import matplotlib.pyplot as plt
import numpy as np
import july
from july.utils import date_range
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

def submission_heatmap(user):
    df = pd.DataFrame(user.submissions)
   
    df['date'] = pd.to_datetime(df['time']).dt.date
    
    oldest_date = df['date'].min()
    newest_date = df['date'].max()
    dates = date_range(oldest_date, newest_date)
    
    # Convert 'Date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Set 'Date' column as the DataFrame index
    df.set_index('date', inplace=True)

    # Resample by day and count occurrences
    daily_counts = df.resample('D').size()

    # Create a date range within the desired range
    start_date = df.index.min()
    end_date = df.index.max()
    dr = pd.date_range(start=start_date, end=end_date, freq='D')

    # Reindex with the date range to add missing dates
    daily_counts = daily_counts.reindex(dr, fill_value=0)
        
    data = daily_counts.values
    july.heatmap(dates, data, title='Kattis Activity', cmap="github", colorbar=True)

