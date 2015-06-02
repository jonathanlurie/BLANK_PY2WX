"""
The Controller part of the MVC.
 - Knows the View
 - Knows the Model
 - Receive Publiser instructions
"""

# import the view
from View import *

# import the model
from Model import *


from wx.lib.pubsub import pub



class Controller:

    _model = None

    # the view part of the MVC
    _view = None

    def __init__(self, title):

        self._model = Model()
        self._view = View(None, title, controller = self)
        # show it!
        self._view.Show()

        # subscribe to all messages from the Model
        self._subscribeToMessages()


    # uses Publisher to add callback to messages
    def _subscribeToMessages(self):
        pub.subscribe(self.messageSpreadListener, "MESSAGE SPREAD")



    # this function is triggered by a click on the button in the view.
    # It asks the Model to trigger a process, then when this process is done
    # the Model will use a Publisher to reach the view and say "it's done"
    def spreadMessage(self, event):
        self._model.processSomething()



    # when the Model sends a message "MESSAGE SPREAD", this function is called
    def messageSpreadListener(self, message, arg2=None, arg3=None):


        t = "the Model sent this message through a Publisher :\n"
        t = t + message + "\t"

        if(arg2):
             t = t + str(arg2) + "\t"

        if(arg3):
            t = t + str(arg3) + "\t"

        self._view.setText(t)
