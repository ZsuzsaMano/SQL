import sqlite3

conn = sqlite3.connect('Day7.db')

print("\n 7.1 Who received a 1.5kg package?")
res1 = conn.execute('''SELECT Client.name
                        FROM Package 
                        JOIN Client
                        ON Package.recipient=Client.AccountNUmber
                        WHERE Weight=1.5''')
for row in res1:
   print(row) 

print("\n 7.2 What is the total weight of all the packages that he sent")
res2 = conn.execute('''SELECT SUM(Weight)
                        FROM Package 
                        JOIN Client
                        ON Package.recipient=Client.AccountNUmber
                        WHERE name="Al Gore's Head"''')
for row in res2:
   print(row) 


conn.close()