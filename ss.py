import os, subprocess

from menu_pipeline import MenuProcessing

updates_path = "/home/ubuntu/ont/updates/"
filenames = os.listdir(updates_path)

# Assumes a symbolic link to the updates folder
for filename in filenames:
    if "pdf" in filename:
        mp = MenuProcessing(updates_path + filename)
        mp.process()

optimize_proc = subprocess.check_output("./ss.sh", shell=True)
print(optimize_proc)
