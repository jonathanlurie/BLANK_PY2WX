# BLANK_PY2WX

This project provide an empty nutshell for a wxPython GUI application that needs to be packaged with py2app.  
This also provide a script `launcher.sh` that allows a execution of the app without the need of packaging.

The `package.sh` script just contains the instruction to package the project with py2app. This script is double-clickable. It will use :

- `build` directory as a temporary building place
- `dist` directory to place the final `.app` package

## Dependencies

- [wxPython](http://www.wxpython.org/) for the GUI part
- [py2app](https://pypi.python.org/pypi/py2app/) for building the package