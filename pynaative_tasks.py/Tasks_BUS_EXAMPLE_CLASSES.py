
#######         CREATING CLASSES     #########

# class Vehicle():
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage

# Vehicle_object_1 = Vehicle(250, 12000)

# print (Vehicle_object_1.max_speed)



######          SUBCLASSES          ######


# class Vehicle():
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# # Create a Bus object that will inherit all of the variables 
# # and methods of the Vehicle class and display it.

# class Bus(Vehicle):
#     pass 

# Shcool_Bus = Bus('School Bus', 180 , 12)

# print(Shcool_Bus.name, Shcool_Bus.max_speed, Shcool_Bus.mileage)




#####           INHERITANCE         ########


# class Vehicle():
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     # created a definition/method for seating capcity for all vehicles to 
#     # and its subclass

#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"

# # Using the seating_capacity method under Vehicle, the Bus class can inherit the 
# # method and be set to default value with = 


# class Bus(Vehicle):
#     def seating_capacity(self, capacity = 50):
#         return super().seating_capacity(capacity = 50)

# Shcool_Bus = Bus('School Bus', 180 , 12)
# print(Shcool_Bus.seating_capacity())





#######     Default CLASS VARIABLES         ####





# The class variable is shared between all class instances. You can define a class 
# attribute by assigning a value to a variable name outside of .__init__().


#### so to give the objects releated to the class the same value of an attribute the,
#### attribute will be put directly into the class as an attribute with a value




# class Vehicle():
#     color = 'White'

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

    

# class Bus(Vehicle):
#     pass

# class Car(Vehicle):
#     pass


# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

# car = Car("Audi Q5", 240, 18)
# print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)






##########        Class Inheritance   - CHILD CLASSES  #######

# class Vehicle:


#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity



#     def fare(self):
#         return self.capacity * 100



# # super() refers to super method argumunt, eg. fare is the super method, 
# # so super() dot method is calling the method as default.

# # below example shows varibale 'amount' to be equal to super method 'fare' and then 
# # we can apply the maths to it.  

# # we are now asking super method 'fare' to be used in 'amount' to be "added" back to 
# # the value of amount and then be multiplied and divided ( for percentage ) amd then
# # return a value for method (this is also overriding the method 'fare' - but only 
# # applying to "BUS" class)


# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount += amount * 10 / 100
#         return amount


# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())





##########



