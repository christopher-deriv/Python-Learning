## functions (def) are essentially code you want to reuse in a script or code block multiple times

def hello(name):
    print(f"Hello {name}!")

hello("John")

def add_numbers(num1,num2):
    print(num1 + num2)
add_numbers(4,8)

def dog_info(name,age):
    print(f"Hello my dog's name is {name}, he is {age} years old")
dog_info("Ziggy",12)