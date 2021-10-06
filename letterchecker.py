

# class vowel_checker:
    
#     def __init__(self):
#         self.vowels = ['a', 'e', 'i', 'o', 'u']


#     def checking(self, h ):
#         if h in self.vowels:
#             print("true")
#         else:
#             print("false")


# wordchecker = vowel_checker()

# print(wordchecker.checking('o'))


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



####### earls method

# class CharacterTest():
  
#   def __init__(self, testString):
#     self.testString = testString
  
#   def testMethod(self, var1):
#     return var1.upper() in self.testString

# straightLines = CharacterTest("AEFHIKLMNTVWXYZ")
# curvedLines = CharacterTest("COS")
# straightAndCurvedLines = CharacterTest("BDGJPQRU")
# noEndpoints = CharacterTest("BDO")
# twoEndpoints = CharacterTest("ACGIJLMNQRSUVWZ")
# threeEndpoints = CharacterTest("EFTY")

# print(straightLines.testMethod("a"))
# print(straightLines.testMethod("q"))
# print(straightLines.testMethod("w"))
# print(curvedLines.testMethod("c"))
# print(curvedLines.testMethod("o"))
# print(curvedLines.testMethod("t"))
# print(straightAndCurvedLines.testMethod("c"))
# print(straightAndCurvedLines.testMethod("b"))
# print(straightAndCurvedLines.testMethod("r"))
# print(noEndpoints.testMethod("r"))
# print(noEndpoints.testMethod("g"))
# print(noEndpoints.testMethod("b"))
# print(twoEndpoints.testMethod("a"))
# print(twoEndpoints.testMethod("q"))
# print(twoEndpoints.testMethod("b"))
# print(threeEndpoints.testMethod("b"))
# print(threeEndpoints.testMethod("e"))
# print(threeEndpoints.testMethod("z"))