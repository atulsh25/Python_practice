import urllib.request
import numpy as np
urllib.request.urlretrieve(
    'https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv', 
    'climate.txt')
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print(climate_data.shape)
weights = np.array([0.3, 0.2, 0.5])
yields=climate_data@weights
print(yields)
print(yields.shape)
results=np.concatenate((climate_data,yields.reshape(10000,1)),axis=1)
#axis=1 is for adding the data along the column 
#axis=0 is for adding the data along the row
print(results)
np.savetxt('climate_results.txt',results,fmt='%.2f',header='temperature,rainfall,humidity,yeild_apples', 
           comments='')
           