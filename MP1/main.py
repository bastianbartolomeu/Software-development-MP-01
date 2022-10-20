
import statistics
import pandas as pd
from collections import defaultdict


def def_value():
    return "No es una opción"

## Definición funciones ##

##PRIMERA ACCION 
def orden_segun(tipo, criterio):
    mk = subir_archivo()
    ln = []
    
    df_pokemon =  mk[0] == tipo
    filtro_pk = mk[df_pokemon]
    try:
        if criterio == 1:
            print(f"Ordenando pokemon de tipo {tipo} segun HP :")
            data = filtro_pk.sort_values(by=['HP'], ascending=True)
            #print(data)
        elif criterio == 2:
            print(f"Ordenando pokemon de tipo {tipo} segun Ataque :")
            data = filtro_pk.sort_values(by=['Attack'], ascending=True)
        elif criterio == 3:
            print(f"Ordenando pokemon de tipo {tipo} segun Defensa:")
            data = filtro_pk.sort_values(by=['Defense'], ascending=True)
            
        data1 = set(list((data.iloc[:,1])))
        for k in data1:
            print(k)
            ln.append(k)
        print('Existen ', len(ln),' pokemones de tipo ', tipo)

    except NameError:
            print("Esta parte no se puede ejecutar ya que aún no has definido todas las estructuras")
    
    
#SEGUNDA ACCION

def estadisticas( criterio,tipo):
    mk = subir_archivo()
    k = []
    df_pokemon =  mk[mk[0] == tipo]
    
    if criterio == 1:
        c = 'HP'
    elif criterio == 2:
        c = 'Attack'
    elif criterio == 3:
        c = 'Defense'

    for i in df_pokemon[c]:
        k.append(i)


    dicionario = {'Maximo':max(k),'Minimo':min(k),'Promedio':round(statistics.mean(k),1)}
    return dicionario


    #------------------------------------
#TERCERA ACCION 
    

def tipo_segun_nombre(nombre):
    mk = subir_archivo()
    df_pokemon =  mk[mk['Name'] == nombre]
    l1 = list(df_pokemon[0])
    l2 = list(df_pokemon[1])
    l3 = l1+l2
    l = tuple(l3)
    return l

## Lectura archivo y definicion estructuras ##

def subir_archivo():
    pokemon = 'pokemon.csv'
    pm = pd.read_csv(pokemon,header = 0)
    pokemon = pd.DataFrame(pm) #Bulbasaur
    pp = pokemon.rename({'Type 1;Type 2':'Tipo'},axis= 1)
    p1= pp["Tipo"].str.split('[;]', expand=True)
    del pp['Tipo']
    miko = pd.concat([pp,p1], axis=1)
    mk = pd.DataFrame(miko)
    return mk

#MENU DE ALTERNATIVAS PARA FILTRAR

def menu():
    mk = ''' Criterios de orden
        - SELECCIONE 1 PA FILTRAR DE FORMA ASCENDENTE POR HP 
        - SELECCIONE 2 PA FILTRAR DE FORMA ASCENDENTE POR ATAQUE 
        - SELECCIONE 3 PA FILTRAR DE FORMA ASCENDENTE POR DESENSA   
        '''
    return mk

## Menu flujo principal ##

acciones = defaultdict(def_value)
acciones["1"] = "orden segun"
acciones["2"] = "estadisticas"
acciones["3"] = "encontrar tipo"
acciones["4"] = "revisar"
acciones["0"] = "salir"

continuar = True
while continuar:
    
    print('''
¿Que desea hacer?

1.- Ordenar segun criterio
2.- Obtener estadísticas
3.- Saber el tipo de un pokemon
4.- Revisar Estructuras
0.- Salir
    ''')

    accion = input('Ingrese el valor : ')
    accion = acciones[accion]

    if accion == "orden segun":
        tipo = input('Ingrese el tipo de pokemon : ')
        m = menu()
        print(m)

        criterio = int(input('Ingrese Criterio : '))
        
        orden = orden_segun(tipo, criterio)
        
        #-----------------------------------------------
        #Punto 2.3 

    elif accion == "estadisticas":
        tipo = input('Ingrese el tipo de pokemon : ')
        m = menu()
        print(m)
        criterio = int(input('Ingrese el criterio : '))
        datos = estadisticas( criterio, tipo)
        #---------------------------------------------------------

        print(f"Informacion de {criterio} en pokemon de tipo {tipo}")
        print(f"  - Máximo: {datos['Maximo']}")
        print(f"  - Mínimo: {datos['Minimo']}")
        print(f"  - Promedio: {datos['Promedio']}")

    elif accion == "encontrar tipo":

        nombre = input('Ingrese el nombre : ')
        t1 = tipo_segun_nombre(nombre)
        print(f'El tipo principal de {nombre} es : ',t1[0])
        if t1[1] == '':
            print(f'{nombre} no tiene tipo secundario ')
        else:
            print(f'El tipo secundario de {nombre} es : ',t1[1])


    elif accion == "revisar":
        try:
            #---------------------------------------------
            #TIPOS DE POKEMON (PRIMERA PARTE)
            df_pokemon = subir_archivo()
            m =  list(set(df_pokemon[0]))
            print(' ')
            print('TIPOS ENCONTRADOS')
            for i in m:
                print(f' - {i}')

            print("")
            #-----------------------------------------------
   
            #SEGUNDA PARTE (FALTA)

            # p = pokemon_por_tipo["Electric"]
            # print(f"Revisando Primarios: {'25' in p[0]}")
            # print(f"Revisando Secundarios: {'170' in p[1]}")

            # print("")

            #-----------------------------------------------
            #TERCERA PARTE (listo)
            lp =[]
            print('INFORMACION DEL POKEMON : ')
            id = int(input('- ID : '))
            mos = df_pokemon[df_pokemon["#"]== id]
            lp = mos.to_numpy().tolist()
            print('- NOMBRE : ',lp[0][1])
            print('- HP : ',lp[0][2])
            print('- ATAQUE : ',lp[0][3])
            print('- DEFENSA : ',lp[0][4])
            print('- GENERACION :', lp[0][5])
            print('- TIPO PRIMARIO :', lp[0][6])
            print('- TIPO SECUNDARIO :', lp[0][7])
            #print(lp)
        
        except NameError:
            print("Esta parte no se puede ejecutar ya que aún no has definido todas las estructuras")
            

    elif accion == "salir":
        continuar = False

    else:
        print(accion)