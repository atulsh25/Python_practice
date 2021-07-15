animals=['goat','cow','lion','tiger','giraffe']
j=0;
for i in animals:
    j+=1
    print(str(j)+" "+i+" is an animal")
print('-----------------------------------------------------')
sentence="Hello ji Namaste"
for k in sentence:
    if k==' ':
        continue
    print(k)
print('-----------------------------------------------------')
#for a for loop to compile without a purpose the "pass" keyword will be used for it
for i in range(1,6):
    pass
x=5
while x<10:
    print(x)
    x=x+1
else:
    print("nothing to loop anymore")
print('-----------------------------------------------------')
employees={'mike':27000,'john':80000,'rohan':100000}
for key in employees:
    print(key)
print('-----------------------------------------------------')
#thus for getting the values associated with the dictionary we should use .items()
for i in employees.items():
    print(i)
print('-----------------------------------------------------')
for i in employees.keys():#just for the keys
    print(i)
print('-----------------------------------------------------')
for i in employees.values():#just for the values
    print(i)
print('-----------------------------------------------------')
for key,value in employees.items():#to get the keys and the values separately this is also called as unpacking
    print(key)
    print(value)
print('-----------------------------------------------------')
employees=[('mike',27000,27),('john',80000,25),('rohan',100000,26)]
for name,salary,age in employees:#while iterating through a list of tuples there is no need of .items() keyword
    print(name)
    print(salary)
    print(age)
    print()