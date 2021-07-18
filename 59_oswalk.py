import os

for a,b,c in os.walk("myfolder"):#this will allow us to walk through the directories
    print(a)#directory path
    print(b)#directory
    print(c)#contents of directory
    print("------------------------")

#print(os.environ.get("data")+"/"+"loan1.txt")#this is for getting the environment variables
#os.path.join(os.environ.get("data"),"loan1.txt")
#this is to get the basename of a file at the directory location given
print(os.path.basename("stuff\sample1.txt"))
#this is to get the dir name only and not the path
print(os.path.dirname("stuff\sample1.txt"))
#this is to get the both dirname and basename
print(os.path.split("stuff\sample1.txt"))
print(os.path.exists("stuff\sample1.txt"))#this is used to check if the path exist
print(os.path.isfile("stuff\sample1.txt"))#this is used to check if the file exist
print(os.path.splitext("stuff\sample1.txt"))#splits the file name and path from the format