import os
#Start Program

class Snake:
    name = ""
    size = int()
    age = int()

def function1():
    Snake.name = input("Whats the snakes name? ")
    Snake.age = int(input("What the Snakes age? "))
    Snake.size = int(input("Whats the snakes size in cm?? "))
    os.system('clear')

def function2():
    print(f"The Snakes name is: {Snake.name}")
    print(f"The Snakes size is: {Snake.size}")
    print(f"The Snakes age is: {Snake.age}")

function1()
function2()


