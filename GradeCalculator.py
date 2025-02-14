# 2. Grade Calculator
# -------------------------------
# • Create a function calculate_grade that takes a list of scores as input.
# • The function should calculate the average score and return the corresponding
# letter grade (e.g., A, B, C, D, F) based on a grading scale.


# Function Definition
def calculate_grade(inp):
    Total = sum(inp)
    avg = Total / len(inp)
    final = round(avg, 2)
    if avg > 90:
        grade = "A"
    elif 80 < avg <= 90:
        grade = "B"
    elif 65 < avg <= 80:
        grade = "C"
    elif 50 < avg <= 65:
        grade = "D"
    elif 35 < avg <= 50:
        grade = "E"
    else:
        grade = "F"
    return f"Your Average Marks: {final}, Grade: '{grade}'"


lst = input("Enter Your marks in 6 subjects out of 100 Separated by space:").split(" ")
if len(lst) == 6:
    scores = []  # Create an empty list to store integer values
    for mark in lst:
        scores.append(int(mark))  # Convert each input to an integer
    result = calculate_grade(scores)
    print(result)
else:
    print("please enter your 6 Subject Marks Separated by space")

# --------------------------------------------------------------------------------------
# Not Taking Values from Function Calling but returning values
# ----------------------------
# def sum():     # function Definition
#     a=int(input("a :"))
#     b=int(input("b :"))
#     c=a+b
#     return c   # function Calling

# result=sum()
# print(result)


# Not Taking Values from Function Calling not returning values
# ----------------------------
# def sum():
#     a=int(input("a :"))
#     b=int(input("b :"))
#     c=a+b
#     print(c)
#
# sum()


# Taking Values from Function Calling not returning values
# ----------------------------
# def sum(a,b):
#     c=a+b
#     print(c)
#
# m=int(input("a :"))
# n=int(input("b :"))
# sum(m,n)


# Taking Values from Function Calling and returning values
# ----------------------------
# def sum(a,b):
#     c=a+b
#     return c
#
# m=int(input("a :"))
# n=int(input("b :"))
# result=sum(m,n)
# print(result)
