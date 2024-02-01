import sqlite3

conn = sqlite3.connect('Day4.db')


# 4.1 Select the title of all movies.
print('\n all movies')
res1=conn.execute('SELECT * FROM Movies')
for row in res1:
   print(row)
   
# 4.2 Show all the distinct ratings in the database.
print('\n distinct ratings')
res2=conn.execute('SELECT DISTINCT rating FROM Movies')
for row in res2:
   print(row)
   
# 4.3 Show all unrated movies.
print('\n unrated')
res3=conn.execute('''SELECT *  
                  FROM Movies
                  WHERE rating IS NULL''')
for row in res3:
   print(row)

# 4.4 Select all movie theaters that are not currently showing a movie.
print('\n movie theater no movie')
res4=conn.execute('''SELECT *  
                  FROM MovieTheaters
                  WHERE movie IS NULL''')
for row in res4:
   print(row)
   
# 4.5 Select all data from all movie theaters and, additionally, the data from the movie that is being shown in the theater (if one is being shown).
print('\n movie theater + movie')
res5=conn.execute('''SELECT *  
                  FROM MovieTheaters
                  LEFT JOIN Movies
                  ON MovieTheaters.movie=Movies.code
                  ''')
for row in res5:
   print(row)
   
# 4.6 Select all data from all movies and, if that movie is being shown in a theater, show the data from the theater.
print('\n movie + theater')
res6=conn.execute('''SELECT *  
                  FROM Movies
                  RIGHT JOIN MovieTheaters
                  ON MovieTheaters.movie=Movies.code
                                   ''')
for row in res6:
   print(row)
# 4.7 Show the titles of movies not currently being shown in any theaters.
print('\n movie not shown in theater')
res7=conn.execute('''SELECT *  
                  FROM Movies
                  LEFT JOIN MovieTheaters
                  ON MovieTheaters.movie=Movies.code
                  WHERE Name IS NULL
                                   ''')
for row in res7:
   print(row)
   
# 4.8 Add the unrated movie "One, Two, Three".
print(" \n add movie")
conn.execute('''INSERT INTO Movies 
             VALUES(9, 'One, Two, Three', null);''')
res8=conn.execute('SELECT * FROM Movies')
for row in res8:
   print(row)
# 4.9 Set the rating of all unrated movies to "G".
print(" \n unrated to G")
conn.execute('''UPDATE Movies 
                SET rating="G"
                WHERE rating IS NULL
                ;''')
res9=conn.execute('SELECT * FROM Movies')
for row in res9:
   print(row)
   
# 4.10 Remove movie theaters projecting movies rated "NC-17".
print(" \n delete theater with NC_17")
conn.execute('''DELETE FROM MovieTheaters
                WHERE EXISTS
                ( SELECT *
                    FROM Movies
                    WHERE Movies.rating = "NC-17" );
                                ;''')
res10=conn.execute('SELECT * FROM MovieTheater')
for row in res10:
   print(row)


   
conn.close()
