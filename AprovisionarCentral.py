import json
import re
#IMPORTAR CLASE
from Main import MainOptions
#LEER ARCHIVO
with open("central.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
print("INSERT INTO gestion__central (id__central,nombre_central,indoor,nemonico,fk_atributos__ciudades,zona,sector,sector_aux,direccion,position,RTA_GEOCODE,BARRIO,COMUNA,DIR_NORM,formato_ldap,distribuidor,central_padre,zona_central,fk_atributos__estados,creado_por_i,fecha_creacion_i,modificado_por_i,fecha_modificacion_i,observaciones,influencia,DIR_NORM_REGEXP,fttx,s_venta,s_instale) VALUES")
patternComuna = '^\w+\s+(\d+)$'
#RECORRER ARCHIVO
for central in jsonObject['centrales']:
    options = MainOptions()
    returnOption=json.loads(options.formartAddress(central['direccion'],central['fk_atributos__ciudades']))
    comuna = 0
    executeRegexp = re.search(patternComuna,returnOption["responseData"]["localidad"])
    #VALIDAR QUE NO VENGA VACIO LA COMUNA
    if executeRegexp is not None:
        comuna = executeRegexp.group(1)
    print("({},'{}',0,'',{},'{}',{},0,'{}',NULL,0,'{}','{}','{}','FTTH','?',{},{},2,1,now(),1,now(),'{}',{},'{}',1,{},{}),".format(
            central['id'],
            central['nombre_central'],
            central['fk_atributos__ciudades'],
            central['zona'],
            central['sector'],
            returnOption["responseData"]["dirtrad"],
            returnOption["responseData"]["barrio"],
            comuna,
            returnOption["responseData"]["dirtrad"],
            central['central_padre'],
            central['zona_central'],
            central['nombre_central'],
            central['influencia'],
            returnOption["responseData"]["dirtrad"],
            central['s_venta'],
            central['s_instale']
        ))


