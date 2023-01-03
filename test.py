# from functions import find_product
# import functions
from functions import *
import datetime
import math

print(math.ceil(1.2))  # 2
print(math.floor(1.2)) # 1

print(abs(-8))
print(math.pow(2,3))
print(max(3,2,5,6,1))
# products_count = int(input("Enter the number of products: "))
# products_list = []
# for i in range(products_count):
#     product_name = input("Enter Product Name:")
#     product_qty = int(input("Enter Product QTY:"))
#     product_price = float(input("Enter Product Price"))
#     product = {
#         "product_name": product_name,
#         "product_qty": product_qty,
#         "product_price": product_price
#     }
#     products_list.append(product)


#
#
#
# new_search = input("Search by product name")
# find_product(new_search, products_list)
# print_hi()
# print(x)

print(datetime.datetime.now().strftime("%A %d-%m-%Y  %H:%M:%S"))