import os
lol = False

while(lol == False):
    try:
        x = int(input("Whats x? "))
        lol = True
    except ValueError:
        print("Please put in a whole Number")

lol = False

while(lol == False):
    try:
        y = int(input("Whats y? "))
        lol = True
    except ValueError:
        print("Please put in a whole Number")

def compare():
    if(x > y):
        print("X is bigger")

    else:
        print("Y is bigger")

compare()