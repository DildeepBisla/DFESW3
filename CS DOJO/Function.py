#>>>>>>>>>>>>>>              Function BASICS MATHS                     <<<<<<<<<<<<<#####

# used for mapping (maths)/(eqautions)
# used in input or an argument

#       def                       <<<--------- define
#       function name             <<<--------- function name
#       ()                        <<<--------- take argument eg. (x)
#       :                         <<<-------- closed line

#       return                    <<<-------- method of outcome
#       2*x                       <<<------- the actual maths 2 X x = function name

#       a = funtion name(what ever 'x' should be) <<<----- will return the answer

def function1(x):
    return 2*x
    
a = function1(3)
print(a)


# MORE EXAMPLES

def function2(x, y):
    return x + y

a = function2(2,3)
print(a)




######        BMI CALCULATOR        ######



name1 = 'dill'
height1 = 2 
weight1 = 115

def bmi_calculator(name, height, weight):
    bmi = weight / (height ** 2)

    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"

name2 = 'pazza'
height2 = 2
weigth2 = 65

dills_res = bmi_calculator(name1, height1, weight1)
print(dills_res)

pazzas_res = bmi_calculator(name2, height2, weigth2)
print(pazzas_res)




######## KM to miles ############

#   km = convert(miles)
#   km = 1.6 * miles

def km_to_miles_converter(miles):
    return 1.6 * miles


km = km_to_miles_converter(30)
print (km)


