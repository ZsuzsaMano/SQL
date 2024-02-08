import sqlite3

conn = sqlite3.connect('Day8.db')

print("\n 8.1 Obtain the names of all physicians that have performed a medical procedure they have never been certified to perform.")
res1 = conn.execute('''SELECT DISTINCT Physician.name, Undergoes.procedure
                        FROM Physician 
                        JOIN Undergoes 
                        ON Physician.EmployeeID = Undergoes.Physician
                        WHERE Undergoes.procedure NOT IN (
                           SELECT Trained_In.treatment
                           FROM Trained_In
                           WHERE Trained_In.Physician = Physician.EmployeeID);
                                          ''')
for row in res1:
   print(row) 
   
   
print("\n 8.2 Same as the previous query, but include the following information in the results: Physician name, name of procedure, date when the procedure was carried out, name of the patient the procedure was carried out on.")
res2 = conn.execute('''SELECT DISTINCT Physician.name, procedures.name, Undergoes.date, patient.name
                        FROM Physician 
                        JOIN Undergoes 
                        ON Physician.EmployeeID = Undergoes.Physician
                        JOIN procedures
                        ON undergoes.procedure=procedures.code
                        JOIN patient
                        ON Undergoes.patient=patient.ssn
                        WHERE Undergoes.procedure NOT IN (
                           SELECT Trained_In.treatment
                           FROM Trained_In
                           WHERE Trained_In.Physician = Physician.EmployeeID);
                                          ''')
for row in res2:
   print(row) 

print("\n 8.3 Obtain the names of all physicians that have performed a medical procedure that they are certified to perform, but such that the procedure was done at a date (Undergoes.Date) after the physician's certification expired (Trained_In.CertificationExpires).")
res3 = conn.execute('''SELECT Physician.name, procedure, treatment, undergoes.date, trained_in.CertificationExpires
                       FROM Physician
                       JOIN Undergoes
                       ON Physician.EmployeeID=Undergoes.Physician
                       JOIN Trained_In
                       ON Physician.EmployeeID=Trained_In.Physician 
                       WHERE treatment=procedure   
                       AND DATE(undergoes.date) > DATE(trained_in.CertificationExpires)          
                      ''')
for row in res3:
   print(row) 

print("\n 8.4 Same as the previous query, but include the following information in the results: Physician name, name of procedure, date when the procedure was carried out, name of the patient the procedure was carried out on, and date when the certification expired.")
res3 = conn.execute('''SELECT Physician.name, procedures.name, undergoes.date, patient.name, trained_in.CertificationExpires
                       FROM Physician
                       JOIN Undergoes
                       ON Physician.EmployeeID=Undergoes.Physician
                       JOIN Trained_In
                       ON Physician.EmployeeID=Trained_In.Physician 
                       JOIN procedures
                       ON undergoes.procedure=procedures.code
                       JOIN patient
                       ON Undergoes.patient=patient.ssn
                       WHERE treatment=procedure   
                       AND DATE(undergoes.date) > DATE(trained_in.CertificationExpires)          
                      ''')
for row in res3:
   print(row) 

print("\n 8.5 Obtain the information for appointments where a patient met with a physician other than his/her primary care physician. Show the following information: Patient name, physician name, nurse name (if any), start and end time of appointment, examination room, and the name of the patient's primary care physician.")
res5 = conn.execute('''SELECT patient.name,Physician.name,Nurse.name, start, end, examinationRoom, PCP.name
                       FROM Appointment
                       JOIN Patient
                       ON Appointment.Patient=Patient.SSN
                       JOIN Physician
                       ON Physician.EmployeeID=Appointment.Physician  
                       JOIN Physician as PCP
                       ON PCP.EmployeeID=Patient.PCP
                       LEFT JOIN Nurse
                       ON Appointment.PrepNurse=Nurse.EmployeeID
                       WHERE PCP!=Appointment.Physician
                      ''')
