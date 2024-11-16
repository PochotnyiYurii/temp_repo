from setuptools import setup

APP = ['real_love.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],  # Добавьте все необходимые библиотеки
    'excludes': ['required_package']  # Добавьте модули, которые не обязательны
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
