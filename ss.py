from menu_pipeline import MenuProcessing

# Assumes a symbolic link to the updates folder
for filename in filenames:
    if "pdf" in filename:
        mp = MenuProcessing("/home/sam/Projects/ovenandtap/menus/updates/" + filename)
        mp.process()
