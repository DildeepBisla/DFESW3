# Tutorial

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# John = Student("John", "21")
# Jane = Student("Jane", "22")

# print(getattr(John, "age"))

####


# class Student:

#     def __init__(self, name, age, class_ = "student"):
#             self.name = name
#             self.age = age
#             self.class_ = class_


#     def test_scores(self, res1, res2, res3):
#         avgscore = (res1 + res2 + res3) / 3
#         print(int(avgscore))


# student1 = Student("dill", 33)

# student1.test_scores(25,33,47)


#####


class vowel_checker:
    
    def __init__(self):
        self.vowels = ['a', 'e', 'i', 'o', 'u']


    def checking(self, h ):
        if h in self.vowels:
            print("true")
        else:
            print("false")


wordchecker = vowel_checker()

print(wordchecker.checking('o'))


##### stewarts code

# class Letters:
    
#     #vowels ='aeiou'#vowel attribute
    
#     def __init__(self):# I dont need vowels to be in this 
#         self.vowels = ['a','e','i','o','u']
    
    
#     def vowelcheck(self,x):
#         if x.isalpha() and x in self.vowels:
#             return "True,Its a vowel"
#         elif x.isalpha() and x not in self.vowels:
#             return "False,Its not a vowel"
#         else: False

# #creating object

# word = Letters()
# print(word.vowelcheck('a'))


##### leon method

# class Letterchecker():
#     vowels = 'aeiou'
    
#     def checkthing(self,x):
#         return x.lower() in self.vowels

# vowlchecker = Letterchecker()

# for i in 'thequickbrownfoxjumpedoverthelazydog':
#     print(vowlchecker.checkthing(i))

