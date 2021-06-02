#sort by keys
d={'a':1,'c':22,'b':4}
t=sorted(d.items())
for (a,b) in t:
    print(a,b)
print(sorted([(v,k)for (k,v) in d.items()]))
#sort by values in descending order
l=list()
for (k,v) in d.items():
    l.append((v,k))
print(sorted(l,reverse=True))