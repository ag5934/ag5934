''' 
 Name: Aya Ghraizi
 ID: 414000196
 Section: 605

 '''
def triangle_validator():
    """
    This function Checks whether three given side lengths we input can form a valid triangle.

    the  triangle is valid only if the sum of the lengths of any two sides 
    is greater than the length of the third side.
    """
    side_A = int(input("Enter a value:")) # prompts user to enter values
    side_B = int(input("Enter a value:"))
    side_C = int(input("Enter a value:"))
    """
     Prompts the user to input three side lengths and prints whether 
    the shape is a triangle or not
    
    """
    if (side_A + side_B > side_C and side_A +side_C > side_B and side_B + side_C > side_A):
         print("The following shape is a valid triangle") #prints this statement if the if statement proves to be true
    else:
      print("The shape is not a valid triangle") #prints this statement if the if statement proves to be false
triangle_validator() #calls the function
     
