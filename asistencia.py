import pandas as pd
from pathlib import Path
assist_crit = 45
late = {}
working_dir = Path('__file__').resolve().parent
output_dir = working_dir.joinpath('attendance')
bk_dir = working_dir.joinpath('bakckup')
students_file_dir = working_dir.joinpath('students.csv')
attendance_file_dir = working_dir.joinpath('attendance.csv')
try:
    #Script para leer el archivo de los estudiantes y almacenarlos en una lista
    students = pd.read_csv(students_file_dir)
    attendance = pd.read_csv(attendance_file_dir, usecols=['Username', 'Total time'])
    #Script que lee la asistencia, corrobora si ese estudiante asistió, si asistió lo saca de la
    #lista de estudiantes previamente definida. Los estudiantes que permanezcan en esa lista, no asistieron
    #Adicionalmente corrobora si duró mas de 45 minutos, si no, la consola mostrara un mensaje informadolo.

    assisted = pd.merge(students, attendance, how='inner', on=['Username','Username'])
    #hh:mm:ss a min
    assisted['Total time'] = assisted['Total time'].apply(lambda x: sum([a*b for a,b in zip(list(map(int,x.split(':')))[::-1],[1/60,1,60])]))
    #agrego los estudiantes que no asistieron y relleno sus valores nan con 0
    assisted = pd.merge(students,assisted, how='left', on=['Username','Username'])
    assisted = assisted.fillna(0)
    tmpAssist = []
    for i,student in assisted.iterrows():
        if student['Total time'] > assist_crit:
            tmpAssist.append('X')
        else: 
            tmpAssist.append('O')
    #la lista de x y o que representan la asistencia de un estudiante
    xno = pd.DataFrame(tmpAssist)

    assisted['attend'] = xno.values
    # imprimo aquellos que no cumplan con el criterio o aquellos que no asistieron
    for i, student in assisted.iterrows():
        if student['Total time'] < assist_crit:
            print('El estudiante {} asistio con un tiempo de {} lo cual implica falla'.format(student['Username'],student['Total time']))


except Exception as e:
    print('xuxa')
    print(str(e))
