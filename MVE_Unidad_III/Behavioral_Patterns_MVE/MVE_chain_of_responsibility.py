"""Maribel Vargas Exiga"""
"""GITI9072-e"""
"""Example Behavioral Patterns"""

class Handler: #Abstract handler
    """Abstract Handler"""
    def __init__(self, successor):
        self._successor = successor #Define who is the next handler

    def handle(self, request):
        handled = self._handle(request) #If handled, stop here

        #Otherwise, keep going
        if not handled:
            self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError('Must provide implementation in subclass')

class ConcreteHandler1(Handler):
    """Concrete handler 1"""
    def _handle(self, request):
        if 0 < request <= 10: #Provide a conditio0n for handling
            print("Request {} handled in handler 1".format(request))
            return True #Indicates that the request has been handled

class DefaultHandler(Handler):

    def _handle(self, request):
        """If there is not handler available"""
        #No condition checking since this is a default handler
        print("End of chain, no handler for {}".format(request))
        return True #Indicates that the request has been handled

class Client: #Using handlers
    def __init__(self):
        self.handler = ConcreteHandler1(DefaultHandler(None)) #Create handlers and use them in a sequence you want

    def delegate(self, requests):
        for request in requests:
            self.handler.handle(request)


#Create a client
c = Client()

#Creae requests
requests = [2, 5, 30]

#Send the requests
c.delegate(requests)