import peewee
from models import Category, Product
import random

def add_category(name):
    try:
        obj = Category(title=name.lower().strip())
        obj.save()
        print(f'Сохранили категорию {obj} - {obj.title}')
    except (peewee.IntegrityError, peewee.InternalError):
        print(f'{name.lower().strip()} - эта категория уже существует')    


# add_category('laptops')
# add_category('    computers          ')
# add_category('Sony Playstations')
# add_category('Tablets')
# add_category('aerphones')

def add_products(name, price, category_name):
    category_name = category_name.lower().strip()
    try:
        category = Category.get(title=category_name)
    except peewee.DoesNotExist:
        price(f'Категории {category_name} не существует!')
    else:
        obj = Product(title=name, price=price, category_id=category)
        obj.save()
        print(f'Сохранили товар {obj} - {obj.title}')


# add_products('Asus megabook', 1000, 'laptops')
# add_products('Aser Swift', 1000, 'laptops')
# add_products('Iphone 14 Pro Max', 1200, 'Smartphones')
# add_products('Samsung S22 ULTRA', 1000, 'Smartphones')
# add_products('Airpod Pro', 500, 'aerphones')
# add_products('Asus megabook', 1000, 'laptops')
# add_products('Asus t', 1005, 'laptops')
# add_products('Asus meyy', 1050, 'laptops')
# add_products('Asus grre', 1230, 'laptops')

####################################################################
# добавление новых данных

# add_category('cars')

# with open('files/cars.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(5000, 20000)
#         add_products(name, price, 'cars')

# with open('files/telefon.txt', 'r') as file:
#     ls = file.readlines()
#     print(ls)
#     for x in ls:
#         name = x.strip()
#         price = random.randint(200, 1300)
#         add_products(name, price, 'smartphones')




















































