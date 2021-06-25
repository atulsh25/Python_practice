from urllib.request import urlretrieve
urlretrieve('https://gist.githubusercontent.com/aakashns/8684589ef4f266116cdce023377fc9c8/raw/99ce3826b2a9d1e6d0bde7e9e559fc8b6e9ac88b/locations.csv', 
            'locations.csv')
import pandas as pd
locations_df = pd.read_csv('locations.csv')
print(locations_df)
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')
import pandas as pd
covid_df=pd.read_csv('italy-covid-daywise.csv')
#covid_df['date']=pd.to_datetime[covid_df.date]#this method is used to covert a column data into date time format
print(covid_df)
#the following methods are used to extract particular date time column such as year day etc in an additional column respectively
covid_df['year'] = pd.DatetimeIndex(covid_df.date).year
covid_df['month'] = pd.DatetimeIndex(covid_df.date).month
covid_df['day'] = pd.DatetimeIndex(covid_df.date).day
covid_df['weekday'] = pd.DatetimeIndex(covid_df.date).weekday
#this is the cumulative sum till the particular row
covid_df['total_cases']=covid_df.new_cases.cumsum()
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
initial_tests = 935310
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests
merged_df = covid_df.merge(locations_df, on="location")#here we are meging 2 data frames based on a particular column
print(merged_df)
merged_df['cases_per_million'] = merged_df.total_cases * 1e6 / merged_df.population
merged_df['deaths_per_million'] = merged_df.total_deaths * 1e6 / merged_df.population
merged_df['tests_per_million'] = merged_df.total_tests * 1e6 / merged_df.population
result_df = merged_df[['date',
                       'new_cases', 
                       'total_cases', 
                       'new_deaths', 
                       'total_deaths', 
                       'new_tests', 
                       'total_tests', 
                       'cases_per_million', 
                       'deaths_per_million', 
                       'tests_per_million']]
result_df.to_csv('results.csv', index=None)#this will push the data from a data frame to a csv file
#as we do not want to retain the information about index so it is set to None