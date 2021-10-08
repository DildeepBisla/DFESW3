
#######             RANGE               ##########

# numb_list = [1,2,3,4,5,6,7,8,9,10]

# x = numb_list[3:7]
# print(x)

          # in this method x variable is going represent the range in the numb_list
          # and pull the numbers from index 3 to 7 

# x = range(6)        #<---- range is to 6 (no list used just range is auto generated) 
# for n in x:         #<---- n is just letter assinged to the iteration in the range 
#   print(n) 

#      # so x is the varibale, its going to have a range of auto populated iteration 
#      # to 6.  n is going to pull the iteration in x till it hits 6 iteration.  













#######    Strings - REVERSE    #########


# txt = "Hello World"[::-1]      #<----- ::-1 will reverse the string (slicing)
# print(txt) 


######     String - REVERSE as a FUNCTION #######

# def str_reverse_func(x):
#   return x[::-1]

##>>>>>><<<<<<<<

# mytxt = str_reverse_func ("I wonder how this text looks like backwards")

# print(mytxt) 



###>>>>>>>>> list reverse as a FUNCTION >>>>>>>>>>>>>

# lst=[100,200,300,400,500]

# def f_1(list):
#     return list.reverse()             

 
 
# # .reverse() will reverse the variable/list/(thing) that its assinged to.







#######>>>>>>>>>>>>>>>>   using len keyword     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# b = ["banana", "apple", "microsoft"] 

# print(len("apple"))       # prints the length of the string/int
# print(len(b))             # prints the length of the string/int/list

# b = "apple"

# print(len(b))







#>>>>>>>>>>>>>>>>>>>>>>>>      Returning Default value    <<<<<<<<<<<<<<<<<<<<<<<<


# def defualt_val_func(x):
#     return 100

# # the return method always give the output of the return value.

# print(defualt_val_func (120))

####>>>>>>>>>>>>>>>>>>>     integer Value Return Func >>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def int_val_func(x : int):
#     return x 

# x = 120   

# print(int_val_func(x))



