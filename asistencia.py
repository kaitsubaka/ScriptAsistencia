import csv

late = {}
students = []

#Script para leer el archivo de los estudiantes y almacenarlos en una lista
with open('students.csv') as students_file:
    csv_students = csv.reader(students_file, delimiter=',')
    for row in csv_students:
        students.append(row[0])

#Script que lee la asistencia, corrobora si ese estudiante asistió, si asistió lo saca de la
#lista de estudiantes previamente definida. Los estudiantes que permanezcan en esa lista, no asistieron
#Adicionalmente corrobora si duró mas de 45 minutos, si no, la consola mostrara un mensaje informadolo.
try:
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
except:
    print("Error con la lectura del archivo, recuerda que el nombre debe ser: attendance")
for student in students:
    print("El estudiante ", student, "No asistió a la clase")
