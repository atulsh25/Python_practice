class PartyAnimal :
    x=0
    def __init__(self,nam):
        self.name=nam
        print(self.name,"The object is constructed")
    def party(self):
        self.x = self.x + 1
        print(self.name,"Self.x so far is ",self.x)
    def __del__(self):
        print("The object is destructed with value ",self.x)

class FootBallFan(PartyAnimal):
    points=0
    def touchdown(self):
        self.points=self.points+7
        self.party()
        print(self.name,"points: ",self.points)

s=PartyAnimal("Sally")
s.party()

j=FootBallFan("Raman")
j.touchdown()
j.party()
