import sys
print(sys.argv[1]+" age is "+sys.argv[2])#0th argiment is the fle name
list_data=sys.argv[1:]#this is for unlimited argument
for arg in list_data:
    print(arg)