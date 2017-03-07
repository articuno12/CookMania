# CookMania
portal for sharing recipes built using web2py

In this portal,users can create account , log in and upload recipes , edit their recipes , view like and comment on others recipes.

To run :<br>
1. Install web2py following the link :http://www.web2py.com/init/default/download <br>
2. Download the repository and move cookmania folder (inside the repository ) to web2py applications folder. <br>
3. run on terminal : python2.7 web2py.py -a 'your password' -i 127.0.0.1 -p 8000 <br>
4. open http://127.0.0.1:8000/cookmania/default/index on your browser <br>

<b> Detailed Description </b>
Login   page​<br>
:   Authentication   is   needed   using   USERNAME   and   PASSWORD   for   already  
registered   users.   If   the   user   fails   to   give   appropriate   details,   error   messages   are   displayed  
accordingly. <br>
 
Registration   page:   Registration    for   newly   visiting   users.   The   registration   form   fields  
is left as per your choice.<br>
Password   Validation:   minimum   8   characters   long,   should   contain   at­least   an  
alphanumeric character, etc.  <br>
 
Home   page:   After   the   intended   user   logs   in,   the   webpage   is   redirected   to   the   home   page  
that   consists   Title   ,   small   image   and   description   of   the   recently   uploaded   recipes   in   a   tabular  
form.The   home   page   displays   only   recent   10   or   20   recipes.   On   pressing   NEXT,   it  
should display next 10 or 20 recipes. <br> 
 
 
 
 
 Detail   Description   of   a   particular   recipe:   ​
After   the   user   selects   a   recipe   from   the   home   page   by  
clicking   on   the   Title   of   the   recipe,   the   page   is   redirected   to   the   intended   recipe   consisting  
of the following: <br>
● Name/Title of the recipe along with Author name and Date of Upload. <br>
● Image of the final Dish. (Bonus for multiple images) <br>
● Short Description of the Dish. <br>
● The   complete   recipe   displayed   in   a   beautifully   structured   way.   (As   per   your  
choice). <br>
● Like button and No of Likes. <br>
 
Upload   A   recipe:   ​<br>
A   logged   in   user   is   allowed   to   share   his/her   recipe   by   uploading   a   recipe.The  
page should have a FORM which takes complete information of the recipe.  <br>
 
My   Recipes:    If   the   user   wants   to   see   his/her   uploaded   recipes,   then   he   can   view   it   on   this   page.  <br>
 
Privileges Given to Users:  <br>
● User   can   upload   a   recipe   and   can   also   edit   it   afterwards   (Bonus   for   EDIT).   He   cannot  
manipulate the recipes of other users. <br>
● User can like a recipe by pressing LIKE button on the page of that recipe. <br>


