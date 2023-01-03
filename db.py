import mariadb

conn = mariadb.connect(
    user="root",
    password="230799",
    host="localhost",
    database="erpnext_gsg")
cur = conn.cursor()

# retrieving information


year = input("Enter Year")

fields_statement = f""" order_id,order_date """
table_name= f""" orders """


query = f""" select {fields_statement} from {table_name}"""
where_statement = f""" where Year(order_date) = {year} """

query += where_statement
print(query)
cur.execute(query)
data = tuple(cur)
print(len(data))
print("ID \t\tDate")
print("____________")
for order_id,order_date in data:
    print(order_id,order_date)

# insert information
# try:
#     cur.execute("INSERT INTO employees (first_name,last_name) VALUES (?, ?)", ("Maria", "DB"))
# except mariadb.Error as e:
#     print(f"Error: {e}")

# conn.commit()
# print(f"Last Inserted ID: {cur.lastrowid}")

conn.close()


while True:
    x = int(input("""1- Get total for each of orders
2-Get all orders which created on 1997
3-Get total for each order which created on 1996
4-Get Customer total spends among all orders on 1996
5-Get best supplier based on products which included in each of order details
"""))