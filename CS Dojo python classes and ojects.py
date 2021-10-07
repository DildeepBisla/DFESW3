
class Robot:
    
    def introduce_self(self):
        print("My name is " + self.name)

r1 = Robot()
r1.name = "Tom"
r1.color = "Red"
r1.weight = 30

r2 = Robot()
r2.name = "Jerry"
r2.color = "blue"
r2.weight = 20

r1.introduce_self()
r2.introduce_self()

#####
#####
#####


class Robot:

    def __init__(self, name, color , weight):
        self.name = name
        self.color = color
        self.weight = weight
    
    def introduce_self(self):
        print("My name is " + self.name)

    def display_all(self):
        print (self.name, self.color, self.weight)    


r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 20)

r1.introduce_self()
r2.introduce_self()

r1.display_all()



# class Person:

#     def __init__(self, name, personality, is_sitting):
#         self.name = name
#         self.personality = personality
#         self.is_sitting = is_sitting

#     def sit_down(self):
#         self.is_sitting = True

#     def standing_up(self):
#         self.is_sitting = False

# p1 = Person ("Alice", "Aggro", False)
# p2 = Person ("Becky", "sweet", True)   



