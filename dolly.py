import json
import re
#IMPORTAR CLASE
from Main import MainOptions
direcciones = [{'direccion':'Cra 3 Nro. 3-91','ciudad':4},
{'direccion':'Cra 6 Nro. 6-11','ciudad':5},
{'direccion':'Cra 3a Diagonal al Banco Agrario','ciudad':6},
{'direccion':'Cra 3 Nro. 5-51','ciudad':7},
{'direccion':'Calle 6 Nro. 4-32 Barrio Centro','ciudad':8},
{'direccion':'Calle 7 y 8 N. 7-36 A 7-40','ciudad':9},
{'direccion':'Cra 6 Nro. 2-26','ciudad':10},
{'direccion':'Cra 8 Nro. 4-43','ciudad':11},
{'direccion':'Cra 1a Nro. 2-84 - Playarrica','ciudad':12},
{'direccion':'Calle 10 Nro. 9-61','ciudad':13},
{'direccion':'Calle 10 Nro. 9-71','ciudad':13},
{'direccion':'Calle 10 Nro. 9-62','ciudad':13},
{'direccion':'Calle 10 Nro. 9-78','ciudad':13},
{'direccion':'Cra 5 Nro. 3-12 Venadillo','ciudad':14},
{'direccion':'Cra 6a Nro. 4-21 - Herveo','ciudad':15},
{'direccion':'Cra 7 Nro. 7-29 - Lerida','ciudad':16},
{'direccion':'Calle 4 Nro. 5-01 - Cunday','ciudad':17},
{'direccion':'Calle 6 Nro. 6-27 - Armero Guayabal','ciudad':18},
{'direccion':'Calle 6 Nro. 6-31 - Armero Guayabal','ciudad':18},
{'direccion':'Calle 6 Nro. 6-35 - Armero Guayabal','ciudad':18},
{'direccion':'Calle 6 Nro. 6-39 - Armero Guayabal','ciudad':18},
{'direccion':'Calle 5 A Esquina con Cra  8A - Villahermosa','ciudad':19},
{'direccion':'Calle 5 Nro. 5-15 - Chicoral','ciudad':20},
{'direccion':'Calle 5 Nro. 5-19 - Chicoral','ciudad':20},
{'direccion':'Carrera 3 Nro. 6-56 - Ortega','ciudad':21},
{'direccion':'Carrera 6 Nro. 4-19 - Icononzo','ciudad':22},
{'direccion':'Carrera 6 Nro. 4-25 - Icononzo','ciudad':22},
{'direccion':'Calle 3 Nro. 2-32 - Coyaima','ciudad':23},
{'direccion':'Carrera 16 Nro. 17-10 - Saldana','ciudad':24},
{'direccion':'Calle 3a Nro. 2-21 Casabianca','ciudad':25},
{'direccion':'Calle 3 Nro. 5-02 centro  -Rioblanco','ciudad':26},
{'direccion':'Cra 6 Nro. 3-03 centro  -Rioblanco','ciudad':26},
{'direccion':'Calle 5 Nro. 6-33 Barrio La Esperanza  - San Luis','ciudad':27},
{'direccion':'Cra 4 Calle 5 Nro. 4-86- Rovira','ciudad':28},
{'direccion':'Cra 4 Calle 5 Nro. 4-98 - Rovira','ciudad':28},
{'direccion':'Cra 7  Calle 3 Esquina Barrio Centro - Dolores','ciudad':29},
{'direccion':'Calle 5 Nro. 8-85 Piso 1 - Libano','ciudad':30},
{'direccion':'Calle 13 Nro. 11-51 - Honda','ciudad':31},
{'direccion':'Calle 13 Nro. 11-61 - Honda','ciudad':31},
{'direccion':'Cra 5 Nro. 8-73 Barrio Carmen - Mariquita','ciudad':32},
{'direccion':'Cra 25 Nro. 7-44 - Melgar','ciudad':33},
{'direccion':'Calle 14 Nro. 2A - 04 Oficina 301 - Ibagué','ciudad':34},
{'direccion':'Calle 9A Nro. 7-46 Edificio - Chaparral','ciudad':35},
{'direccion':'Calle 8 Nro. 5-77 local 2 - Ambalema','ciudad':36},
{'direccion':'Cra 6 Nro. 3-41 - Carmen de Apicala','ciudad':37},
{'direccion':'Cra 6 Nro. 3-49 - Carmen de Apicala','ciudad':37},
{'direccion':'Calle 6 Nro. 6-18 - Purificación','ciudad':38},
{'direccion':'Cra 5 Nro. 40-70 - Ibagué','ciudad':39},
{'direccion':'Cra 5 Nro. 40-71 - Ibagué','ciudad':39},
{'direccion':'Calle 10 Nro. 04-16','ciudad':41},
{'direccion':'Calle 9 Nro.2-40','ciudad':42},
{'direccion':'Calle 14 Nro. 4 - 20  LOCAL COMERCIAL 2 ','ciudad':43},
{'direccion':'Carrera 4 Nro. 14-21 LOCAL COMERCIAL 3','ciudad':43},
{'direccion':'Carrera 7 Nro. 10 -41 Local 2','ciudad':44},
{'direccion':'Cra 3a Nro. 10-16','ciudad':45},
{'direccion':'Cra 3a Nro. 10-22','ciudad':45}]
#print(direcciones)
#RECORRER ARCHIVO
options = MainOptions()
for direccion in direcciones:
     #print(direccion)
     returnOption=json.loads(options.formartAddress(direccion['direccion'],direccion['ciudad']))
     #print(returnOption["responseData"]["dirtrad"])
     print("{},{},{}".format(returnOption["responseData"]['dirtrad'],returnOption["responseData"]['longitud'],returnOption["responseData"]['latitud']))
     