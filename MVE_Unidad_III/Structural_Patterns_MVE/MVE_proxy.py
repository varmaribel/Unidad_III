"""Maribel Vargas Exiga"""
"""GITI9072-e"""
"""Example Structural Patterns"""

import time

class Producer:
    """Defina the 'resource-intensive' object to instantiate!!"""

    def produce(self):
        print("Producer is working hard!!")

    def meet(self):
        print("Prodicer has time to meet you now")

class Proxy:
    """Define the 'relatively less resource-intensive' proxy to instantiate as a middleman"""
    def __init__(self):
        self.occupied = 'No'
        self.producer = None

    def produce(self):
        """Check if Prodecer is available"""
        print("Artist checking if Producer is available ...")

        if self.occupied == 'No':
            #If the producer is availble create a producer object!!
            self.producer = Producer()
            time.sleep(2)

            #Make the producer meet the guest
            self.producer.meet()
        else:
            #Otherwise, don't instantiate a producer
            time.sleep(2)
            print("Produce is busy!!")

#Instaniate a Proxy
p = Proxy()

#Make the proxy: Artist produce until Producer is available
p.produce()

#Change the state to 'occupied'
p.occupied = 'Yes'

#Make he Producer produce
p.produce()
