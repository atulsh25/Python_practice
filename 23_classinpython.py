class PartyAnimal :
    x=0
    def __init__(self):
        print("The object is constructed")
    def party(self):
        self.x = self.x + 1
        print("Self.x so far is ",self.x)
    def __del__(self):
        print("The object is destructed with value ",self.x)
an=PartyAnimal()
an.party()
an.party()
an.party()
an=42#this is the point where the destructor will be called as the existence of object is destroyed
print(an)