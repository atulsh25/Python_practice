import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]
plt.bar(years, oranges)
plt.plot(years, oranges,'.--r')#here both line and bar chart are mapped together
plt.show()
plt.bar(years, apples)
plt.bar(years, oranges,bottom=apples)#here both the bar graphs are stacked over each other
plt.show()