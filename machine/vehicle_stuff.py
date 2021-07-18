class Vehicle:
    color='blue'#this should not be changed as per the best practice to avoid error
    vehicle_counter=0
    def __init__(self,body_type,make):#initialization of a constructor
        self.vehicle_body=body_type#the self keyword here is pointing to the object being created
        self.vehicle_make=make
        Vehicle.vehicle_counter=Vehicle.vehicle_counter+1#this portion will be called when an object is instantiated
    def get_vehicle_count(self):
        return Vehicle.vehicle_counter
    def drive(self):
        print("Vehicle driving")
    #the reason that we have not used self here is because it is associated with that particular instance and not class as a whole
car1=Vehicle('Jeep','Toyota') #the object is created and are the instances of a class
print(car1.vehicle_body)
print(car1.vehicle_make)
print(type(car1))
car2=Vehicle('Truck','Mercedes')
print(car2.vehicle_body)
print(car2.vehicle_make)
print(car2.color)
print(Vehicle.vehicle_counter)
#Vehicle.color='green'#the way to change the value of the attribute of a class
#car1.color='yellow'#the attribute for an instance of a class can also be modified
class Truck(Vehicle):#here the truck class is inheriting the property of vehicle
    def drive(self):#here we are actually overiding the method of vehicle class
        print("Truck driving")
class Motorcycle(Vehicle):#here the truck class is inheriting the property of vehicle
    def drive(self):#here we are actually overiding the method of vehicle class
        print("Motorcycle driving")