from urllib.request import urlretrieve
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')
import pandas as pd
covid_df=pd.read_csv('italy-covid-daywise.csv')
print(covid_df.columns)
covid_df['date']=pd.to_datetime[covid_df.date]#this method is used to covert a column data into date time format
print(covid_df)
#the following methods are used to extract particular date time column such as year day etc in an additional column respectively
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
covid_df_may=covid_df[covid_df.month==5]
covid_df_may_metrics=covid_df[['new_cases','new_tests','new_deaths']]
print(covid_df_may_metrics.sum())#this will return the sum on the entire data metrics
print(covid_df[covid_df.day==6].new_cases.mean())
print(covid_df.groupby('month')[['new_cases','new_tests','new_deaths']].sum())
#the above method is used to combine the similar data set based on a particular column and study their mathematical result
