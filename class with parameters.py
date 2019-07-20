class Animal:
    def __init__(self, kind, place):
        self.kind = kind
        self.place = place

#This class inherits kind and place arguments from Animal class (which can work for any animal)
#Initiates a Dog object with name, gender and breed parameters.

class Dog(Animal):
    def __init__(self, name, gender, breed):
        self.name = name
        self.gender = gender
        self.breed = breed
        Animal.__init__(self, 'Dog', 'Ground')

    #woof method, just prints an action for the Dog object with his name. 
    def woof(self, *args):
        print("%s just did a %s woof" % (self.name, *args))

    #getallinfo method, get's all the parametrs of both classes.
    def getallinfo(self):
        print("%s is a %s %s %s, sitting on the %s" % (self.name, self.gender, self.breed, self.kind, self.place))

#Cat class inherits the paramets of use for a Cat (similar things) like name, gender and breed, which they both share, also the getallinfo method and initiate them. 
class Cat(Dog):
    def __init__(self, name, gender, breed):
        Dog.__init__(self, name, gender, breed)
        Animal.__init__(self, 'Cat', 'Ground')

#Speak method, returns a print for a cat "meow" with him name.
    def speak(self, *args):
        print("%s just did a %s meow" % (self.name, *args))

#Here I create 3 objects, 2 dogs and 1 cat with selected arguments.
#And check for some methods on the objects.
Mickey = Dog('Mickey', 'Male', 'Bulldog')
Flora = Dog('Flora','Female','Pug')
Tina = Cat('Tina','Female','Persian')
Tina.getallinfo()
Tina.speak('soft')
Dog.getallinfo(Flora)
Dog.woof(Mickey, 'loud')
