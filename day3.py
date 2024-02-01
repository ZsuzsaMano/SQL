import sqlite3

conn = sqlite3.connect('Day3.db')



# 3.1 Select all warehouses.
print('\n all warehouses')
res1=conn.execute('SELECT * FROM Warehouses')
for row in res1:
   print(row)
   
# 3.2 Select all boxes with a value larger than $150.
print('\n boxes >150 value')
   
res2=conn.execute('''SELECT * FROM Boxes WHERE value>=150''')
for row in res2:
   print(row)
   
# 3.3 Select all distinct contents in all the boxes.
print('\n distinct content boxes')

res3=conn.execute('''SELECT DISTINCT contents FROM Boxes ''')
for row in res3:
   print(row)
   

# 3.4 Select the average value of all the boxes.
print('\n avg value of boxes')

res4=conn.execute('''SELECT AVG(value) FROM Boxes ''')
for row in res4:
   print(row)

# 3.5 Select the warehouse code and the average value of the boxes in each warehouse.
   print('\n avg value of boxes by warehouse')

res5=conn.execute('''SELECT AVG(value),warehouse  
                  FROM Boxes 
                  GROUP BY warehouse''')
for row in res5:
   print(row)
   
# 3.6 Same as previous exercise, but select only those warehouses where the average value of the boxes is greater than 150.
print('\n avg value of boxes by warehouse if avg>150')

# res5=conn.execute('''SELECT AVG(value),warehouse  
#                   FROM Boxes 
#                   WHERE Value>150                WHY???????
#                   GROUP BY warehouse''')   

res5=conn.execute('''SELECT warehouse , AVG(value) 
                  FROM Boxes          
                  GROUP BY warehouse
                  HAVING AVG(value)>150''')   


for row in res5:
   print(row)
   
# 3.7 Select the code of each box, along with the name of the city the box is located in.
print('\n box code + location')
res7=conn.execute('''SELECT Boxes.Code, Warehouses.Location
                     FROM Boxes 
                     JOIN Warehouses
                    ON Boxes.Warehouse=Warehouses.code ''')
for row in res7:
   print(row)
   
# 3.8 Select the warehouse codes, along with the number of boxes in each warehouse.
print('\n warehouse code + num of boxes')

res8=conn.execute('''SELECT warehouse, Count(code)
                  FROM Boxes 
                  GROUP BY warehouse''')
for row in res8:
   print(row)

# 3.9 Select the codes of all warehouses that are saturated (a warehouse is saturated if the number of boxes in it is larger than the warehouse's capacity).
print('\n saturated warehouses')

res9=conn.execute('''SELECT warehouse, COUNT(Boxes.code)
                  FROM Boxes 
                  JOIN Warehouses
                  ON Boxes.Warehouse=Warehouses.code
                  GROUP BY warehouse
                  HAVING COUNT(Boxes.code)>capacity''')
for row in res9:
   print(row)


# 3.10 Select the codes of all the boxes located in Chicago.
print('\n boxes in Chicago')

res10=conn.execute('''SELECT Boxes.code
                  FROM Boxes 
                  JOIN Warehouses
                  ON Boxes.Warehouse=Warehouses.code          
                  WHERE Location="Chicago"''')
for row in res10:
   print(row)
   
# 3.11 Create a new warehouse in New York with a capacity for 3 boxes.
   
# 3.12 Create a new box, with code "H5RT", containing "Papers" with a value of $200,and located in warehouse 2.
# 3.13 Reduce the value of all boxes by 15%.
# 3.14 Remove all boxes with a value lower than $100.
#  3.15 Remove all boxes from saturated warehouses.
#  3.16 Add Index for column "Warehouse" in table "boxes"
#  !!!NOTE!!!: index should NOT be used on small tables in practice
#  3.17 Print all the existing indexes
#  !!!NOTE!!!: index should NOT be used on small tables in practice
#  3.18 Remove (drop) the index you added just