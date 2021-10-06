

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

