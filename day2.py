import sqlite3

conn = sqlite3.connect('Day1.db')

print('Opened database successfully')

# create tables
conn.execute('''CREATE TABLE IF NOT EXISTS Departments (
Code INTEGER,
Name TEXT NOT NULL,
Budget decimal NOT NULL,
PRIMARY KEY (Code)
);
''')
print( "Departments Table created successfully")

conn.execute('''
CREATE TABLE IF NOT EXISTS Employees (
SSN INTEGER,
Name varchar(255) NOT NULL ,
LastName varchar(255) NOT NULL ,
Department INTEGER NOT NULL ,
PRIMARY KEY (SSN)
);''')
print( "Employees Table created successfully")

dep_data=[(14,'IT',65000),
(37,'Accounting',15000),
(59,'Human Resources',240000),
(77,'Research',55000)]

conn.executemany('''INSERT INTO Departments VALUES(?, ?, ?)''', dep_data)
print( "Populated Departments Table successfully")


empl_data=[('123234877','Michael','Rogers',14),
('152934485','Anand','Manikutty',14),
('222364883','Carol','Smith',37),
('326587417','Joe','Stevens',37),
('332154719','Mary-Anne','Foster',14),
('332569843','George','ODonnell',77),
('546523478','John','Doe',59),
('631231482','David','Smith',77),
('654873219','Zacary','Efron',59),
('745685214','Eric','Goldsmith',59),
('845657245','Elizabeth','Doe',14),
('845657246','Kumar','Swamy',14)
]

conn.executemany('''INSERT INTO Employees VALUES(?, ?, ?,?)''', empl_data)
print( "Populated Employees Table successfully")



res0=conn.execute('SELECT * FROM Employees')
for row in res0:
   print(row)

# 2.1 Select the last name of all employees.
print( "Last name of all employees")
res1 = conn.execute('SELECT LastName FROM Employees')
for row in res1:
   print(row)

# 2.2 Select the last name of all employees, without duplicates.
print( "Unique Last name of all employees")
res2 = conn.execute('SELECT DISTINCT LastName FROM Employees')
for row in res2:
   print(row)

# 2.3 Select all the data of employees whose last name is "Smith".
print( "Smith")
res3 = conn.execute('SELECT * FROM Employees WHERE LastName="Smith"')
for row in res3:
   print(row)

# 2.4 Select all the data of employees whose last name is "Smith" or "Doe".
print( "Smith or Doe")
res4 = conn.execute('SELECT * FROM Employees WHERE LastName="Smith" OR LastName="Doe"')
for row in res4:
   print(row)

# 2.5 Select all the data of employees that work in department 14.
print( "Dep 14")
res5 = conn.execute('SELECT * FROM Employees WHERE department=14')
for row in res5:
   print(row)

# 2.6 Select all the data of employees that work in department 37 or department 77.
print( "Dep 37 or 77")
res6 = conn.execute('SELECT * FROM Employees WHERE department=37 OR department=77')
for row in res6:
   print(row)

# 2.7 Select all the data of employees whose last name begins with an "S".
print( "S...")
res7 = conn.execute('SELECT * FROM Employees WHERE LastName LIKE "S%"')
for row in res7:
   print(row) 

# 2.8 Select the sum of all the departments' budgets.
print( "Budget SUM")
res8 = conn.execute('SELECT SUM(budget) FROM Departments')
for row in res8:
   print(row) 

# 2.9 Select the number of employees in each department (you only need to show the department code and the number of employees).
print( "Employee per department")
res9 = conn.execute('SELECT COUNT(name), department FROM Employees GROUP BY department')
for row in res9:
   print(row) 

# 2.10 Select all the data of employees, including each employee's department's data.
print( "Employee and department full data")
res10 = conn.execute('SELECT * FROM Employees JOIN departments ON Employees.Department=departments.code')
for row in res10:
   print(row) 

# 2.11 Select the name and last name of each employee, along with the name and budget of the employee's department.
print( "Employee and department data")
res11 = conn.execute('SELECT Employees.name, Employees.LastName, departments.name, departments.budget FROM Employees JOIN departments ON Employees.Department=departments.code')
for row in res11:
   print(row) 

# 2.12 Select the name and last name of employees working for departments with a budget greater than $60,000.
print( "Employee and department data")
res12 = conn.execute('SELECT Employees.name, Employees.LastName FROM Employees JOIN departments ON Employees.Department=departments.code WHERE budget>60000')
for row in res12:
   print(row) 

# 2.13 Select the departments with a budget larger than the average budget of all the departments.
print( "Budget higher than Avarage")
res13 = conn.execute('''SELECT * 
                        FROM Departments
                        WHERE budget>(SELECT AVG(budget) 
                        FROM Departments)''')
for row in res13:
   print(row) 

# 2.14 Select the names of departments with more than two employees.
print( "department with 2+ employee")
res14 = conn.execute('''SELECT department
                        FROM Employees 
                        GROUP BY department HAVING COUNT(name)>2''')
for row in res14:
   print(row) 
# 2.15 Select the name and last name of employees working for the two departments with lowest budget.
# 2.16  Add a new department called "Quality Assurance", with a budget of $40,000 and departmental code 11. 
# And Add an employee called "Mary Moore" in that department, with SSN 847-21-9811.
# 2.17 Reduce the budget of all departments by 10%.
# 2.18 Reassign all employees from the Research department (code 77) to the IT department (code 14).
# 2.19 Delete from the table all employees in the IT department (code 14).
# 2.20 Delete from the table all employees who work in departments with a budget greater than or equal to $60,000.
# 2.21 Delete from the table all employees.



conn.close()