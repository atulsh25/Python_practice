def test(num):
    if num<10:
        print('Number less than 10')
        return num*2
    elif num==10:
        print('Number is 10')
        return num/2
    else:
        print('Number is greater than 10')
        return num
print('First Function')
print('Result is here',test(8))
#print(type(num))