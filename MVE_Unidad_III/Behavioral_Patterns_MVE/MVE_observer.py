"""Maribel Vargas Exiga"""
"""GITI9072-e"""
"""Example Behavioral Patterns"""

class Subject(object): #Represents what is being 'observed'

    def __init__(self):
        self._observers = []

    def attach(self, observer):
        if observer not in self._observers: #If the observer is not already in the observers list
            self._observers.append(observer)#append the observer to the list

    def detach(self, observer): #Simply remove the observer
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:#For all the observers in he list
            if modifier != observer:# Don't notify the observer who is actually updating the temperature
                observer.update(self)# Alert he observers!!

class Core(Subject): #Inherits from the subject class

    def __init__(self, name=""):
        Subject.__init__(self)
        self._name = name #Set the name of the core
        self._temp = 0 #Iniialize the temperature of he core

    @property #Getter thet gets the core temperature
    def temp(self):
        return self._temp

    @temp.setter #Setter that sets he core temperature
    def temp(self, temp):
        self._temp = temp

class TempViewer:

    def update(self, subject):
        print("Temperature Viewer: {} has temperature {}".format(subject._name, subject._temp))

#Let's create our subjects
c1 = Core("Core 1")
c2 = Core("Core 2")

#Let's create our observers
v1 = TempViewer()
v2 = TempViewer()

#Let's attach our observers o the first core
c1.attach(v1)
c1.attach(v2)

#Let's change the temperature of our first core
c1.temp = 80
c1.temp = 90


