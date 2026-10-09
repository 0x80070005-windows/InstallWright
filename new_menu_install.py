name = "AwesomeApp"
version = "v1.5"
description = "Description is empty"
corporation = "© Kirill Corporation"

left_gray_top = "╭"
right_gray_top = "╮"

left_gray_down = "╰"
right_gray_down = "╯"

vertical = "│"
horizontal = "─"

first_string = name + "  " + version

len_name_and_version = len(first_string)
len_description = len(description)

if len_name_and_version > len_description:
    main_len = len_name_and_version

else:
    main_len = len_description

horizontal_new = main_len * horizontal

string = left_gray_top + horizontal_new + right_gray_top + "\n" + vertical + "  " + first_string 