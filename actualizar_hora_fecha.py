from requests import get
fecha = get(url="http://api.timezonedb.com/v2.1/get-time-zone?key=2MMX5TN0QFNV&format=json&by=zone&zone=America/Argentina/Buenos_Aires")
my_fecha = fecha.json()["formatted"].split()
from os import system
fecha = my_fecha[0].split("-")
fecha = "{0}-{1}-{2}".format(fecha[-1],fecha[1],fecha[0])
system(f"date "+fecha)
system(f"time "+my_fecha[1])
