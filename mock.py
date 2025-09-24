number = int(input("Enter your number:")) #allows user to enter a number
def odd_even():
"""
This function checks if the input is even or odd

"""
    if number() % 2 = 0 #checks if the function even
        print("this number is even")
    else:
        print("this number is odd") #checks if the function is odd
def negative_positive():
"""

This function checks if the input is a negative or positive number

"""
    if num < 0: #checks if the number is negative
        print("This number is negative")
    elif num > 0: # checks if a number is positive
        print("This number is positive")
    else: #if the previous statements are not satisfied then the following will be printed
        print("The number is equal to 0")
def square():
"""

This function gives the square root of the input given

"""
    square_num  = num * num # gives the square of the number
    print("The square of this number is", square_num)
def cube():

"""
This function gives nthe cubic root of the input given

"""
cube_num = num * num * num #gives the cube of the number
print("The cube of this number is", cube_num)
def main():
    odd_even()
    negative_positive()
    square()
    cube()
    