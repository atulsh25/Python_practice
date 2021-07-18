try:
    with open('sample2.txt',mode='w+') as myfile:
        myfile.write("\nHello Ji")
        print(myfile.read())
        2+'2'
except FileNotFoundError:#this is a general way to catch all error
    print("The file was not found")
except TypeError:
    print("Type mismatch encountered")
except:
    print("Error of general scenario")
finally:
    print("This will run regardless of anything")
print("this program ran")