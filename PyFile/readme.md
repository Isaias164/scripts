Pyfile es un script que organiza los archivos de una o varias carpetas. Para ello organiza los archivos en base a la extensión del archivo. Dependiendo del delay que le has asignado al bajar un archivo, este puede estar en la carpeta con la extension del archivo. Tambien puede eliminar los archivos repetidos.


**Archivo config.json**

Este contiene la configuración del funcionameinto del script.

**directorios**: Es una lista de cadenas de directorios donde va a ordenar y/o borrar aquellos archivos repetidos. Reemplaza los \ por \\ cuando escrivas tus rutas.

**event**: contiene *repeat* y *delay*. **repeat** determina si infinamente se ordenan los archivos de los directorios. repeat almacena 2 valores 0=el script se ejecuta una sola vez 1=ordena los archivos en bucle.
**delay** determina el tiempo de espera que debe pasar para ordenar los directorios.

**delete**: Si los archivos que intestas mover en las carpetas creadas y delete esta puesto a 1 lo que va hacer es no mover esos archivos repetidos sino que lo va a eliminar. Si esta puesto a 0 deja los archivos repetidos en la misma carpeta de donde queria ser movido.



