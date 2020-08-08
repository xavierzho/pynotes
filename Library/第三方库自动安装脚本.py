import os

libs = {
    "flask", "sklearn", "beautifulsoup4", "wheel",
    "sympy", "django", "werobot", "pandas", "pyqt5",
    "pyoeng1", "pypdf2", "docopt"}

try:
    for lib in libs:
        os.system("pip install " + lib)
    print("successful")
except:
    print("Failed Somehow")
