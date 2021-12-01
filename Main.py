import urllib.parse
import urllib.request
class MainOptions:
    
    #PARCEAR DIRECCIONES
    def formartAddress(self,address,cityId):
        ciudades={
                    1:'Cali',
                    2:'Jamundi',
                    3:'Yumbo',
                    4:'Alvarado',
                    5:'Planadas',
                    6:'Roncesvalles',
                    7:'Villarrica',
                    8:'ValleDeSanJuan',
                    9:'Fresno',
                    10:'Natagaima',
                    11:'Cajamarca',
                    12:'Playarrica',
                    13:'Guamo',
                    14:'Venadillo',
                    15:'Herveo',
                    16:'Lerida',
                    17:'Cunday',
                    18:'Armero',
                    19:'Villahermosa',
                    20:'Chicoral',
                    21:'Ortega',
                    22:'Icononzo',
                    23:'Coyaima',
                    24:'Saldana',
                    25:'Casabianca',
                    26:'Rioblanco',
                    27:'SanLuis',
                    28:'Rovira',
                    29:'Dolores',
                    30:'Libano',
                    31:'Honda',
                    32:'Mariquita',
                    33:'Melgar',
                    34:'Ibague',
                    35:'Chaparral',
                    36:'Ambalema',
                    37:'CarmenDeApicala',
                    38:'Purificacion',
                    39:'Ibague',
                    40:'Libano',
                    41:'Espinal',
                    42:'Lerida',
                    43:'Ibague',
                    44:'Guamo',
                    45:'Anzoategui'
                }
        #PARCEAR LA DIRECCION PARA ENVIARLAR POR URL
        stringFormatAddress=urllib.parse.quote_plus(address)
        #CREAR URL
        url="http://servidorweb1.sitimapa.com/webservices/Bavaria/getData.php?servicio=traerPorGeoDirecto&usr=Bavaria&pwd=8efcas*dAA&direccion="+stringFormatAddress+"&ciudad="+ciudades.get(cityId)
        salida=urllib.request.urlopen(url).read(1000)
        return salida
        
