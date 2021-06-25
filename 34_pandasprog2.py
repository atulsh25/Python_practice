from urllib.request import urlretrieve
from numpy import positive
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')
import pandas as pd
covid_df=pd.read_csv('italy-covid-daywise.csv')
print(covid_df)
from IPython.display import display
with pd.option_context('display.max_rows',100):
    display(covid_df[covid_df.new_cases>1000])
covid_df['positive_rates']=covid_df.new_cases/covid_df.new_tests#this method is used to create a new column in the data frame
print(covid_df)
covid_df.drop(columns='positive_rates',inplace=True)
print(covid_df)
print(covid_df.sort_values('new_cases',ascending=True).head(10))#this method is used to sort the data based on a particular column 
