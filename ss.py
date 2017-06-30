import os, shutil, subprocess

from wand.image import Image

original_menus_folder = "./originals/"

menu_brunch_food = "./renamed/brunch_menu.pdf"
menu_brunch_drinks = "./renamed/brunch_drinks_menu.pdf"
menu_lunch_food = "./renamed/lunch_menu.pdf"
menu_lunch_drinks = "./renamed/lrunch_drinks_menu.pdf"
menu_dinner_food = "./renamed/dinner_menu.pdf"
menu_dinner_drinks = "./renamed/dinner_drinks_menu.pdf"

DRINK_WORDS = ["beverage", "drink"]

def is_drink_menu(menu_str):
    for drink_word in DRINK_WORDS:
        if drink_word in menu_str:
            return True
    return False
    

def get_renamed_menu(original_menu_name):
    menu_lower = original_menu_name.lower()

    if "brunch" in menu_lower:
	if is_drink_menu(menu_lower):
	    return  menu_brunch_drinks;
	return  menu_brunch_food);
    if "lunch" in menu_lower:
	if is_drink_menu(menu_lower):
	    return  menu_lunch_drinks;
	return  menu_lunch_food);
    if "dinner" in menu_lower:
	if is_drink_menu(menu_lower):
	    return  menu_dinner_drinks;
	return  menu_dinner_food;
    
    
def rename_files():
    os.mkdir("./renamed")
    
    originals = os.listdir(original_menus_folder)
    for original in originals:
        renamed = get_renamed_menu(original)
        shutil.copyfile(original_menus_folder + "original", renamed)


def convert_pdf_to_png(filename):
    os.mkdir("./converted/")

    with Image(filename=filename) as pdf:
        with pdf.convert('png') as converted:
            converted.density = 150
            converted.quality = 70
            converted.save("./converted/" + file.strip(".")[0] + ".png")

def convert_renamed_to_png():
    renamed_dir = "./renamed/"
    renamed_files = os.listdir(renamed_dir)
    for filename in renamed_files:
        convert_pdf_to_png(renamed_dir + filename)

command = """cd converted && pngquant --quality=0-10 --speed 1 --ext=.png --force *.png && cd ../ ;"""

def optimize():
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    print(process.returncode)
