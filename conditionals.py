
#\

# devs_money = 100
# dev_can_play_smash = False

# if devs_money > 10 and dev_can_play_smash:
#     print("Dev enters a smash tournament!")

# elif devs_money < 10 and dev_can_play_smash:
#     print("Dev is too poor to enter")    

# else:
#     print("Dev just can't play smash")


#\

# usermark = int(input("Enter Mark: "))

# if usermark >= 85:
#     print("Distinction") 

# elif usermark >= 65 and usermark < 85:
#     print("pass")

# else: 
#     print ("fail")

#\





#\ LOOPS

# FOR LOOPS

# stringVar = '011100010010'

# for intvar in stringVar:
#     if int(intvar):
#         print('this is false')

#     else:
#         print('This is true')



#\\\




# stringVar = 'this is a string'

# for teststringvar in stringVar:
#     if teststringvar == 't':
#         print('this is a TEEEE')

#     else:
#         print('This is not')



#\\\




# for numVar in  range(0, 100, 7):
#     print(numVar)

# \ ^ used in a 7 times table format





#\\\



# my_fruit = ["Apple", "Banana", "Orange", "Pear", "Grape", "Berry"]

# for fruit in my_fruit:
#     # add if statements here (optional)
#     print(fruit.upper())








#\\\

# WHILE LOOPS

# inputNumbVar = int(input('Enter NUmber: '))

# resultVar = 1

# while inputNumbVar > 0:
#     resultVar= resultVar * inputNumbVar
#     inputNumbVar = inputNumbVar - 1
#     print(resultVar)



#\


# userinput = int(input('Enter Number: '))

# usercode =+ 3

# while userinput > 0:
#     userscore = usercode * userinput
#     print(userscore)
#     break

#\

# for i in range(3):
#     for j in range(4):
#         print(i, "x", j, "=", i * j)


#\


# count = 0
# name = str(input("What is your name? "))

# while count < 5:
#     print(name, "is awesome! ")
#     count += 1


#\


# for i in range(5, 11):
#     print(i)


#\
#
#


# while True:
#     name = str(input('Entername Here: '))
#     print(name + " " + "is awesome!")
#     break
    

#
#\
#

#JORDANS EXAMPLE

# names = 0

# while names < 5:

#     name = input("Please enter a name: ")

#     print(name + " Is awesome!")

#     names = names + 1


#AMELIA

# userString = input("Please type a word here. ")
# reverseString = userString[::-1] #this reverses the order of a word
# if reverseString == userString:
#     print("This is a palindrome! Conrats!")
# else:
#     print("This word is not a palindrome.")

#    

# userinput = str(input('Enter Input: '))
# inputlength = len(userinput) 
# #print(inputlength)

# reversestring = userinput[::-1]
# #print(reversestring)

# if userinput == reversestring:
#     print("this is a palindrome")
# else:
#     print("this is not palindrome ") 

#\
# 
# 
#     

#Paul Randalls#

# string = input("Provide potential palindrome: ").lower()

# revstring = ""

# for i in range (len(string)):

#     revstring = revstring + string[-1-i]

# if revstring == string:

#     print("Palindrome provided")

# else:

#     print("Not a palindrome")

#Leon#

# palinVar = input('TYPE IN: ')
# numChars = len(palinVar) - 1
# raVnilap = ''
# while numChars >= 0:
#     raVnilap = raVnilap  + palinVar[numChars]
#     numChars = numChars - 1
# if raVnilap == palinVar:
#     print('PALINDROME')
# else:
#     print('no')


########

