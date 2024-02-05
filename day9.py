import sqlite3

conn = sqlite3.connect('Day9.db')

conn.execute('''UPDATE cran_logs
            SET
                    download_date = REPLACE(download_date,'"','')''');
conn.execute('''UPDATE cran_logs
            SET
                    ip_id = REPLACE(ip_id,'"','')''');


print("\n 9.1 Give the package name and how many times they're downloaded. Order by the 2nd column descending.")
res1 = conn.execute('''SELECT package, COUNT(package)
                       FROM cran_logs
                       GROUP BY package
                       ORDER BY COUNT(package) DESC
                        ''')
for row in res1:
   print(row) 
   
print("\n 9.2 Give the package ranking (based on how many times it was downloaded) during 9AM to 11AM")
res2 = conn.execute('''SELECT package, COUNT(package)
                       FROM cran_logs
                       GROUP BY package
                       HAVING time>TIME('09:00:00') AND time<TIME('11:00:00')
                        ''')
for row in res2:
   print(row) 
   
print("\n 9.3 How many records (downloads) are from China (CN) or Japan(JP) or Singapore (SG)?")
res3 = conn.execute('''SELECT country, COUNT(country)
                       FROM cran_logs
                       GROUP BY country
                       HAVING country='CN' OR  country='JP' OR country='SG'
                        ''')
for row in res3:
   print(row) 
   

res32 = conn.execute('''SELECT COUNT(package)
                       FROM cran_logs
                       WHERE country='CN' OR  country='JP' OR country='SG'
                        ''')
for row in res32:
   print(row) 
# print("\n 9.4 Print the countries whose downloads are more than the downloads from China (CN)")
# print("\n 9.5 Print the average length of the package name of all the UNIQUE packages")
# print("\n 9.6 Get the package whose download count ranks 2nd (print package name and its download count).")
# print("\n 9.7 Print the name of the package whose download count is bigger than 1000.")
# print("\n 9.8 The field r_os is the operating system of the users.")
 #	Here we would like to know what main system we have (ignore version number), the relevant counts, and the proportion (in percentage).

conn.close()