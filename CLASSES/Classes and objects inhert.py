
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("HI iam ", self.name, "and i am", self.age, 'years old')

    def talk(self):
        print('Bark!')

# Dog is superclass

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)     #<--- auto inherit from Dog because of (Dog)
        self.color = color

    def talk(self):
        print('meow')       # whatever goes in the subclass it will override the DOG 
                            # class


tim = Cat('tim', 5, 'blue')        
tim.speak()

jim = Dog('jim', 70)
jim.talk()




