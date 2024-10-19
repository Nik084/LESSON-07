from pprint import pprint

class Product:
    def __init__(self, name, wight, category):
        self.name =name
        self.wight = wight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.wight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        # pprint(file.read())
        file_in = file.read()
        file.close()
        return file_in

    def add(self, *products):
        # pass
        for i in products:
            # print (type(i))
            i = str(i)
            # print(i)
            if i in self.get_products():
                print(f'Продукт "{i}" уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()

s1 = Shop()
p1 = Product('Potato', 45, 'Vegetables')
p2 = Product('Apple', 84, 'Fruits')
p3 = Product('Spaghetti', 3.4, 'Groceries')
p4 = Product('Apple', 10.1, 'Marmalade')

print(p2)

s1.add(p1, p2, p3, p4)
print(s1.get_products())