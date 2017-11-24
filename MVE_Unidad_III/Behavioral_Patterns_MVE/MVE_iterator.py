"""Maribel Vargas Exiga"""
"""GITI9072-e"""
"""Example Behavioral Patterns"""

def count_to(count):
    """Our iterator implementation"""

    #Our list
    numbers_in_german = ["eins", "swei", "drei", "vier", "funf"]

    #Our built-in iterator

    #Creates a tuple such as (1, "eins")
    iteator = zip(range(count), numbers_in_german)

    #Extract the German numbers
    #Put them in a generator called number
    for position, number in iteator:

        #Returns a 'generator' containing numbers in German
        yield number

 #Let's test the generator reurned by our iterator
for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))