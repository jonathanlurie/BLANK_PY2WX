"""

Usage:
    python setup.py py2app
"""

from setuptools import setup
import glob

exec(open('src/_version.py').read())


APP = ['src/main.py']
DATA_FILES = [
    ('images', glob.glob('images/*')),
    ('settings', glob.glob('settings/*')),
    ('text', glob.glob('text/*')),
    ('lib/natives', glob.glob('lib/natives/*')),

]

OPTIONS = {
    'iconfile':'ressources/icon.icns',
    'argv_emulation': True#,
    #'frameworks' : glob.glob('./lib/natives/*')
}

setup(
    name='BLANK_PY2WX',
    version= __version__,
    url='https://github.com/jonathanlurie',
    author='Jonathan Lurie',
    author_email='lurie.jo@gmail.com',
    description='Empty nutshell for wxPython GUI application, packaged with py2app',
    license='MIT',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
