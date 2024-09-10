iterations = int(input("Enter iterations: "))
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

def bigger(arg1, arg2):
    if arg1 > arg2:
        return arg1
    elif arg2 > arg1:
        return arg2
    else:
        return arg1

for i in range(iterations):
    number_to_divide = bigger(num1, num2)
    if num1 < 2 or num2 < 2:
        break
    number_to_divide/=2
    if num1 > num2:
        num1 = number_to_divide
    else:
        num2 = number_to_divide
    print(number_to_divide)

# Solution provided by coddy.tech
# for i in range(iterations):
#     if num1 < 2 or num2 < 2:
#         break
#     big = bigger(num1, num2)
#     if big == num1:
#         num1 /= 2
#         print(num1)
#     else:
#         num2 /= 2
#         print(num2)