import obtaining_information_by_field

def main():
    text_for_save = ""

    product_name = obtaining_information_by_field.Product_metadata.product_name()
    text_for_save = text_for_save + "product_name = " + '"' + product_name + '"' + "\n"

    product_version = obtaining_information_by_field.Product_metadata.product_version()
    text_for_save = text_for_save + "product_version = "  + '"' + product_version + '"' + "\n"

    publisher = obtaining_information_by_field.Product_metadata.publisher()
    text_for_save = text_for_save + "publisher = " + '"' + publisher + '"' + "\n"

    description = obtaining_information_by_field.Product_metadata.description()
    text_for_save = text_for_save + "description = " + '"' + description + '"' + "\n"


    source_dir = obtaining_information_by_field.Package_and_build.source_dir()
    text_for_save = text_for_save + "source_dir = " + '"' + source_dir + '"' + "\n"


    system = obtaining_information_by_field.Package_and_build.system()
    text_for_save = text_for_save + "system = " + '"' + system + '"' + "\n"


    default_install_dir = obtaining_information_by_field.Intall.default_install_dir()
    text_for_save = text_for_save + "default_install_dir = " + '"' + default_install_dir + '"' + "\n"

    allow_change_dir = obtaining_information_by_field.Intall.allow_change_dir()
    text_for_save = text_for_save + "allow_change_dir = " + '"' + allow_change_dir + '"' + "\n"

    create_uninstaller = obtaining_information_by_field.Uninstaller.create_uninstaller()
    text_for_save = text_for_save + "create_uninstaller = " + '"' + create_uninstaller + '"'


    with open('setting.py' , 'w') as fp:
        fp.write(text_for_save)