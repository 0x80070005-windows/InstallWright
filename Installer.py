import os
import sys
import platform
import zipfile
from pathlib import Path


class setting:




def clear():
	os.system("clear" if os.name != "nt" else "cls")


def spaced(text):
	return " ".join(text)


def extract(target_dir):
	create_uninstaller = setting.create_uninstaller
	zip_path = setting.source_dir

	clear()
	print()
	print("  [3/4] Распаковка")
	print("  " + "-" * 45)
	print()

	with zipfile.ZipFile(zip_path) as z:
		members = z.infolist()
		for member in members:
			print("  + " + member.filename)
			z.extract(member, target_dir)

			if create_uninstaller == "Yes":
				if os.path.exists("uninstaller.data"):
					with open("uninstaller.data", "r") as file:
						uninstaller_data = file.read()

					text_for_save = uninstaller_data + "\n" + member.filename

					with open("uninstaller.data", "w") as fp:
						fp.write(text_for_save)

				else:
					with open("uninstaller.data", "w") as fp:
						fp.write(member.filename)


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
	clear()

	product_name = setting.product_name
	product_version = setting.product_version
	description = setting.description
	publisher = setting.publisher

	print()
	print(spaced(product_name).center(64))
	print(spaced(product_version).center(64))
	print()
	print("-" * 64)
	print()
	print("  Издатель     " + publisher)
	print("  Описание     " + description)
	print()
	input("  Нажмите [Enter], чтобы начать установку, или нажмите [Ctrl+C] для отмены...")
	print("\n")


def two_page():
	script_dir = Path(__file__).resolve().parent
	DIR_FILE = script_dir / ".dir_install"

	if os.path.exists(DIR_FILE):
		os.remove(DIR_FILE)

	clear()
	print()
	print("  [1/4] Папка установки")
	print("  " + "-" * 45)
	print()

	change_dir = setting.allow_change_dir
	if change_dir == "Yes":

		default_install_dir = setting.default_install_dir
		print("  Директория по умолчанию - " + default_install_dir)
		print()

		user_change_dir = input("  Хотите ли вы её поменять(y или n) - ")
		if user_change_dir.lower() == "y":
			print()
			user_directory = input("  Введите директорию для установки - ")

			with open(DIR_FILE, "w") as fp:
				fp.write(user_directory)

	elif change_dir == "No":
		print("  Директория для установки(изменить нельзя) - " + default_install_dir)


def start():
	script_dir = Path(__file__).resolve().parent
	DIR_FILE = script_dir / ".dir_install"

	check_system()
	first_page()
	two_page()

	if os.path.exists(DIR_FILE):
		with open(DIR_FILE, "r") as file:
			dir_install = file.read()
	else:
		dir_install = setting.default_install_dir

	print('\n')

	extract(dir_install)

	clear()
	print()
	print("  [4/4] Завершено")
	print("  " + "-" * 45)
	print()
	print("  + Установка завершена успешно")
	print()
	print("  Продукт : " + setting.product_name)
	print("  Версия  : " + setting.product_version)
	print("  Путь    : " + dir_install)
	print()


start()