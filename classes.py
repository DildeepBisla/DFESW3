# Tutorial

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# John = Student("John", "21")
# Jane = Student("Jane", "22")

# print(getattr(John, "age"))

####


class Student:

    def __init__(self, name, age, class_ = "student"):
            self.name = name
            self.age = age
            self.class_ = class_


    def test_scores(self, res1, res2, res3):
        avgscore = (res1 + res2 + res3) / 3
        print(int(avgscore))

    def display_all(self):
        print(self.name, self.age, self.class_)   


student1 = Student ("dill", 25)

avgscore = student1.test_scores(25,33,47)

student1.display_all() 


#####
