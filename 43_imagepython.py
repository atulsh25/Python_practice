import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from urllib.request import urlretrieve
urlretrieve('https://i.imgur.com/SkPbq.jpg', 'chart.jpg');
from PIL import Image#PIL is python image Library
img = Image.open('chart.jpg')
img_array = np.array(img)#the image here is a three dimensional array where the array is an array of RGB color format
plt.grid(False)#this is for hiding grid details
plt.axis('off')#this is for hiding axis details
print(img_array)
#plt.imshow(img[125:225,200:300]);#to show a particular portion of the image
plt.imshow(img)
plt.show()