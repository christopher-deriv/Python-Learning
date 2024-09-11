# Just telling the script to expect 3 inputs 
iterations = int(input("Enter iterations: "))
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

# This is the function to do a comparison between the two numbers. arg in this instance are being used as placeholders so they don't ncessarily represent any value but it's letting you know that if you call on the function bigger then it will require that many arguements
def bigger(arg1, arg2):
    if arg1 > arg2:
        return arg1
    elif arg2 > arg1:
        return arg2
    else:
        return arg1

# In this instance "count" works as a placeholder just to initialize the loop, it will start at 0 and loop over however many times you set after in. In this case you're using the input from interations to determine how many times to loop
for count in range(iterations):
    # here you are taking the 2 numbers given in the first input and subsequent loops to determine which is the bigger of the two by utilizing the function created earlier
    number_to_divide = bigger(num1, num2)
    # Now you have a simple if statement to stop the loop if either number is lower than 2
    if num1 < 2 or num2 < 2:
        break
    # At this point it will divide whichever number is larger of the two by 2
    number_to_divide/=2
    # And in this if else loop it will determine which of the two numbers needs to be passed back to the top of the loop (line 17) to be divided
    if num1 > num2:
        num1 = number_to_divide
    else:
        num2 = number_to_divide
    # This will have it print each time it loops though and to print out the number after it was divded by 2.
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