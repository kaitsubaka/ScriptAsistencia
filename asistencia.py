import pandas as pd
from pathlib import Path
import sys
#minutos que definen el criterio de inasistencia
assist_crit = 45

#directorios y archivos
working_dir = Path('__file__').resolve().parent
output_dir = working_dir.joinpath('attendance')
bk_dir = working_dir.joinpath('bakckup')
students_file_dir = working_dir.joinpath('students.csv')
attendance_file_dir = working_dir.joinpath('attendance.csv')

#main script
def main(argv):
    try:
        #Lectura de csvs en dataframes
        students = pd.read_csv(students_file_dir)
        attendance = pd.read_csv(attendance_file_dir, usecols=['Username', 'Total time'])
        # genero la tabla de los estudiantes que asistieron
        response = pd.merge(students, attendance, how='inner', on=['Username','Username'])
        #hh:mm:ss a min
        response['Total time'] = response['Total time'].apply(lambda x: sum([a*b for a,b in zip(list(map(int,x.split(':')))[::-1],[1/60,1,60])]))
        #agrego los estudiantes que no asistieron y relleno sus valores nan con 0
        response = pd.merge(students,response, how='left', on=['Username','Username'])
        response = response.fillna(0)
        tmpXnOlist = []
        for i,student in response.iterrows():
            if student['Total time'] > assist_crit:
                tmpXnOlist.append('X')
            else: 
                tmpXnOlist.append('O')

        #la lista de x y o que representan la asistencia de un estudiante
        xno = pd.DataFrame(tmpXnOlist)

        response['attend'] = xno.values
        # imprimo aquellos que no cumplan con el criterio o aquellos que no asistieron
        if len(argv) <= 1:
            for i, student in response.iterrows():
                if student['Total time'] < assist_crit:
                    print('El estudiante: {} asistio con un tiempo de: {} min lo cual implica falla'.format(student['Username'],student['Total time']))
        elif argv[1] == '-bk':
            #TODO: implementar los metodos de backup del attendace original y el output en xlsx para solo tener que hacer ctl +  c y ctl + v
            #ademas de el metodo eliminar el archivo de attendance para dejarlo listo para otra ejecucion
            pass
        elif argv[1] == '-p' or argv[1] == '-P':
            print(response)
        else:
            print('Opcion no soportada')



    except Exception as e:
        print('error: ' + str(e))

#main lock
if __name__ == '__main__':
    main(sys.argv)
