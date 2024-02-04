import sqlite3

conn = sqlite3.connect('Day10.db')

print("\n 10.1 Join table PEOPLE and ADDRESS, but keep only one address information for each person (we don't mind which record we take for each person). ")
    # i.e., the joined table should have the same number of rows as table PEOPLE

res1 = conn.execute('''SELECT *
                        FROM PEOPLE 
                        JOIN ADDRESS
                        ON PEOPLE.id=ADDRESS.id
                        GROUP BY name
                        ''')
for row in res1:
   print(row) 

print("\n 10.2 Join table PEOPLE and ADDRESS, but ONLY keep the LATEST address information for each person. ")
    # i.e., the joined table should have the same number of rows as table PEOPLE

res1 = conn.execute('''SELECT name, MAX(updatedate), address
                        FROM PEOPLE 
                        JOIN ADDRESS
                        ON PEOPLE.id=ADDRESS.id
                        GROUP BY name
                        ''')
for row in res1:
   print(row) 

conn.close()
