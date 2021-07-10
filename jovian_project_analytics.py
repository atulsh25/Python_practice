# Change this
dataset_url = 'https://www.kaggle.com/gregorut/videogamesales?select=vgsales.csv' 
import opendatasets as od
od.download(dataset_url)
project_name = "zerotopandas-course-project-starter-atul_game_sales"
#this will retrieve the data from the csv file and load it into a dataframe
import pandas as pd
gsales_df=pd.read_csv('./videogamesales/vgsales.csv')
#this will show case the data frame that has been loaded
print(gsales_df)
#this will give the nature of the data frame with respect to the columns i.e., data type used for the columns
print(gsales_df.info())
#this will give the mathematical details such as count,mean and the percentage of the data being used
#the max and min value present in the referred column and others
print(gsales_df.describe())
#this give the number of rows and column details in the data frame
print(gsales_df.shape)
#the following t_sales will hold the total sales made from all the games here we are using .sum() of Pandas 
tot_sales=gsales_df.Global_Sales.sum()
#the following part will create an additional column that will hold the percentage of total revenue made by a game of total revenue of all the games
gsales_df['Percentage_Sales']=(gsales_df.Global_Sales/tot_sales)*100
#this will represent the data details with the additional column being included
print(gsales_df)
#NumPy is a library for the Python programming language,
#adding support for large, multi-dimensional arrays and matrices,
#along with a large collection of high-level mathematical functions to operate on these arrays
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (40, 40)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
plt.bar(gsales_df['Platform'],gsales_df['Percentage_Sales'])
plt.show()
#this is the data representation of the graphical representation of the above graph
#here we are grouping the percentage of sales made at the same platforms
print(gsales_df.groupby('Platform')[['Percentage_Sales']].sum())
#this will group the data based on publisher and the genre where the sales was made
nw_df=gsales_df.groupby(['Publisher','Genre'])[['Percentage_Sales']].sum()
#this will create a dataframe with top 10 publishers and Genre where the maximum sales was made by using sorting and extracting
top_10_pub_df=nw_df.sort_values('Percentage_Sales',ascending=False).head(10)
#this will plot a heat map for top 10 publishers and Genre 
matplotlib.rcParams['figure.figsize'] = (9, 5)
sns.heatmap(top_10_pub_df,fmt="f",annot=True,cmap='Blues')
plt.show()
#here we are extracting the data using conditional operator
new_gsales_df=gsales_df[(gsales_df['Year']>=2000)&(gsales_df['Year']<=2010)]
#here we have grouped the sales data based on the year
sales_df=new_gsales_df.groupby('Year')[['EU_Sales','JP_Sales']].sum()
print(sales_df)
#by using the scatter polt we can identify where the maximum sales was made
sns.scatterplot(x=sales_df.EU_Sales, 
                y=sales_df.JP_Sales, 
                hue=sales_df.index, 
                s=100)
plt.show()
from urllib.request import urlretrieve
urlretrieve('https://upload.wikimedia.org/wikipedia/commons/4/43/Xbox-console.jpg', 'XBOX.jpg');
from PIL import Image#PIL is python image Library
img = Image.open('XBOX.jpg')
img_array = np.array(img)#the image here is a three dimensional array where the array is an array of RGB color format that's why we are using numpy
plt.grid(False)#this is for hiding grid details
plt.axis('off')#this is for hiding axis details
#plt.imshow(img[125:225,200:300]);#to show a particular portion of the image
plt.imshow(img)
plt.plot(sales_df.index, sales_df.EU_Sales, 's--b')
plt.show()
#here we will first create a new dataframe having the data after the 2000
nw_after_df=gsales_df[(gsales_df.Year>2000)]
#var_tot will store the sum of all the sales done after year 2000 .sum() is a function of PANDAS 
#that will perform summation of all the data in the particular column on which the summation is performed
var_tot=nw_after_df.JP_Sales.sum()
print(var_tot*1e6)
#var_mean will store the sum of all the sales done after year 2000 .mean() is a function of PANDAS 
#that will perform mean of all the data in the particular column on which the average is performed
var_mean=nw_after_df.EU_Sales.mean()
#var_mean will store the sum of all the sales done after year 2000 .mean() is a function of PANDAS 
#that will perform mean of all the data in the particular column on which the average is performed
var_mean=nw_after_df.EU_Sales.mean()
print(var_mean*1e6)
#from the following graph we can easily determine that Nintendo made the maximum sale in the Year of 2000
nintendo_df=new_gsales_df[new_gsales_df.Publisher=='Nintendo']
plt.bar(nintendo_df.Year,nintendo_df.EU_Sales)
plt.show()
console_df=new_gsales_df.groupby('Platform')[['Global_Sales']].sum()
console_df=new_gsales_df.groupby('Platform')[['Global_Sales']].sum()
#from this we can determine that most played game was PS2 in the complete decade
sns.barplot(x=console_df.index,y='Global_Sales',data=console_df)
plt.show()
#this will help in grouping the Global_Sales data based on the Publishers
pub_df=gsales_df.groupby('Publisher')[['Global_Sales']].sum()
#this will help us in getting top 10 publishers
pub10_df=pub_df.sort_values('Global_Sales',ascending=False).head(10)
#the column data is modified to represent in million
pub10_df['Global_Sales']=pub10_df.Global_Sales*1e6
print(pub10_df)
