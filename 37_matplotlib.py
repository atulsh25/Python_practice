import matplotlib.pyplot as plt
import seaborn as sns
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years,apples,markers='.')#this represents the plot(x,y) axis for the line graph
plt.plot(years,oranges,markers='x')#the markers can be added to the line graph to differentiate the graphs
#OR
#fmt'[marker][line][color]' formatting can be used to represent the graphs formatting
#plt.plot(years, apples, 's-b')
#plt.plot(years, oranges, 'o--r')
plt.figure(figsize=(8,6))#this will help in changing the size of the plotted graph
#sns.set_style("whitegrid")#this can only be used when we are using a marker format
plt.xlabel('Year')#this represents the label that will be given to the x axis
plt.ylabel('Yield tons per hectare')#this represents the label that will be given to the y axis
plt.title('Crop yields in Kanto')#this will lable the entire chart
plt.legend(['Apples','Oranges'])#this will help in labelling the line graph to indicate the detailing
plt.show()