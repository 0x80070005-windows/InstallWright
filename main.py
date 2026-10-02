import os
from pathlib import Path

import Create_setting_file

Create_setting_file.main()

script_dir = os.path.dirname(os.path.realpath(__file__))

os.system("pyinstaller --onefile Installer.py")

DIR_FILE = script_dir + "/build"
os.system("rm -rf " + DIR_FILE)

DIR_FILE = script_dir + "/Installer.spec"
os.system("rm -rf " + DIR_FILE)

FIRST = script_dir + "/dist/Installer"
GET = script_dir + ""
os.system("cp " + FIRST + " " + GET) 


DIR_FILE = script_dir + "/dist"
os.system("rm -rf " + DIR_FILE)