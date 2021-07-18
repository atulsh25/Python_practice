class Employee:
    def __init__(self,name,age):
        self.emp_name=name
        self.emp_age=age
    def __str__(self):#this dunder method automatically invokes the string data
        return self.emp_name+" the age is "+str(self.emp_age)

tom=Employee('Tom',47)
print(tom)