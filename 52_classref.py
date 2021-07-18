from machine.vehicle_stuff import Vehicle,Truck,Motorcycle #from is the source basically foldername.filename import classname
                                          #the property of the class we want to inherit
car1=Vehicle('Jeep','Toyota') #the object is created and are the instances of a class
print(car1.vehicle_body)
print(car1.vehicle_make)

truck1=Truck("Big Rig","Mercedes")
truck2=Truck("Small Big","Chevy")
truck3=Truck("Big Rig","Toyota")
moto=Motorcycle("Kawasaki Ninja","Honda")

print(truck3.get_vehicle_count())
for i in [car1,truck3,moto]:
    i.drive()
