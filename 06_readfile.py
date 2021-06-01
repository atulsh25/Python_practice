try :
    fhand=open('/home/atul/Documents/RUST_PROJECT/mbox.txt')
    count=0
    for line in fhand :
        count+=1
        print(line.lower())
        print(line.upper())
        print(line.strip())
        print(len(line))
        print(line)
        if line.startswith('My'):
            line=line.rstrip()
            print(line,'Found')
except :
    print('Not able to open the file')
    quit()
print('Done with reading')
print('Number of lines is' , count)