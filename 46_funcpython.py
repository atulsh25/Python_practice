def greet_person(jibberish="Default user"):#default value can be assigned to a function
    '''
    DOCSTRING: this returns a greeting
    INPUT:jibberish
    OUTPUT:Hello ... name
    '''
    print("Hello ji ")
    print("Hello this is "+jibberish)
def remainder(a,b):
    return a%b
print(remainder(10,3))
greet_person()
def mysum(*args):#*args gives the capability to a function to pass multiple parameters without the need of defining them
    return sum(args)
print(mysum(1,2,3,4,5))
def myfunc(**kwargs):#*kwargs gives the capability to a function to pass multiple parameters
                    # without the need of defining them as a key value pair
    print(kwargs)
myfunc(name="Atul",weight=80)
def age_variance():
    age=44
    def reduce_age_by_20(age):
        age=age-20
        print("Nested method age: "+str(age))
    reduce_age_by_20(age)
age_variance()