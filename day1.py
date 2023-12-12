import sqlite3

conn = sqlite3.connect('Day1.db')

print('Opened database successfully')

# create tables
conn.execute('''CREATE TABLE IF NOT EXISTS Manufacturers (
  Code INTEGER,
  Name TEXT NOT NULL,
  PRIMARY KEY (Code)
);
''')
print( "Manufacturers Table created successfully")
conn.execute('''
CREATE TABLE IF NOT EXISTS Products (
  Code INTEGER,
  Name TEXT NOT NULL,
  Price INTEGER NOT NULL,
  Manufacturer INTEGER NOT NULL,
  PRIMARY KEY (Code)
);''')
print( "Product Table created successfully")

#insert values
conn.execute('''INSERT INTO Manufacturers(Code,Name) VALUES(1,'Sony');''')
conn.execute('''INSERT INTO Manufacturers(Code,Name) VALUES(2,'Creative Labs');''')
conn.execute('''INSERT INTO Manufacturers(Code,Name) VALUES(3,'Hewlett-Packard');''')
conn.execute('''INSERT INTO Manufacturers(Code,Name) VALUES(4,'Iomega');''')
conn.execute('''INSERT INTO Manufacturers(Code,Name) VALUES(5,'Fujitsu');''')
conn.execute('''INSERT INTO Manufacturers(Code,Name) VALUES(6,'Winchester');''')
print( "Manufacturers table populated successfully")

conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(1,'Hard drive',240,5);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(2,'Memory',120,6);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(3,'ZIP drive',150,4);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(4,'Floppy disk',5,6);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(5,'Monitor',240,1);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(6,'DVD drive',180,2);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(7,'CD drive',90,2);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(8,'Printer',270,3);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(9,'Toner cartridge',66,3);''')
conn.execute('''INSERT INTO Products(Code,Name,Price,Manufacturer) VALUES(10,'DVD burner',180,2);''')
print( "Products table populated successfully")

#1.1 Select the names of all the products in the store.
cursor1 = conn.execute("SELECT name FROM Products")
print ("\n Product Name:")
for row in cursor1:
   print (row[0])
   
#1.2 Select the names and the prices of all the products in the store.
cursor2 = conn.execute("SELECT name, price FROM Products")
print ("\n Product Name and price:")
for row in cursor2:
   print (f'{row[0]}: {row[1]} €')

# 1.3 Select the name of the products with a price less than or equal to $200.
cursor3 = conn.execute("SELECT name FROM Products WHERE price >= 200")
print ("\n Product Name and price  200:")
for row in cursor3:
   print (f'{row[0]}')

# 1.4 Select all the products with a price between $60 and $120.
cursor4 = conn.execute("SELECT name FROM Products WHERE price <120 AND price>60 ")
print ("\n Product Name and price 60-200:")
for row in cursor4:
   print (f'{row[0]}')

# 1.5 Select the name and price in cents (i.e., the price must be multiplied by 100).
cursor5 = conn.execute("SELECT name, price FROM Products")
print ("\n Product Name and price:")
for row in cursor5:
   print (f'{row[0]}: {row[1]*100} cent')

# 1.6 Compute the average price of all the products.
cursor6 = conn.execute("SELECT AVG(price) FROM Products")
print ("\n Product Avarage price:")
for row in cursor6:
   print (f'{row[0]} €')

# 1.7 Compute the average price of all products with manufacturer code equal to 2.
cursor7 = conn.execute("SELECT AVG(price) FROM Products WHERE Manufacturer=2")
print ("\n Product Avarage price from manu 2:")
for row in cursor7:
   print (f'{row[0]} €')

# 1.8 Compute the number of products with a price larger than or equal to $180.
cursor8 = conn.execute("SELECT COUNT(name) FROM Products WHERE price>=180")
print ("\n Products >=180€:")
for row in cursor8:
   print (f'{row[0]}')


# 1.9 Select the name and price of all products with a price larger than or equal to $180, and sort first by price (in descending order), and then by name (in ascending order).
cursor9 = conn.execute("SELECT name, price FROM Products WHERE price >= 180 ORDER BY price DESC, name ASC")
print ("\n Product price DESC Name ASC and  >=180 :")
for row in cursor9:
   print (f'{row[0]}: {row[1]}')

# 1.10 Select all the data from the products, including all the data for each product's manufacturer.
cursor10 = conn.execute("SELECT * FROM Products JOIN Manufacturers ON Products.Manufacturer=Manufacturers.Code")
print ("\n Product with Manufacturer :")
for row in cursor10:
   print (f'{row}')

# 1.11 Select the product name, price, and manufacturer name of all the products.
cursor11 = conn.execute("SELECT Products.name, price, Manufacturers.name FROM Products JOIN Manufacturers ON Products.Manufacturer=Manufacturers.Code")
print ("\n Product name, price with Manufacturer :")
for row in cursor11:
   print (f'{row}')

# 1.12 Select the average price of each manufacturer's products, showing only the manufacturer's code.
cursor12 = conn.execute("SELECT AVG(price), Manufacturer FROM Products GROUP BY Manufacturer")
print ("\n AVG price by Manufacturer :")
for row in cursor12:
   print (f'{row}')

# 1.13 Select the average price of each manufacturer's products, showing the manufacturer's name.
cursor13 = conn.execute("SELECT AVG(price), Manufacturers.name FROM Products JOIN Manufacturers ON Products.Manufacturer=Manufacturers.Code GROUP BY Manufacturer")
print ("\n Product name, price with Manufacturer :")
for row in cursor13:
   print (f'{row}')

# 1.14 Select the names of manufacturer whose products have an average price larger than or equal to $150.

# 1.15 Select the name and price of the cheapest product.

# 1.16 Select the name of each manufacturer along with the name and price of its most expensive product.

# 1.17 Add a new product: Loudspeakers, $70, manufacturer 2.

# 1.18 Update the name of product 8 to "Laser Printer".

# 1.19 Apply a 10% discount to all products.

# 1.20 Apply a 10% discount to all products with a price larger than or equal to $120.

conn.close()