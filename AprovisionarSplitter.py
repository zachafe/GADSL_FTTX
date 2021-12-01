import json
import re
#IMPORTAR CLASE
from Main import MainOptions
#LEER ARCHIVO
with open("splitter.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

print("INSERT INTO adsl__recurso ( fk_gestion__tecnologia, fk_gestion__transporte, fk_RMS__uam, fk_gestion__central, fk_gestion__bastidor, tarjeta, puerto, puerto_real, instancia, rack, shelf, slot, res_ubicacion, res_plantside, res_tono, res_combinado, fk_gestion__transporte1, viableFTTH, fk_atributos__estados,estado_causal, creado_por_i, fecha_creacion_i, observaciones, influencia, influenciaJson, splitterJson) VALUES")

# #RECORRER ARCHIVO
# instancia = 1
# for splitters in jsonObject['splitters']:
#     if splitters['subir'] == 1:
#         #for i in range(1,jsonObject['NIVEL_SALIDAS_MAX']+1):
#         for i in range(1,splitters['NIVEL_SALIDAS']+1):
#             #TARJETA
#             tarjeta="0101"+str('%02d' % jsonObject["tarjeta"])
#             instanciaFinal=str(jsonObject['puerto'])+":"+str(instancia)
#             #N1
#             splitterN1=str(jsonObject['NAME_N1'])+":"+str(splitters['POSICION_N1'])
#             #N2
#             splitterN2=str(splitters['NAME_N2'])+":"+str(i)
#             #SPLITTER JSON
#             jsonSplitter='{"N1":{"DIRECCION": "'+jsonObject['DIRECCION']+'","NIVEL": "1-'+str(jsonObject['NIVEL_SALIDAS_MAX'])+'"},"N2":{"DIRECCION": "'+splitters['DIRECCION']+'","NIVEL": "1-'+str(splitters['NIVEL_SALIDAS'])+'"}}'
#             print("({},5,{},{},1,'{}','{}',{},{},1,1,{},'?','{}','{}','{}',5,1,2,0,664,now(),'{}','{}','{}','{}'),".format(
#                 jsonObject["fk_gestion__tecnologia"],
#                 jsonObject["fk_RMS__uam"],
#                 splitters['fk_gestion__central'],
#                 tarjeta,
#                 instanciaFinal,
#                 jsonObject['puerto'],
#                 instancia,
#                 jsonObject['tarjeta'],
#                 jsonObject['res_plantside'],
#                 splitterN1,
#                 splitterN2,
#                 splitters['nombre_proyecto'],
#                 splitters['influencia'],
#                 splitters['jsonInfluencia'],
#                 jsonSplitter
#             ))
#             instancia = instancia + 1
#     else:
#         instancia = instancia + splitters['NIVEL_SALIDAS']

#SUBIR PROYECTO COMPLETO
#N1
for splitterN1 in jsonObject['splitterN1']:
    #INICIAR EL CONTADOR DE LAS INSTANCIAS
    instancia = 1
    #VALIDAR SI EL N1 ESTA PARA SUBIR
    if splitterN1['subir'] == 1:
        #RECORRE N2
        for splitterN2 in splitterN1['splitterN2']:
            #VALIDAR SI EL N2 ESTA PARA SUBIR
            if splitterN2['subir'] == 1:
                for i in range(1,splitterN2['NIVEL_SALIDAS']+1):
                    #TARJETA
                    tarjeta="0101"+str('%02d' % splitterN1["tarjeta"])
                    instanciaFinal=str(splitterN1['puerto'])+":"+str(instancia)
                    #N1
                    splitter_N1=str(splitterN1['NAME_N1'])+":"+str(splitterN2['POSICION_N1'])
                    #N2
                    splitter_N2=str(splitterN2['NAME_N2'])+":"+str(i)
                    #SPLITTER JSON
                    jsonSplitter='{"N1":{"DIRECCION": "'+splitterN1['DIRECCION']+'","NIVEL": "1-'+str(splitterN1['NIVEL_SALIDAS_MAX'])+'"},"N2":{"DIRECCION": "'+splitterN2['DIRECCION']+'","NIVEL": "1-'+str(splitterN2['NIVEL_SALIDAS'])+'"}}'
                    
                    print("({},5,{},{},1,'{}','{}',{},{},1,1,{},'?','{}','{}','{}',5,1,2,0,664,now(),'{}','{}','{}','{}'),".format(
                        jsonObject["fk_gestion__tecnologia"],
                        jsonObject["fk_RMS__uam"],
                        jsonObject['fk_gestion__central'],
                        tarjeta,
                        instanciaFinal,
                        splitterN1['puerto'],
                        instancia,
                        splitterN1['tarjeta'],
                        splitterN1['res_plantside'],
                        splitter_N1,
                        splitter_N2,
                        jsonObject['nombre_proyecto'],
                        splitterN2['influencia'],
                        splitterN2['jsonInfluencia'],
                        jsonSplitter
                    ))
                    instancia = instancia + 1
            else:
                instancia = instancia + splitterN2['NIVEL_SALIDAS']