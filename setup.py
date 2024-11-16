from setuptools import setup

APP = ['your_app.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['required_package'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
