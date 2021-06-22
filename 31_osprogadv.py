import os
url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'
from urllib.request import urlretrieve
urlretrieve(url1, './data/loans1.txt')
urlretrieve(url2, './data/loans2.txt')
urlretrieve(url3, './data/loans3.txt')
print(os.listdir('./data'))
file1 = open('./data/loans1.txt', mode='r')
file1_contents = file1.read()
print(file1_contents)
file1.close()
#Closing files automatically using with
with open('./data/loans2.txt') as file2:
    file2_contents = file2.read()
    print(file2_contents)
#Reading a file line by line
with open('./data/loans3.txt', 'r') as file3:
    file3_lines = file3.readlines()