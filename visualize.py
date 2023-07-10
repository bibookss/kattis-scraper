import matplotlib.pyplot as plt
import pandas as pd

def visualize_submissions_over_time(user):
    df = pd.DataFrame(user.submissions)
    print(df)