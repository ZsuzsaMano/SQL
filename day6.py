import sqlite3

conn = sqlite3.connect('Day6.db')

print("\n6.1 List all the scientists' names, their projects' names and the total hours worked on each project in alphabetical order of scientist name")
res1=conn.execute('''SELECT Scientists.name, Projects.name, Projects.hours
                    FROM AssignedTo
                    JOIN Scientists
                    ON  Scientists.SSN=AssignedTo.Scientist
                    JOIN Projects 
                     ON Projects.Code=AssignedTo.Project
                    ORDER BY Scientists.name''')
for row in res1:
   print(row)
   

print("\nin alphabetical order of project name")
res1=conn.execute('''SELECT Projects.name, Scientists.name, Projects.hours
                    FROM AssignedTo
                    JOIN Scientists
                    ON  Scientists.SSN=AssignedTo.Scientist
                    JOIN Projects 
                    ON Projects.Code=AssignedTo.Project
                    ORDER BY Projects.name''')
for row in res1:
   print(row)
   
print("\n6.2 Select the project names which are not assigned yet")
res2=conn.execute('''SELECT Projects.name
                    FROM Projects
                   EXCEPT SELECT Projects.name
                    FROM Projects
                    RIGHT JOIN AssignedTo 
                    ON Projects.Code=AssignedTo.Project
                                     
                   ''')
for row in res2:
   print(row)

conn.close()