# ScriptAsistencia

Este script ayuda a tomar asistencia basado en csv. A continuación explicaré su uso paso a paso.

1) Entras a clase remota, en la parte derecha de la sesión de clase ingresar a opciones de la sesión (Boton con 3 puntos).
2) Hacer click en ver informes y entrar al informe del día que quieres tomar asistencia.
3) En la parte izquierda donde dice herramientas, dar click en exportar a csv, eso te descargará el archivo csv correspondiente a dicha sesión.
4) Cambiar el nombre del archivo a "attendance" y guardarlo en la misma carpeta de este script.
5) Ingresar a consola, despues en la consola ingresa al directorio que contiene el script.
6) Ejecutar el comando:  
``python 
python asistencia.py [option]``

 * donde option puede ser: -p, -bk o vacio
   * con -p se imprime la tabla de asistencia en la terminal con el usuario, tiempo total y asistencia  
   * con -bk se crea persistentemente un xlsx donde se tiene guardada la info de la asistencia, ademas de guardar      * una copia del attendance.csv con la fecha
   * con el paramentro vacio se obtienen los usuario y el tiempo que estuvieron en clase de aquellos estudiantes que no cumplan con el criterio de asistencia (45 minutos por defecto)

# Comentarios adicionales

- Cada vez que vayas a tomar asistencia, debes seguir el mismo procedimiento anterior, se recomienda usar el comando -bk para evitar perdidas de informacion
- El archivo students son los nombres de usuarios de los estudiantes de x seccion por lo que no debe eliminarse, pero puede reemplazarse a necesidad.
- los headers en los csvs son completamente necesarios, principalmente el de students.csv
