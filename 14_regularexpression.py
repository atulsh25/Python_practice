import re
hand=open('mbox.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^I am',line):
        print(line)
x='My 2 favourite numbers are 9 and 1200'
z='From: Using: the character'
w=re.findall('^F.+:',z)
v=re.findall('^F.+?:',z)
print('Greedy result ',w)
print('Non Greedy result ',v)
y=re.findall('[0-9]+',x)
print(y)
data='From stephen.maquard@uct.ac.za Sat Jan 5 09:14:16 2008'
a=re.findall('^From (\S+@\S+)',data)
b=re.findall('From .*@([^ ]*)',data)
print(a)
print(b)