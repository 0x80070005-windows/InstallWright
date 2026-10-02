import os
import sys
import platform
import zipfile
from pathlib import Path


import setting

def extract(target_dir):
    zip_path = setting.source_dir

    with zipfile.ZipFile(zip_path) as z:
        members = z.infolist()
        for member in members:
            print(f"  {member.filename}")
            z.extract(member, target_dir)

        
def check_system():
    system = setting.system

    system_user = platform.system()

    if system_user == "Linux":
        if system == "2" or system == "3":
            print()
        else:
            print("The system is not supported.")
            input("\nДля продолжения нажмите Enter")
            sys.exit()

    elif system_user == "Windows":
        if system == "1" or system == "3":
            print()
        else:
            print("The system is not supported.")
            input("\nДля продолжения нажмите Enter")
            sys.exit()

def first_page():
    simvow = "-"

    product_name = setting.product_name
    product_version = setting.product_version
    description = setting.description
    publisher = setting.publisher


    first_line = "Скрипт установки " + product_name  + " v" + product_version
    count_len = len(first_line)

    simvows = simvow * count_len

    text = first_line + "\n" + simvows + "\n\n" + description + "\n\n" + publisher + "\n"

    print(text)

def two_page():

    script_dir = Path(__file__).resolve().parent
    DIR_FILE = script_dir / ".dir_install"


    if os.path.exists(DIR_FILE):
        os.remove(DIR_FILE)

    change_dir = setting.allow_change_dir
    if change_dir == "Yes":

        default_install_dir = setting.default_install_dir
        print("Директория по умолчанию - " + default_install_dir)

        user_change_dir = input("Хотите ли вы её поменять(y или n) - ")
        if user_change_dir.lower() == "y":
            user_directory = input("Введите директорию для установки - ")

            with open(DIR_FILE , "w") as fp:
                fp.write(user_directory)


    elif change_dir == "No":
        print("Директория для установки(изменить нельзя) - " + default_install_dir)

def start():
    script_dir = Path(__file__).resolve().parent
    DIR_FILE = script_dir / ".dir_install"
    
    check_system()
    first_page()
    input("Нажмите [Enter], чтобы начать установку, или нажмите [Ctrl+C] для отмены...")
    
    print("\n")
    
    two_page()

    if os.path.exists(DIR_FILE):
        with open(DIR_FILE , "r") as file:
            dir_install = file.read()
    else:
        dir_install = setting.default_install_dir

    print('\n')

    extract(dir_install)

start()