from urllib.request import urlretrieve
italy_covid_url = 'https://gist.githubusercontent.com/aakashns/f6a004fa20c84fec53262f9a8bfee775/raw/f309558b1cf5103424cef58e2ecb8704dcd4d74c/italy-covid-daywise.csv'

urlretrieve(italy_covid_url, 'italy-covid-daywise.csv')
import pandas as pd
covid_df=pd.read_csv('italy-covid-daywise.csv')
print(covid_df)
print(covid_df.info())#this will give the nature of the data frame with respect to the columns
print(covid_df.describe())#this will give the mathematical details such as count mean and other details
print(covid_df.columns)#this will give the column details of the data frame
print(covid_df.shape)#this give the rows and column details in the data frame
print(covid_df['new_cases'])#this returns the list of complete data in that column header
#OR 
print(covid_df.new_cases)
print(covid_df['new_cases'][246])#the specific values can be retrieved by using indeces
#OR .at method can be used in a similar manner
print(covid_df.at[246,'new_cases'])
print(covid_df[['new_cases','new_deaths']])#multiple columns associated can be accessed
covid_df_new=covid_df[['new_cases','new_deaths']].copy()
print(covid_df_new)
print(covid_df_new.loc[243])
print(covid_df.head(5))#first 5 rows
print(covid_df.tail(5))#last 5 rows
print(covid_df.new_tests.first_valid_index())#This will give the first non NAN indeces in the column
print(covid_df.loc[108:113])
print(covid_df.sample(10))#this will give 10 random data set from the data frame
df_death_sum=covid_df.new_deaths.sum()
print(df_death_sum)
print(covid_df.new_cases>1000)#this is a conditional logic that can be implemented on a dataframe to get where the criteria is satisfied
print(covid_df[covid_df.new_cases>1000])#filter the data based on certain condition
covid_df['total_cases']=covid_df.new_cases.cumsum()#this is the cumulative sum till the particular row
covid_df['total_deaths'] = covid_df.new_deaths.cumsum()
initial_tests = 935310
covid_df['total_tests'] = covid_df.new_tests.cumsum() + initial_tests
print(covid_df.sort_values('new_cases',ascending=True).head(10))
