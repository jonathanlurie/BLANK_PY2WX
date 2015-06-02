# importing wxPython library, see the reference here :
# http://www.wxpython.org/docs/api/wx-module.html
# and an excelent step by step tutorial there :
# http://zetcode.com/wxpython
import wx

from Controller import *

# main function
def main():

    # each wx application must have a wx.App object
    app = wx.App()

    controller = Controller(title = "BLANK_PY2WX")

    # entering the endless loop that catches all the events
    app.MainLoop()


if __name__ == '__main__':
    main()
