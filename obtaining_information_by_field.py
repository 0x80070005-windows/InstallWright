import os


class Product_metadata:
    def product_name():
        product_name = input("Введите название программы - ")
        return product_name

    def product_version():
        product_version = input("Введите версию программы(только цифры) - ")
        return product_version

    def publisher():
        publisher = input("Введите издателя - ")
        return publisher

    def description():
        description = input("Введите Описание - ")
        return description

class Package_and_build:
    def source_dir():
        source_dir = input("Введите директорию до архива - ")
        if os.path.isfile(source_dir):
            print()
        else:

            while True:
                source_dir = input("Введите директорию директорию для архива - ")
                if os.path.isfile(source_dir):
                    break
                else:
                    continue


        return source_dir

    def system():
        system = input("1 - Windows\n2 - linux\n3 - кросплотформенная\nВведите с какими систами будет работать - ")
        if system == "1" or system == "2" or system == "3":
            return system


class Intall:
    def default_install_dir():
        default_install_dir = input("Папка установки по умолчанию - ")
        return default_install_dir

    def allow_change_dir():
        allow_change_dir = input("1 - Да\n2 - Нет\nРазрешить менять папку - ")

        if allow_change_dir == "1":
            return "Yes"
        elif allow_change_dir == "2":
            return "No"

class Uninstaller:                
    def create_uninstaller():
        create_uninstaller_input = input("\n1 - Да\n2 - Нет\nСоздавать деинсталятор - ")
        if create_uninstaller_input == "1":    
            return "Yes"
        
        elif create_uninstaller_input == "2":
            return "No"