cp --backup=numbered ./tmp/*.png /home/ubuntu/Dropbox/menu_backups
mv ./tmp/*.png /home/ubuntu/ont/template/assets/menus

cd template;
git config remote.origin.url https://ovenandtap%40gmail.com:tap1234@jeremy-teff-apql.squarespace.com/template.git; 
git add -A;
git commit -m "Updated menus.";
git push;

