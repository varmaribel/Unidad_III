"""Maribel Vargas Exiga"""
"""GITI9072-e"""
"""Example Creational Patterns"""

class Dog:
    """One of he objects o be returned"""

    def speak(self):
        return "Woof!!"

    def __str__(self):
        return "Dog"

class DogFactory:
    """Concrete Factory"""

    def get_pet(self):
        """Returns a Dog object"""
        return Dog()

    def get_food(self):
        """Return a Dog Food object"""
        return "Dog Food!"

class PetStore:
    """ PetStore houses our Abstrac Factory"""

    def __init__(self, pet_factory=None):
        """ pet_factory is our Abstract Factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """ Utility method to display the details of the objects returned by dogFactory"""

        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print("Our pet is '{}'!".format(pet))
        print("Our pet says hello by '{}'!".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

#Create a Concrete Factory
factory = DogFactory()

#Create a pet store housing our Abstract Factory
shop = PetStore(factory)

#Invoke the utility method to show the details of our pet
shop.show_pet()
