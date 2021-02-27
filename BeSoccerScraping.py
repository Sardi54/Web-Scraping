from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

import csv
import sqlite3



jornada = int(input("Jornada: "))
if jornada <= 0 or jornada >= 39:
        print("Jornada entre la 1 - 38")
        
'''
def error():
    pass

def final():
    global jornada
    jornada = int(input("(func final)  Jornada: "))
    if jornada <= 0 or jornada >= 39:
        print("Jornada entre la 1 - 38")
        error()
      '''  

#jornada = 1
# CODIGO EJECUCION :   scrapy runspider BeSoccerScraping.py -o BeSoccer.csv -t csv
class Articulo(Item):
    Equipos = Field()
    Datos = Field()
    Tipo = Field()

class MercadoLibreCrawler(CrawlSpider):
    name = "SegundoSpider"
    custom_settings = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0. 3945.88 Safari/537.36',
        'CLOSESPIDER_PAGECOUNT': 35
    }


    allowed_domains = ['es.besoccer.com']
    
    #jornada = 3

    start_urls = [f'https://es.besoccer.com/primera/grupo1/jornada{jornada}']

    download_delay = 0.5

    rules = (

        #Rule(
         #   LinkExtractor(
          #      allow=r'/grupo1/jornada2'
           # ), follow=True),

        Rule(
            LinkExtractor(
                allow=r'/2021'
            ), follow=True, callback='parse_items'),
    )

    def limpiarTexto(self, texto):
        nuevoTexto = texto.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ').replace(',', '').replace('%', '').replace('á', 'a').replace('é', 'e').replace('ó', 'o').strip()
        return nuevoTexto

    def parse_items(self, response):
        #sel = Selector(response)
        item =ItemLoader(Articulo(), response)


        item.add_xpath('Datos', '//tr[@class="barstyle bar4"]/td/text()', MapCompose(self.limpiarTexto))
        item.add_xpath('Tipo', '//tr[@class="barstyle bar4"]/td/h6/text()', MapCompose(self.limpiarTexto))
        item.add_xpath('Equipos', '//h3/a/b/text()', MapCompose(self.limpiarTexto))

        yield item.load_item()

        with open('BeSoccer.csv') as File:
            reader = csv.reader(File)
            list = []                # EQUIPOS DESDE: 280 - 299
            for row in reader:
                list.append(row)

              # QUITAR COMILLAS ( ENTRAR EN EL ARCHIVO CSV (EXCEL) BUSCAR 'REEMPLAZAR' EN LA BARRA, ESCRIBIR " Y ESPACIO EN BLANCO, REEMPLAZAR TODOO
        #print(list)

