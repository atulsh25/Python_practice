friends=['Akash','Amit','GG']
for friend in friends :
    print( 'Hello ' , friend )
print('Done with loops')
num=[10,51,84,72,66,4]
smallest_number=None
for i in num:
    if smallest_number is None:
        smallest_number=i
    elif i<smallest_number:
        largest_number = i
print('The smallest number is ',smallest_number)