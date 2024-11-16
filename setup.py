from setuptools import setup

APP = ['real_love.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],  # Убедитесь, что Tkinter указан правильно
    'excludes': ['required_package'],  # Убедитесь, что лишние пакеты исключены
    'plist': {
        'CFBundleIdentifier': 'com.example.realloveapp',  # Уникальный идентификатор
        'CFBundleName': 'Real Love App',
        'CFBundleVersion': '1.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
