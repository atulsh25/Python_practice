mynum=[1,2,3,4,5]
words=['hello','my','name','is','atul']
games=['cricket','badminton','khoko','football']
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
print("----------------------------------")
from random import randint
random_num=randint(0,1000)#this is the range from which the random number is picked
print(random_num)
print("----------------------------------")
from random import shuffle
shuffle(words)#this method is used to shuffle the contents of the list
print(words)
print("----------------------------------")
new_list=list(range(0,101))
shuffle(new_list)
print(new_list)