import numpy as np
arr2 = np.array([[1, 2, 3, 4], 
                 [5, 6, 7, 8], 
                 [9, 1, 2, 3]])
arr4 = np.array([4, 5, 6, 7])
print(arr2+arr4)
arr5 = np.array([7, 8])
#print(arr2+arr5)#this will throw error as replication of data is not possible here
arr1 = np.array([[1, 2, 3], [3, 4, 5]])
arr6 = np.array([[2, 2, 3], [1, 2, 5]])
print(arr1==arr6)
print((arr1==arr6).sum())#this will give the number of matching elements in the 2 array
arr7 = np.array([
    [[11, 12, 13, 14], 
     [13, 14, 15, 19]], 
    
    [[15, 16, 17, 21], 
     [63, 92, 36, 18]], 
    
    [[98, 32, 81, 23],      
     [17, 18, 19.5, 43]]])
print(arr7[1:, 1, :3])