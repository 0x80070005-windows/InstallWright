import os
import sys
from pathlib import Path
import shutil


def main():
    if os.path.exists("uninstaller.data"):
        print()
    else:
        print("файл uninstaller.data не найден !")
        input("\n\nДля выхода нажмите Enter")
        sys.exit()


    with open("uninstaller.data", "r", encoding="utf-8") as file:
        for line in file:
            # Убираем пробелы и символы переноса строки (\n)
            clean_path = line.strip()
            
            # Создаем объект Path
            path_obj = Path(clean_path)
            
            # Проверяем, существует ли объект вообще
            if path_obj.exists():
                if path_obj.is_dir():
                    shutil.rmtree(clean_path)
                    print(f"Папка {clean_path} успешно удалена.")
                
                elif path_obj.is_file():
                    os.remove(clean_path)
                    print(f"Файл {clean_path} успешно удален.")
    try:
        # sys.argv[0] содержит точный путь к текущему запущенному скрипту
        os.remove(sys.argv[0])
        print("Скрипт успешно удалил сам себя с диска.")
    except Exception as e:
        print(f"Не удалось удалить файл: {e}")


    os.system("rm -rf uninstaller.data")

    if os.path.exists("Installer"):
        os.system("rm -rf Installer")

main()