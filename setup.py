import sys
# conda install -c conda-forge cx_freeze
from cx_Freeze import setup, Executable

build_exe_options = {"optimize": 2}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

name = "Main.py"

setup(  name = name,
        version = "0.1",
        description = '"Dalli Klick" Desktop App',
        options = {"build_exe": build_exe_options},
        executables = [Executable(name, base=base)])