#testscores calc.

def test_grade():
    total = hwm + asm + exm
    answer = (total / 175) * 100
    return answer

name = str(input("Enter Name: "))

hwm = int(input("Enter Homework Socre: "))
while hwm > 25:
    print("Invalid Entry")
    hwm = int(input("Enter Homework Score: "))

asm = int(input("Enter Assessment Score: "))
while asm > 50:
    print("Invalid Entry")
    asm = int(input("Enter Assessment Score: "))

exm = int(input("Enter Exam Score: "))
while exm > 100:
    print("Invalid Entry")
    exm = int(input("Enter Exam Score: "))

avgtestgrade = round(test_grade())

print(f"{name}, {avgtestgrade}%")

