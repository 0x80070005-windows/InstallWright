import os
from pathlib import Path

import Create_setting_file

def Create_install():
    if not os.path.exists("setting.py"):
        Create_setting_file.main()
    else:
        user = input("хотите ли вы поменять конфиг(y or n) - ")
        if user.lower() == "y":
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

    os.system("rf -rf /dist/")

def Create_uninstaller():
    script_dir = os.path.dirname(os.path.realpath(__file__))

    os.system("pyinstaller --onefile Uninstaller.py")

    DIR_FILE = script_dir + "/build"
    os.system("rm -rf " + DIR_FILE)

    DIR_FILE = script_dir + "/Uninstaller.spec"
    os.system("rm -rf " + DIR_FILE)

    FIRST = script_dir + "/dist/Uninstaller"
    GET = script_dir + ""
    os.system("cp " + FIRST + " " + GET) 

    DIR_FILE = script_dir + "/dist"
    os.system("rm -rf " + DIR_FILE)



Create_install()
Create_uninstaller()