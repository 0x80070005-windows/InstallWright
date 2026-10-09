import os


def insert_lines_block(filename, at_line, new_lines):
    """Вставляет new_lines перед строкой at_line (1-based)."""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = [l if l.endswith('\n') else l + '\n' for l in new_lines]
    lines[at_line - 1:at_line - 1] = new_lines

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)


with open("setting.py", 'r', encoding='utf-8') as f:
    setting_lines = ["\t" + line for line in f.readlines()]

insert_lines_block("Installer.py", 10, setting_lines)

os.remove("setting.py")