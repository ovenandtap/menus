#!/bin/bash

rm -r pngquant-files; 
rm -r optipng-files; 
rm -r converted;
rm -r renamed;

mkdir renamed

# Run a check on the filenames, changing them accordingly
shopt -s nullglob
for f in originals/*.pdf
do
  f_lower=`echo "$f" | tr '[:upper:]' '[:lower:]'`
  if [[ $f_lower == *"brunch"* ]]; then
    if [[ $f_lower == *"beverage"* ]]; then
      cp "$f" renamed/brunch_drinks_menu.pdf;
    else
      cp "$f" renamed/brunch_menu.pdf;
    fi
  else
    if [[ $f_lower == *"dinner"* ]]; then
      if [[ $f_lower == *"beverage"* ]]; then
        cp "$f" renamed/dinner_drinks_menu.pdf;
      else
        cp "$f" renamed/dinner_menu.pdf;
      fi
    else
      if [[ $f_lower == *"lunch"* ]]; then
        if [[ $f_lower == *"beverage"* ]]; then
          cp "$f" renamed/lunch_drinks_menu.pdf;
        else
          cp "$f" renamed/lunch_menu.pdf;
        fi
      fi
    fi
  fi
done

# Convert PDFs to PNGs
mkdir converted
for f in renamed/*.pdf ; do convert -density 150 "$f" -quality 70 "${f%.*}.png" ; done
mkdir pngquant-files
mv renamed/*.png pngquant-files;

# pngquant operates on copies in pngquant-files
cd pngquant-files && pngquant --quality=0-10 --speed 1 --ext=.png --force *.png && cd ../ ;

## optipng copies files to optipng-files
optipng -o7 -strip=all -dir optipng-files pngquant-files/*;

## copy optimized files to squarespace assets folder.
ls optipng-files
mv optipng-files/*.png template/assets/menus;
ls optipng-files

cd template && git config remote.origin.url https://ovenandtap%40gmail.com:tap1234@jeremy-teff-apql.squarespace.com/template.git && git add -A && git commit -m "Updated menus." && git push;

