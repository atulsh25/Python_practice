myfile=open('sample.txt')#here I have opened the file
content=myfile.read()#this reads the content file
#so once the contents is read from the file we reach the end of the file it doesn't go to the start itself
#thus to reset we use seek
print(content)
data=myfile.read()
print(data+" no data read")
myfile.seek(0)
data=myfile.read()
print(data)
myfile.seek(0)
content_list=myfile.readlines()
myfile.close()#this closes the file to be accessible to others
print(content_list)
