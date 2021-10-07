# #created a list
# a = [3, 10, -1]
# print (a)

# #append list
# a.append (1)
# print (a)

# #delete items in list
# a.pop (1)
# print (a)

# #index number
# a [0]
# print(a[0])     # prints number 3 and so on

# txt = "hello world"       #index of the charaters in the string
# x = txt[0]
# print(x)

# x = txt[2:5]                #to set range from:to characters
# print(x)

##########
##########
##########

# b = ["banana", "apple", "microsoft"]

#### using index keyword

# i = b.index("banana")
# # b[0] = "orange"      <---- we assigned b list and selected index positon and changed to orange 
# print(i)                  # so banana is at index 0

# i = b.index("microsoft")
# print(i)                  # so microsoft is at index 2

#### using count keyword

# i = b.count("banana")
# print(i)           # need to specify the item that is required for "count()" in the ()

##### using len keyword

# print(len("apple"))       # prints the length of the string/int
# print(len(b))             # prints the length of the string/int/list

##### using list keyword 

# print(list(b))      #shows the items in the list or array

# = list(stringvariable) <---- to convert string into list


#######             RANGE               ##########

# numb_list = [1,2,3,4,5,6,7,8,9,10]

# x = numb_list[3:7]
# print(x)

          # in this method x variable is going represent the range in the numb_list
          # and pull the numbers from index 3 to 7 

# x = range(6)        #<---- range is to 6 (no list used just range is auto generated) 
# for n in x:         #<---- n is just letter assinged to the iteration in the range 
#   print(n) 

#         # so x is the varibale, its going to have a range of auto populated iteration 
#         # to 6.  n is going to pull the iteration in x till it hit 6 iteration.  



######      Making Dictionaries         #######

#               Dictionaries are defined using { : }, as shown below.

#       noises = {"cow" : "moo", "sheep" : "baa"}
