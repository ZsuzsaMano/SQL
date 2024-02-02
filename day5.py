
import sqlite3

conn = sqlite3.connect('Day5.db')

print("\n5.1 Select the name of all the pieces.") 
res1=conn.execute('SELECT name FROM Pieces')
for row in res1:
   print(row)
   

print("\n5.2  Select all the providers' data. ")
res2=conn.execute('SELECT * FROM providers')
for row in res2:
   print(row)
   
   
print("\n5.3 Obtain the average price of each piece (show only the piece code and the average price).")
res3=conn.execute('''SELECT piece, AVG(price)
                  FROM provides
                  GROUP BY piece''')
for row in res3:
   print(row)
   

print("\n5.4  Obtain the names of all providers who supply piece 1.")
res4=conn.execute('''SELECT Providers.name
                  FROM Provides
                  JOIN Providers
                  ON Providers.code=Provides.provider
                  WHERE piece=1''')
for row in res4:
   print(row)


print("\n5.5 Select the name of pieces provided by provider with code HAL.")
res5=conn.execute('''SELECT pieces.name
                  FROM Provides
                  JOIN Pieces
                  ON Pieces.code=Provides.piece
                  WHERE provider="HAL"''')
for row in res5:
   print(row)
   
   
print("\n5.6 For each piece, find the most expensive offering of that piece and include the piece name, provider name, and price (note that there could be two providers who supply the same piece at the most expensive price) Note: Insert a new record in the table to see if your query can be scaled up to answer the query if there are two providers who supply the same piece at the most expensive price.")
res6=conn.execute('''SELECT pieces.name, MAX(price), provides.provider
                  FROM Provides
                  JOIN Pieces
                  ON Pieces.code=Provides.piece
                  GROUP BY pieces.code
                  ''')
for row in res6:
   print(row)
   
   
print("\n5.7 Add an entry to the database to indicate that Skellington Supplies (code TNBC) will provide sprockets (code 1) for 7 cents each.")
conn.execute('''INSERT INTO Provides 
             VALUES(1, 'TNBC', 7);''')
res7=conn.execute('''SELECT * FROM Provides
                  ''')
for row in res7:
   print(row)



print("\n5.8 Increase all prices by one cent.")
conn.execute('''UPDATE  Provides
             SET price=price+0.01;''')
res8=conn.execute('''SELECT * FROM Provides
                  ''')
for row in res8:
   print(row)

print("\n5.9 Update the database to reflect that 'Susan Calvin Corp'. (code RBT) will not supply bolts (code 4).")
conn.execute('''DELETE FROM Provides
                     WHERE Provider="RBT" AND Piece=4
                     ''')
res9=conn.execute('''SELECT * FROM Provides''')
for row in res9:
   print(row)

   

print("\n5.10 Update the database to reflect that 'Susan Calvin Corp'.(code RBT)will not supply any pieces (the provider should still remain in the database).")
conn.execute('''DELETE FROM Provides
                     WHERE Provider="RBT"
                     ''')
res10=conn.execute('''SELECT * FROM Provides''')
for row in res10:
   print(row)


conn.close()