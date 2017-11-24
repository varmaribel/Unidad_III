"""Maribel Vargas Exiga"""
"""GITI9072-e"""
"""Example Structural Patterns"""

from functools import wraps

def make_blink(function):
    """Defines the decorator """

    #This makes the decorator transparent in terms of its name and docstring
    @wraps(function)

    #Define he inner function
    def decorator():
        #Grab the return value of the fucntion being decorated
        ret = function()

        #Add new functionality to the function being decorated
        return "<blink>" + ret + "</blink>"

    return decorator

#Apply the decorator here!
@make_blink

def hello_world():
    """Original function!!"""
    return "Hello, world"

#Check the resilt of decorating
print(hello_world())

#Check if the function name is still the same of the function being decorated
print(hello_world.__name__)

#Check if the docstring is still the same as that of he function being decorated
print(hello_world.__doc__)