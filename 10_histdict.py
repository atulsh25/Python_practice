histogram=dict()
names=['csev','ccc','cwen','zqian','ccc','cwen','csev','cwen','zqian']
for name in names:
        histogram[name]=histogram.get(name,0)+1
print(histogram)