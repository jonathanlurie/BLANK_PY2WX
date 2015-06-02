"""
The Model (core) part of the MVC.
 - Does NOT know the Model, neither the View
 - Sends message through wx Publisher
"""

import time

from wx.lib.pubsub import pub


class Model:

    def __init__(self):
        None


    # This function might be called by the Controller.
    # Since the Model is supposed to work even without the Controller and the View,
    # it sends a message that might be caught by "someone" (aka. the Controller)
    def processSomething(self):

        #Simulating a process
        #time.sleep(1)

        #pub.sendMessage("MESSAGE SPREAD", message="A bottle in the sea.", arg2 = 99, arg3 = 99.1)

        for i in range(0, 5):
            pub.sendMessage("MESSAGE SPREAD", message="A bottle in the sea." + str(i), arg2 = 99, arg3 = 99.1)
            time.sleep(1)
