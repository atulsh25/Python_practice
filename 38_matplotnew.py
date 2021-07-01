import matplotlib.pyplot as plt
import matplotlib
#the following data will change the default details of matplotlib.rcParams
matplotlib.rcParams['font.size'] = 14 
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
import seaborn as sns
flowers_df = sns.load_dataset("iris")#the iris is a predefined data set of seaborn
print(flowers_df)
print(flowers_df.species.unique())
plt.plot(flowers_df.sepal_length,flowers_df.sepal_width)
plt.show()
sns.scatterplot(x=flowers_df.sepal_length,y=flowers_df.sepal_width)
plt.show(sns)
plt.title('Sepal')
sns.scatterplot('sepal_length','sepal_width',hue='species',s=100)
#this will actually colour the specific species differently and s here signifies the size