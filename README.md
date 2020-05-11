# PP_hw_teoria_11052020
tarea python plus entrega 11/05/2020


Python Plus: set de juegos con archivos
Victoria Hipatia Olivera Craig
11/05/2020

Archivos adjuntos:

python_plus_craig_08052020.py
hangman.py
reversegam.py
tictactoeModificado.py


Estructura de Datos:

Al correr el programa se abre una ventana que solicita al usuario ingresar el nombre y la edad, decidí a su vez agregar una ventana de visualización de datos y edad mientras no se haya decidido salir del mismo (sin ingresar la opción "vuelvo más tarde" varios usuarios con distintas edades pueden elegir jugar distintos juegos). 
Mientras no se elija salir, la ventana seguirá activa permitiendo al/a los usuario/usuarios utilizar el menú e ir a la consola a jugar el juego que haya/n elegido.
Una vez que se haya elegido salir se generará un archivo donde los datos del/ de los usuario/s y los juegos que eligió/eligieron jugar quedarán guardados.

Formato de archivo de salida:

Elegí en esta oportunidad utilizar ".csv" debido a que consideré este tipo de archivo de salida uno que a diferencia de json u otros similares me permite, sin utilizar herramientas como python, leerlo y levantar el dato para hacer otro tipo de cálculos. Cualquier persona que quiera acceder al dato guardado lo puede leer fácilmente. Si bien consideré que el archivo de salida fuera ".txt", me pareció que provablemente quien fuera a buscar los datos guardados querría hacer cálculos sobre los mismos (de tenerlos en archivo de texto debería importar los mismos a una tabla, de esta forma ya los tiene en una tabla).

Problemas sin resolver y dudas:

Si bien el programa parece andar sin problemas no logré solucionar el problema de que me deje un fila vacía entre filas llenas ingresadas. 
Una solución que encontré hablando con compañeros y buscando en la web fue la de generar otro código que elimine filas vacías del csv, sin embargo estoy segura de que se debe poder solucionar fácil en el mismo código. ¿Dónde está el problema?

Desde ya muchísimas gracias.

Buena semana!

Victoria
