import csv

late = {}
students = []

with open('students.csv') as students_file:
    csv_students = csv.reader(students_file, delimiter=',')
    for row in csv_students:
        students.append(row[0])
   
with open('attendance.csv') as attendance_file:
    csv_attendance = csv.reader(attendance_file, delimiter=',')
    header = True
    for row in csv_attendance:
        if header:
            header = False
            continue
        login = row[1]
        try:
            students.remove(login)
        except:
            print("La persona "+row[0]+" no es estudiante de esta seccion")
        time = row[6].split(':')
        minutes = int(time[0])*60+int(time[1])*1
        if minutes < 45:
            print("El estudiante", row[0], "asitió pero solo estuvo ",minutes," Minutos")
        
            
for student in students:
    print("El estudiante ", student, "No asistió a la clase")
    



        
    