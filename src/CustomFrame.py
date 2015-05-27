import wx


# CustomFrame just inherit from wx Frame to make it the way we want
class CustomFrame(wx.Frame):



    # constuctor
    def __init__(self, parent, title):

        # calling the regular wx.Frame constuctor
        super(CustomFrame, self).__init__(parent, title=title, size=(550, 400))

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

        # show it!
        self.Show()



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



    # quit the app
    def OnQuit(self, e):
        self.Close()
