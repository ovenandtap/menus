import os, shutil, subprocess
from wand.image import Image


class MenuProcessing(object):
    
    pngquant_cmd = "pngquant --quality=0-20 --speed 1 --ext .png --force "
    scratch_path = "./tmp/"

    food_menu_suffix = "_menu"
    drink_menu_suffix = "_drinks_menu"

    menu_types = ["breakfast","brunch", "lunch", "dinner"]
    drink_words = ["beverage", "drink"]
    
    def __init__(self, path):
        self.path = path
        self.assetName = self._buildAssetName(path)
        self.error = False
        self.message = ""
        
    def process(self):
        if not os.path.exists(self.scratch_path):
            os.makedirs(self.scratch_path)
        
        shutil.copyfile(src=self.path, dst=self.scratch_path + self.assetName + ".pdf")
        
        is_converted = self._pdfToPng(self.scratch_path + self.assetName + ".pdf")
        is_crushed = self._crushPng(self.scratch_path + self.assetName + ".png")
        
    
    def _pdfToPng(self, pdf_path):
        if not ('pdf' in pdf_path.lower()):
            print("Attempted to convert non-pdf.")
            return False
        
        name = pdf_path.split('.')
        convert = Image(filename=pdf_path, resolution=200)  

        page=convert.sequence[0]
        convert.compression_quality = 70
        convert.save(filename="." + name[1] +  ".png")
        

    
    def _crushPng(self, png_path):
        if "png" not in png_path:
            print("trying to crush non-png")
            return False
        
        optimize_proc = subprocess.check_output(self.pngquant_cmd + png_path, shell=True)
        print(optimize_proc)
        return True 
        
    
    def _isDrinkMenu(self, menu):
        if "beverage" in menu.lower():
            return True
        return False
    
    def _buildAssetName(self, filename):
        parts = filename.split(".")
        assert len(parts) == 2
        
        lowercase_name = parts[0].lower().replace(" ", "_")
        extension_name = "." + parts[1]
        
        for menu in self.menu_types:
            if menu in lowercase_name:
                if "beverage" in lowercase_name:
                    return menu + self.drink_menu_suffix
                else:
                    return menu + self.food_menu_suffix
        
        print("Asset doesn't match criteria")

