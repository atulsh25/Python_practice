import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
flowers_df = sns.load_dataset("iris")
plt.title("Distribution of Sepal Width")
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))#alpha here defines the opacity of the graph
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.show()
#all the three graphs can be stacked over each other as follows
plt.hist([versicolor_df.sepal_width,versicolor_df.sepal_width,virginica_df.sepal_width], alpha=0.4, bins=np.arange(2, 5, 0.25),stacked=True)
plt.legend(['Setosa', 'Versicolor', 'Virginica']);
plt.show()