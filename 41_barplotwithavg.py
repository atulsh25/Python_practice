import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
tips_df=sns.load_dataset("tips")
print(tips_df)
avg_tips_df=tips_df.groupby('day')[['total_bill']].mean()
print(avg_tips_df)
plt.bar(avg_tips_df.index,avg_tips_df.total_bill)
plt.show()
sns.barplot('day','total_bill',hue='sex',data=tips_df)#the other method to get an average plotted barchart
plt.show()