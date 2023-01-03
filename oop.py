import random


class Car:

    def __init__(self,brand,your_color="Red"):
        self._color = your_color
        self._brand = brand
        self.speed = 0

    def drive(self,new_speed):
        self.speed += new_speed

    def reverse(self,new_speed):
        self.speed -= new_speed

    def get_color(self):
        return self._color

    def set_color(self,new_color):
        self._color = new_color

    def get_brand(self):
        return self._brand

    def set_brand(self,new_brand):
        self._brand = new_brand




car = Car("Verna","Red")

car.set_color("White")

print(car.get_brand())
print(car.get_color())


class Product:
    index = 1

    def __init__(self):
        self.product_name =input("Enter Product Name:")
        self.product_price = float(input("Enter Product Price"))
        self.product_qty =  int(input("Enter Product QTY:"))
        self._product_id = Product.index
        Product.index += 1


    @staticmethod
    def generate_serial():
        return random.randint(10000,99999)

    def get_product_details(self):
        print("Product ID ", self._product_id)
        print("Product Name ",self.product_name)
        print("Product QTY ", self.product_qty)
        print("Product Price ", self.product_price)


# product_count = int(input("Enter Products Count:"))
# products_list = []
# for i in range(product_count):
#     new_product = Product()
#     products_list.append(new_product)
#
# for product in products_list:
#     product.get_product_details()
# print(Product.get_product_details())
print(Product.generate_serial())