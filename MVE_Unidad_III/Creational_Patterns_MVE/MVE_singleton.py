"""Maribel Vargas Exiga"""
"""GITI9072-e"""
"""Example Creational Patterns"""

class Borg:
    """ Borg class making class attribues global"""
    _shared_state = {} # Attribute dictionary

    def __init__(self):
        self.__dict__=self._shared_state # Make it an attribute dictionary

class Singleton(Borg): #Inherits from the Borg class

    def __init__(self, **kwargs):
        Borg.__init__(self)

        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribue dictionery for printing
        return str(self._shared_state)

#Let´s create a singleton object and add our first acronym
x = Singleton(HTTP ="Hyper Text Tansfer Protocol")
#Print the objec
print(x)

#Let´s creae a singleton object and if it refers to the same attribute dictionary by adding anoher acronym
y = Singleton(SNMP = "Simple Network Management Protocol")
print(y)