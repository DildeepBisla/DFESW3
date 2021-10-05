
# def greet():
#     name = input("What is your name? ")
    
#     print(f"Hello {name}")

# greet()

#####

# def greet(name):
#     return f"Hello {name}"

# name = input("What is your name? ")
# print(greet(name))

#####

# def greet(name, greeting="Hello"):
#     return f"{greeting} {name}"

# print(greet("Steve"))  # Prints "Hello Steve"
# print(greet("Bill", "Hola"))  # Prints "Hola Bill"

#####

# def add_calc(number1, number2):
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)

#####

# def mark(hwM,asM,esM):
#     hwM = (hwM / 25) * 100 #Get homework as a percentage
#     asM = (asM / 50)*100 #Get assignment mark as a percent
#     return((hwM+asM+esM)/3) #Average them out


# def grade(intMark):
#     if intMark >= 80: #Checks the input to see what grade it'd equate to
#         return("A")  #If grade is below 50, it's a fail.
#     elif intMark >= 70:
#         return("B")
#     elif intMark >= 60:
#         return("C")
#     elif intMark >=50:
#         return("D")
#     else:
#         return("Fail")


# studName = input("Please enter your name: ")
# intHomework = int(input("Please enter your homework mark out of 25: "))
# intAssignment = int(input("Please enter your Assignment mark out of 50: "))
# intExamScore = int(input("Please enter your exam score out of 100: "))
# #Get my stuff


# while intHomework >25 or intHomework < -1:
#     intHomework = int(input("Please enter a homework mark between 0 and 25: "))
# while intAssignment >50 or intAssignment < -1:
#     intAssignment = int(input("Please enter your Assignment mark between 0 and 50: "))
# while intExamScore > 100 or intExamScore < -1:
#     intExamScore = int(input("Please enter an exam score between 0 and 100: "))


# #Making sure the input is in the correct range.
# intICTMark = round(mark(intHomework,intAssignment,intExamScore)) #Rounds the result from mark to get rid of the decimal.
# intGrade = grade(intICTMark) #generates the grade based on mark
# print(f"{studName}, your overall mark is {intICTMark} graded at a {intGrade}") #Pretty output for the user




#####


#######

# def grade():

#     name = input("Name: ")

#     homework_score = int(input("Homework Mark: "))  

#     if homework_score > 25 or homework_score < 0:

#         print("Error: homework score is out of 25")

#         quit()

#     assessment_score = int(input("Assessment Mark: ")) 

#     if assessment_score > 50 or assessment_score < 0:

#         print("Error: assessment score is out of 50")

#         quit()

#     final_exam_score =  int(input("Final Exam Mark: "))

#     if final_exam_score > 100 or final_exam_score < 0:

#         print("Error: final exam score is out of 100")

#         quit()

#     total_score = int((homework_score + assessment_score + final_exam_score)/175*100)

#     return f"Student Name: {name}, Final Grade: {total_score}%"



# print(grade())


