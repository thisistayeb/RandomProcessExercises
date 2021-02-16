import pandas as pd
import matplotlib.pyplot as plt

def plotter(name='1-A.csv'):
    df = pd.read_csv(name)
    ax = plt.gca()
    df.plot(kind='line',x='Time',y='Healthy People',color='green', ax=ax)
    df.plot(kind='line',x='Time',y='Ill People', color='red', ax=ax)
    df.plot(kind='line',x='Time',y='Recoverd people', color='blue', ax=ax)
    df.plot(kind='line',x='Time',y='RIP', color='black', ax=ax)
    plt.savefig('{}.jpg'.format(name))
