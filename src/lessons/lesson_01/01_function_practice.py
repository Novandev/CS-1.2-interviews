#1. Create a variable called global_food
#This variable is a string which represents a well known
#food globally

global_food = "Spinach"
#2. Create a function called print_foods which takes in 
#string called local_food which represents a more local
#food not as well known globally
local_food = "Avocado"

def print_foods(local_food):
    """
    Returns  the name of a food based on the input

    Parameters
    ----------
    local_food : The string to print.
    

    Returns
    ----------
    String
        The food returned from the string.
    """

    return local_food
#3. Have your function print out something about each food

#Label the varible scope in the comments

print(print_foods(global_food))
