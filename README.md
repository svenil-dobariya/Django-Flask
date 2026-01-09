# Django-Flask

for data base useful commands
python manage.py makemigration filename
python manage.py migrate

for running server
python managr.py runserver
for open shell
python ./manage.py shell

diffent data Fields :--- 
CharField(max_length=…) - Short text (name, title) , 
TextField() - Large text (description, notes) , 
EmailField() - Email validation , 
SlugField() - URL-friendly text , 
URLField() -  Website links , 
IntegerField() - Integer numbers , 
BigIntegerField()-Very large integers , 
FloatField()	- Decimal with floating point , 
DecimalField() - Precise decimals (money) , 
PositiveIntegerField()-Only positive values , 
DateField()	- Date only , 
TimeField()	- Time only , 
DateTimeField() - Date + time , 
auto_now_add=True	 - Set once on creation , 
auto_now=True	- Update on every save , 