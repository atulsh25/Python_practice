class Animal:
    def __init__(self,name):
        self.animal_name=name
    def eat(self):#this is basically an abstract method that it is declared but not defined
        raise NotImplementedError('Child class should be implementing the abstract method')
class Monkey(Animal):
    def eat(self):
        print('Monkey eats banana')
class Bird(Animal):
    def eat(self):
        print('Bird eats seed')
    def fly(self):
        print('Bird soar high')
myMonkey=Monkey("koko")
myMonkey.eat()
mybird=Bird('Jojo')
mybird.eat()
mybird.fly()