# ---------------------------------------- 10 veces cambiando el nº de lista cada ejecucion ---------------------
            Z = 1
            
            while Z<=10:
                
                try:
                    goles = list[Z].index('Goles')
                except:
                    goles = 0

                if goles == 0:

                    
                    posL = []
                    posV = []
                    golL = [0]
                    golV = [0]
                    t_puertaL = []
                    t_puertaV = []
                    tirosL = []
                    tirosV = []
                    t_fueraL = []
                    t_fueraV = []
                    paradasL = []
                    paradasV = []
                    equipoL = []
                    equipoV = []

                    posL.append(list[Z][0])
                    for A in range(len(posL)):  # CAMBIA LA LISTA DE PUNTOS EN STRING A INT
                        posL[A] = int(posL[A])

                    posV.append(list[Z][1])
                    for A in range(len(posV)):
                        posV[A] = int(posV[A])


                    t_puertaL.append(list[Z][2])
                    for A in range(len(t_puertaL)):
                        t_puertaL[A] = int(t_puertaL[A])

                    t_puertaV.append(list[Z][3])
                    for A in range(len(t_puertaV)):
                        t_puertaV[A] = int(t_puertaV[A])



                    tirosL.append(list[Z][6])
                    for A in range(len(tirosL)):
                        tirosL[A] = int(tirosL[A])

                    tirosV.append(list[Z][7])
                    for A in range(len(tirosV)):
                        tirosV[A] = int(tirosV[A])



                    t_fueraL.append(list[Z][4])
                    for A in range(len(t_fueraL)):
                        t_fueraL[A] = int(t_fueraL[A])

                    t_fueraV.append(list[Z][5])
                    for A in range(len(t_fueraV)):
                        t_fueraV[A] = int(t_fueraV[A])



                    paradasL.append(list[Z][8])
                    for A in range(len(paradasL)):
                        paradasL[A] = int(paradasL[A])

                    paradasV.append(list[Z][9])
                    for A in range(len(paradasV)):
                        paradasV[A] = int(paradasV[A])

                else:
                    posL = []
                    posV = []
                    golL = []
                    golV = []
                    t_puertaL = []
                    t_puertaV = []
                    tirosL = []
                    tirosV = []
                    t_fueraL = []
                    t_fueraV = []
                    paradasL = []
                    paradasV = []
                    equipoL = []
                    equipoV = []

                    posL.append(list[Z][0])
                    for A in range(len(posL)):  # CAMBIA LA LISTA DE PUNTOS EN STRING A INT
                        posL[A] = int(posL[A])

                    posV.append(list[Z][1])
                    for A in range(len(posV)):
                        posV[A] = int(posV[A])

                    golL.append(list[Z][2])
                    for A in range(len(golL)):
                        golL[A] = int(golL[A])

                    golV.append(list[Z][3])
                    for A in range(len(golV)):
                        golV[A] = int(golV[A])

                    t_puertaL.append(list[Z][4])
                    for A in range(len(t_puertaL)):
                        t_puertaL[A] = int(t_puertaL[A])

                    t_puertaV.append(list[Z][5])
                    for A in range(len(t_puertaV)):
                        t_puertaV[A] = int(t_puertaV[A])

                    tirosL.append(list[Z][8])
                    for A in range(len(tirosL)):
                        tirosL[A] = int(tirosL[A])

                    tirosV.append(list[Z][9])
                    for A in range(len(tirosV)):
                        tirosV[A] = int(tirosV[A])

                    t_fueraL.append(list[Z][6])
                    for A in range(len(t_fueraL)):
                        t_fueraL[A] = int(t_fueraL[A])

                    t_fueraV.append(list[Z][7])
                    for A in range(len(t_fueraV)):
                        t_fueraV[A] = int(t_fueraV[A])

                    paradasL.append(list[Z][10])
                    for A in range(len(paradasL)):
                        paradasL[A] = int(paradasL[A])

                    paradasV.append(list[Z][11])
                    for A in range(len(paradasV)):
                        paradasV[A] = int(paradasV[A])




                # BUSCAR CON index LA POSICIÓN DE LOS EQUIPOS EL QUE ESTÉ ANTES EN LA LISTA ES EL LOCAL
                try:
                    a = list[Z].index("Alaves")
                except:
                    a = 101
                    pass
                try:
                    b = list[Z].index("Athletic")
                except:
                    b = 101
                    pass
                try:
                    c = list[Z].index("Atletico")
                except:
                    c = 101
                    pass
                try:
                    d = list[Z].index("Barcelona")
                except:
                    d = 101
                    pass
                try:
                    e = list[Z].index("Real Betis")
                except:
                    e = 101
                    pass
                try:
                    f = list[Z].index("Cadiz")
                except:
                    f = 101
                    pass
                try:
                    g = list[Z].index("Celta")
                except:
                    g = 101
                    pass
                try:
                    h = list[Z].index("Eibar")
                except:
                    h = 101
                    pass
                try:
                    i = list[Z].index("Elche")
                except:
                    i = 101
                    pass
                try:
                    j = list[Z].index("Getafe")
                except:
                    j = 101
                    pass
                try:
                    k = list[Z].index("Granada")
                except:
                    k = 101
                    pass
                try:
                    l = list[Z].index("Huesca")
                except:
                    l = 101
                    pass
                try:
                    m = list[Z].index("Levante")
                except:
                    m = 101
                    pass
                try:
                    n = list[Z].index("Osasuna")
                except:
                    n = 101
                    pass
                try:
                    o = list[Z].index("R. Sociedad")
                except:
                    o = 101
                    pass
                try:
                    p = list[Z].index("Real Madrid")
                except:
                    p = 101
                    pass
                try:
                    q = list[Z].index("Real Valladolid")
                except:
                    q = 101
                    pass
                try:
                    r = list[Z].index("Sevilla")
                except:
                    r = 101
                    pass
                try:
                    s = list[Z].index("Valencia")
                except:
                    s = 101
                    pass
                try:
                    t = list[Z].index("Villarreal")         # 20
                except:
                    t = 101
                    pass




                # AÑADE EQUIPO LOCAL Y VISITANTE




                equipos = []
                try:
                    if a < 100:
                        equipos.append('Alaves')
                except:
                    pass
                try:
                    if b < 100:
                        equipos.append('Athletic')
                except:
                    pass
                try:
                    if c < 100:
                        equipos.append('Atletico')
                except:
                    pass
                try:
                    if d < 100:
                        equipos.append('Barcelona')
                except:
                    pass
                try:
                    if e < 100:
                        equipos.append('Real Betis')
                except:
                    pass
                try:
                    if f < 100:
                        equipos.append('Cadiz')
                except:
                    pass
                try:
                    if g < 100:
                        equipos.append('Celta')
                except:
                    pass
                try:
                    if h < 100:
                        equipos.append('Eibar')
                except:
                    pass
                try:
                    if i < 100:
                        equipos.append('Elche')
                except:
                    pass
                try:
                    if j < 100:
                        equipos.append('Getafe')
                except:
                    pass
                try:
                    if k < 100:
                        equipos.append('Granada')
                except:
                    pass
                try:
                    if l < 100:
                        equipos.append('Huesca')
                except:
                    pass
                try:
                    if m < 100:
                        equipos.append('Levante')
                except:
                    pass
                try:
                    if n < 100:
                        equipos.append('Osasuna')
                except:
                    pass
                try:
                    if o < 100:
                        equipos.append('R. Sociedad')
                except:
                    pass
                try:
                    if p < 100:
                        equipos.append('Real Madrid')
                except:
                    pass
                try:
                    if q < 100:
                        equipos.append('Real Valladolid')
                except:
                    pass
                try:
                    if r < 100:
                        equipos.append('Sevilla')
                except:
                    pass
                try:
                    if s < 100:
                        equipos.append('Valencia')
                except:
                    pass
                try:
                    if t < 100:
                        equipos.append('Villarreal')
                except:
                    pass
                
                eq1 = list[Z].index(equipos[0])
                eq2 = list[Z].index(equipos[1])


                if eq1 < eq2:
                    equipoL.append(list[Z][eq1])
                    equipoV.append(list[Z][eq2])

                else:
                    equipoV.append(list[Z][eq1])
                    equipoL.append(list[Z][eq2])

                print(jornada)
                print(equipoL, posL, golL, t_puertaL, t_fueraL, tirosL, paradasL)
                print(equipoV, posV, golV, t_puertaV, t_fueraV, tirosV, paradasV)

                equipoL = equipoL[0]
                equipoV = equipoV[0]
                posL = posL[0]
                posV = posV[0]
                golL = golL[0]
                golV = golV[0]
                t_puertaL = t_puertaL[0]
                t_puertaV = t_puertaV[0]
                t_fueraL = t_fueraL[0]
                t_fueraV = t_fueraV[0]
                tirosL = tirosL[0]
                tirosV = tirosV[0]
                paradasL = paradasL[0]
                paradasV = paradasV[0]

                Njornada = str(jornada)


                ref_partido = equipoL + Njornada + equipoV 
                
                try:            
                    miConexion = sqlite3.connect("BBDD/La_Liga_Jornadas")

                    miCursor = miConexion.cursor()
                    data = ref_partido, jornada, equipoL, equipoV, posL, posV, golL, golV, t_puertaL, t_puertaV, t_fueraL, t_fueraV, tirosL, tirosV, paradasL, paradasV
                        
                    miCursor.execute('INSERT INTO PARTIDOS (REF_PARTIDO, JORNADA, EQUIPO_L, EQUIPO_V, POSESION_L, POSESION_V, GOL_L, GOL_V, TIROS_PUERTA_L, TIROS_PUERTA_V, TIROS_FUERA_L, TIROS_FUERA_V, TIROS_L, TIROS_V, PARADAS_L, PARADAS_V) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                        data)
                        #'INSERT INTO PARTIDOS (JORNADA, EQUIPO_L, EQUIPO_V, POSESION_L, POSESION_V, GOL_L, GOL_V, TIROS_PUERTA_L, TIROS_PUERTA_V, TIROS_FUERA_L, TIROS_FUERA_V, TIROS_L, TIROS_V, PARADAS_L, PARADAS_V) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                            #data)
                    miConexion.commit()
                    
                    miConexion.close()
                except:
                    finall()
                    

                def finall():
                    pass

                equipos = []

                Z = Z + 1




        









