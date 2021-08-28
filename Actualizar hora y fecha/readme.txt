Problema:
La computadora de un familiar tiene la pila de litio agotada. Por diferentes motivos no ha enviado a cambiarla. Esta pila almacena la configuraci�n de la hora y fecha del sistema. Si la hora y/o la fecha est�n mal, el navegador no le devuelve ninguna p�gina.

Soluci�n:
Utilice la api de timezonedb.
Es obligatorio que en cada petici�n env�es una key que se genera al darte de alta en la aplicaci�n. Por ende te sugiero que primero te logues en timezonedb y despu�s reemplaces mi key por la tuya. S� el script no funciona es por esto.

Api https://timezonedb.com/api
El timezone de la Argentina:  https://timezonedb.com/time-zones/America/Argentina/Buenos_Aires

Conclusi�n:
Sin la api mi familiar ten�a que hacer 7 clips para actualizar la hora y fecha en su equipo Windows. 
Ahora tiene que hacer un solo clic y ya tiene actualizada la hora y fecha. Esto es una soluci�n parcial, deber�a mandar arreglar esa pila?. 
Ese script puede colocarse como un servicio o podemos modificar la clave del sistema para que el script se ejecute al iniciar el sistema.
