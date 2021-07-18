import os
print(os.getcwd())#this will give us the the current directory
os.chdir('data')#this changes the current directory
print(os.getcwd())
print(os.listdir())#this will list the contents of the current directory
os.mkdir('myfolder3')#this will create a new directory in the current location
os.makedirs('myfolder\datafolder')#create director in a specific path
os.rmdir("myfolder")#deletes specific the directory
os.rmdir("myfolder\datafolder")#this removes only the subfolder
os.rmdir("myfolder1")
os.rmdir("myfolder3")
os.remove('myfile.txt')#this removes a specific file
os.removedirs('myfolder\datafolder')#this will remove all the folders aand subfolders
os.rename('loans2.txt','loan1.txt')