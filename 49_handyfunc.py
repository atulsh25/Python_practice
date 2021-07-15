word="hello"
for i in list(word):#this is a method to convert a string to a list
    print(i)
print("----------------------------------")
for num in range(10):#this means it will loop through the range without including 10 and it will start with 0
    print(num)
print("----------------------------------")
for num in range(5,12,2):#the first argument is starting point while the 2nd argument is till that point but not including
    print(num)           #the third argument is the step size
print("----------------------------------")
mynum=[1,2,3,4,5]
words=['hello','my','name','is','atul']
games=['cricket','badminton','khoko','football']
for zipper in zip(mynum,words,games):#the multiple data can be zipped and iterated together this will zip the data till all the contents are present
    print(zipper)
print("----------------------------------")
for item in enumerate(words,1):#the second argument 1 here defines that the enumeration will start from 1
    print(item)
print("----------------------------------")
zipped_list=zip(mynum,words,games)
for a,b,c in zipped_list:
    print(a)
    print(c)
    print(b)
print("----------------------------------")   
print(2 in mynum)#the in method is used to check whether a value exist in a list or dictionary
                #in dictionary it only checks for the key and not for the value
print(140 in {'john':140}.values())#by this we can check the values in a dictionary
print(max(mynum))#this returns the maximum value in a list