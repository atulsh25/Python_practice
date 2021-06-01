n=5
while n>0 :
    print(n)
    n=n-1
print(n)
print('Blastoff')
while True :
    line = input('>')
    if line[0]=='#' :
        continue
    if line =='done':
        break
    print(line)
print('Done')