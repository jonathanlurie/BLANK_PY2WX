"""
The View part of the MVC.
 - Knows the Controller
 - Does NOT know the Model
"""

import wx

class View(wx.Frame):

    _controller = None

    _button = None
    _textBox = None


    # constuctor
    def __init__(self, parent, title, controller):

        # calling the regular wx.Frame constuctor
        wx.Frame.__init__(self, parent, title=title, size=(550, 400))

        # sets the Controller part
        self._controller = controller

        # make it possible to resize, but with boundaries
        self.SetMinSize((300, 300))
        self.SetMaxSize((800, 500))

        # initialize UI
        self.initUI()


    # init all the UI
    def initUI(self):

        # center the window on the screen
        self.Centre()

        # adding the menubar
        self.addMenuBar()

        # adding widgets
        self.addWidgets()

        self.Bind(wx.EVT_MOVE, self.OnMove)



    # adding everythong that concerns the menubar
    def addMenuBar(self):
        # creating the menu bar
        menubar = wx.MenuBar()

        # creating the "File" menu
        fileMenu = wx.Menu()

        # creating the "Quit" button
        quitMenuItem = wx.MenuItem(fileMenu, 1, '&Quit\tCtrl+Q')
        quitMenuItem.SetBitmap(wx.Bitmap('images/icon_quit.png'))

        # adding the behavior to quit
        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)

        # append the "Quit" menu item to the "File" menu
        fileMenu.AppendItem(quitMenuItem)


        # addin the "File" menu to the the menubar
        menubar.Append(fileMenu, '&File')

        # adding the menubar to our CustomFrame
        self.SetMenuBar(menubar)


    # adding the main widgets in this frame
    def addWidgets(self):

        # the main panel of our Frame (self)
        mainPanel = wx.Panel(self)
        mainPanel.SetBackgroundColour('#4f5049')

        # creating a BoxSizer
        vbox = wx.BoxSizer(wx.HORIZONTAL)

        # creating a left sub panel
        leftMidPan = wx.Panel(mainPanel)
        leftMidPan.SetBackgroundColour('#ededed')

        # creating a right sub panel
        rightMidPan2 = wx.Panel(mainPanel)
        rightMidPan2.SetBackgroundColour('#FFeded')

        # fitting the left and right sub panels in the horizontal box
        vbox.Add(leftMidPan, 3, wx.EXPAND | wx.ALL, 10)
        vbox.Add(rightMidPan2, 1, wx.EXPAND | wx.ALL, 10)

        # setting the sizer to the man panel
        mainPanel.SetSizer(vbox)


        # A button to ask the Model to work on something (throuh the Controller)
        self._button = wx.Button(rightMidPan2, label='Spread a message')
        self._button.Bind(wx.EVT_BUTTON, self._controller.spreadMessage)

        # A text box to display the output given by the Model, through the Controller and a Publisher
        self._textBox = wx.StaticText(leftMidPan, label="Nothing really interesting here", style=wx.ALIGN_CENTRE)



    # set the text in the text box
    def setText(self, t):
        print(t)

        self._textBox.SetLabel(t)


    def OnMove(self, e):

        x, y = e.GetPosition()
        self._textBox.SetLabel(str(x) + ' ' +  str(y))


    # quit the app
    def OnQuit(self, e):
        self.Close()
