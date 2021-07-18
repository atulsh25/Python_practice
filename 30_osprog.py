import os
print(os.getcwd())#this gives the path of the file or the current working directory
print(os.listdir())#this gives the list of the files in the current directory
os.makedirs('./data',exist_ok=True)
for d in os.listdir('.'):
    print(d)
print('data' in os.listdir('.'))
