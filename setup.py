from setuptools import setup

APP = ['real_love.py']  # имя вашего Python файла
DATA_FILES = []  # если нужно добавить дополнительные файлы
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],  # добавляем tkinter, если используете его
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
