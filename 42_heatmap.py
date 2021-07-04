import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
flights_df=sns.load_dataset("flights").pivot("month","year","passengers")#this will put the data frame into a matrix kind of format
plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df)
sns.heatmap(flights_df,fmt="d",annot=True,cmap='Blues')#cmap is for the colour distribution and annot determines the numeric representation in the graph
plt.show()