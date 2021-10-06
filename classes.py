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
        return (res1 + res2 + res3) / 3

student1 = Student("dill", 33)


result_dill = dillon.test_scores(25,33,47)
print(result_dill)