for row in res5:
   print(row) 

print("\n 8.6 The Patient field in Undergoes is redundant, since we can obtain it from the Stay table. There are no constraints in force to prevent inconsistencies between these two tables. More specifically, the Undergoes table may include a row where the patient ID does not match the one we would obtain from the Stay table through the Undergoes.Stay foreign key. Select all rows from Undergoes that exhibit this inconsistency. ")
res6 = conn.execute('''SELECT *
                       FROM Undergoes
                       JOIN Stay
                       ON Stay.StayID=Undergoes.Stay
                       WHERE stay.patient!=undergoes.patient       
                      ''')
for row in res6:
   print(row) 

print("\n 8.7 Obtain the names of all the nurses who have ever been on call for room 123.")
res7 = conn.execute('''SELECT  Nurse.name, Room.Number
                       From Room
                       JOIN Block 
                       ON Room.BlockFloor=Block.Floor
                       AND Room.BlockCode=Block.Code
                       JOIN On_Call
                       ON On_Call.BlockFloor=Block.Floor
                       AND On_Call.BlockCode=Block.Code
                       JOIN Nurse
                       ON On_Call.Nurse=Nurse.EmployeeID  
                       WHERE Room.Number=123     
                      ''')

for row in res7:
   print(row) 


print("\n 8.8 The hospital has several examination rooms where appointments take place. Obtain the number of appointments that have taken place in each examination room. ")
res8 = conn.execute('''SELECT ExaminationRoom, COUNT(ExaminationRoom)
                       FROM Appointment
                       GROUP BY ExaminationRoom                     
                      ''')
for row in res8:
   print(row) 

print("\n 8.9 Obtain the names of all patients and their primary care physician, such that the following are true:")
print("\n 8.9.1 The patient has been prescribed some medication by his/her primary care physician.")
res9 = conn.execute('''SELECT patient.name,  Physician.name, PCP.name
                       FROM Prescribes
                       JOIN Patient
                       ON Prescribes.Patient=Patient.SSN
                       JOIN Physician
                       ON Physician.EmployeeID=Prescribes.Physician   
                       JOIN Physician as PCP
                       ON PCP.EmployeeID=Patient.PCP
                       WHERE Physician.name=PCP.name      
                      ''')
for row in res9:
   print(row) 
   
print("\n 8.9.2 The patient has undergone a procedure with a cost larger that $5,000")
res9 = conn.execute('''SELECT patient.name,  Physician.name, cost
                       FROM Undergoes
                       JOIN Patient
                       ON Undergoes.Patient=Patient.SSN
                       JOIN Physician
                       ON Physician.EmployeeID=Patient.PCP 
                       JOIN Procedures
                       ON Undergoes.Procedure=Procedures.code
                       WHERE cost>5000
                      ''')
for row in res9:
   print(row) 

print("\n 8.9.3 The patient has had at least two appointments where the nurse who prepared the appointment was a registered nurse.")
res9 = conn.execute('''SELECT patient.name, Physician.name, nurse.name
                       FROM Appointment
                       JOIN Patient
                       ON Appointment.Patient=Patient.SSN
                       JOIN Physician
                       ON Physician.EmployeeID=Patient.PCP  
                       JOIN Nurse
                       ON Appointment.PrepNurse=Nurse.EmployeeID
                       WHERE Nurse.registered=1
                       GROUP BY patient.name
                       HAVING COUNT(patient.name)>=2
                   
                      ''')
for row in res9:
   print(row) 

print("\n 8.9.4 The patient's primary care physician is not the head of any department.")
res9 = conn.execute('''SELECT patient.name,  Physician.name, head
                       FROM Patient
                       JOIN Physician
                       ON Physician.EmployeeID=Patient.PCP
                       LEFT JOIN Department
                       ON Physician.EmployeeID=Department.Head 
                       WHERE head IS NULL             
                      ''')
for row in res9:
   print(row) 
   

conn.close()
