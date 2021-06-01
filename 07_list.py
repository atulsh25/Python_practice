num_range=[55,33,122,10,25,6]
for i in range(len(num_range)):
    print(num_range[i])
print('The content of the list are as above')
print(sum(num_range))
x=list()
x.append('Atul')
x.append('Akash')
x.append('Amit')
x.sort()
print('The content of the list',x)
x.pop()
print('The new content of the list',x)
names_are='Sonu Rehman Satish'
name_list=names_are.split()
print(name_list)