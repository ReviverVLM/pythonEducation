"""
Задача "Учёт товаров":
Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.

Объекты класса Product будут создаваться следующим образом -
Product('Potato', 50.0, 'Vegetables')
и обладать следующими свойствами:

Атрибут name - название продукта (строка).
Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
Атрибут category - категория товара (строка).
Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
Все данные в строке разделены запятой с пробелами.

Объекты класса Shop будут создаваться следующим образом -
Shop()
и обладать следующими свойствами:

Инкапсулированный атрибут __file_name = 'products.txt'.

Метод get_products(self), который считывает всю информацию из файла __file_name,
закрывает его и возвращает единую строку со всеми товарами из файла __file_name.

Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине'.
"""


class Product:
    name = ""
    weight = 0.0
    category = ""

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        info = f"{self.name}, вес {self.weight}, {self.category}"
        return info


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        # with open(self.__file_name, 'r') as info:
        #     return info.readlines()
        temp_info = open(self.__file_name, 'r', encoding="UTF-8")
        info = temp_info.read()
        temp_info.close()
        return info

    def add(self, *products):
        for product in products:
            if (product.name in self.get_products() and str(product.weight) in self.get_products()
                    and product.category in self.get_products()):
                # inform = self.get_products()
                print(f"{product.name}" + " уже в списке")
            else:
                info = open(self.__file_name, 'a', encoding="UTF-8")
                info.write(f"{product}\n")
                info.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__
print(s1.get_products())

s1.add(p1, p2, p3)

print(s1.get_products())

# clear = "products.txt"
# open(clear, 'w')
