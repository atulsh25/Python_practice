import urllib
count=dict()
fhand=urllib.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    words=line.decode().split()
    for word in words:
        count[word]=count.get(word,0)+1
print(count)