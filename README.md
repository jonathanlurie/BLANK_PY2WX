# BLANK_PY2WX

> **BLANK** stands for *empty*  
> **PY2** stands for *py2app*  
> **WX** stands for *wxPython*  

This project provide an empty nutshell for a wxPython GUI application that needs to be packaged with py2app.  
This also provide a script `launcher.sh` that allows a execution of the app without the need of packaging.

The `package.sh` script just contains the instruction to package the project with py2app. This script is double-clickable. It will use :

- `build` directory as a temporary building place
- `dist` directory to place the final `.app` package

## Design pattern

The app is composed of 3 main parts, in accordance to the *Model-View-Controller* design pattern. In addition, the `main.py` is the entry point, in charge of the creation of the **Controller**.  
Since an *MVC-compliant* application is supposed to be able to run and be fully functional without the **View-Controller**, the **Model** communicates to the other part of the application *sending messages* with a *Publisher* (wx.lib.pubsub). On the other side, the **Controller**  is *subscribing* to messages and implements the appropriate *callbacks*. Thanks to this indirect communication, the **Model** remains free of  dependencies toward **View-Controller**.  

## Dependencies

- [wxPython](http://www.wxpython.org/) for the GUI part
- [py2app](https://pypi.python.org/pypi/py2app/) for building the package