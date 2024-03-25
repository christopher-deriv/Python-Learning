# dynamic_input will determine the number of integers/inputs to accept
dynamic_input = int(input())
res = 0
# in here the variable "numbers" is used to store the # of times it will loop through the code
for numbers in range(dynamic_input):
    #there is another nested input function as once you input how many inputs you will make in "dynamic_input = int(input())" here you then input the individual numbers you want to be added up
    add_numbers = int(input())
    res += add_numbers
print(res)