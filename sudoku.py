import random




def crear_caja(cantidad): 
    """
    Devuelve las casillas a llenar en UNA CAJA, tomando por argumento cuántas pistas debe tener

    """
    #Elegir cuáles casillas serán llenadas
    casillas = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
    random.shuffle(casillas) #las revuelve
    casillas = casillas[:cantidad] # deja sólo las que se van a llenar
    
    números= [1,2,3,4,5,6,7,8,9] #lista de las opciones de números
    random.shuffle(números) #revolver los números 
    números_a_utilizar= números[:cantidad] #seleccionar sólo la cantidad deseada

    caja = {"A1":{}, "B1":{}, "C1":{}, #caja vacía
          "A2":{}, "B2":{}, "C2":{},
           "A3":{}, "B3":{}, "C3":{} }


    for casilla in casillas: #casillas_a_llenar es un dict con las coordenadas de las casillas a llenar
        caja[casilla] = números_a_utilizar[-1] #elige el último número y lo asigna a una casilla
        números_a_utilizar.pop() #borra el último número, para que la siguiente iteración ocupe el "nuevo" último número
    
    return caja
    
def pistas_por_caja():
    """
    Crea una lista de 9 cantidades de pistas, entre 1 y 5,
    donde la suma total es mayor o igual a 17 y menor o igual a 30
    """
   
    #Un sudoku debe tener solo UNA solución, y para lograr esto se necesitan al menos 17 pistas,
    #y como máximo puede tener 30.

    mínimo_de_pistas = 17 
    máximo_de_pistas = 30 
    
    #Entonces, genero una lista para saber con cuántos números se llenarán las 9 cajas
    lista_pistas_por_caja = [] #lista vacía

    while True:
        for caja in range(9): #9 son las cajas        
            lista_pistas_por_caja.append(random.randint(1,5)) #llena la lista con las cantidades, nunca he visto uno con más de 5
  
        if sum(lista_pistas_por_caja) < mínimo_de_pistas or sum(lista_pistas_por_caja) > máximo_de_pistas:
            lista_pistas_por_caja = [] #si la cantidad de pistas suman menos de 17 o más de 30, se comienza de nuevo

        else:
            break #sino, se sale del loop porque se encontró una lista que cumple con las condiciones

    return lista_pistas_por_caja

def mostrar_sudoku(sudoku):
    
    print("---+---+---")

    for item in sudoku:
        if item[2] == {}:
            print(" ", end='')
        
        else:
            print(item[2], end='')
        
        if (sudoku.index(item)+1) % 9 == 0 :
            print('')

        if ((sudoku.index(item) + 1)% 27 == 0):
            print("---+---+---")

        elif ((sudoku.index(item) + 1) % 3 == 0) and ((sudoku.index(item) + 1) % 9 != 0) and ((sudoku.index(item) + 1)% 27 != 0):
            #print(item[2], end='')
            print("|", end='')

    print('')


def intento_sudoku():
    """
    Intento de Sudoku, al que sólo le falta validar la no repetición de números en cada fila o columna de cajas
    """
    sudoku = {"A1":{}, "B1":{}, "C1":{},
          "A2":{}, "B2":{}, "C2":{},
           "A3":{}, "B3":{}, "C3":{} }
    lista_pistas = pistas_por_caja()
    for caja in sudoku:
        sudoku[caja] = crear_caja(lista_pistas[-1])
        lista_pistas.pop()
    
    


    while True:
        nros_columnas = []
        nros_filas = []
        intento = sudoku
        #print(intento)
        #revisar columnas
        # tuplas porque no se modifican
        filas = ("A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3")
        

        columnaA = ("A1", "A2", "A3")
        columnaB = ("B1", "B2", "B3")
        columnaC = ("C1", "C2", "C3")
        columnas = (columnaA, columnaB, columnaC)
        lista_análisis = []
        for key, value in intento.items():
            #print("-")
            for key2, value2 in value.items():
                #print(key, key2, value2)
                lista_análisis.append((key, key2, value2))

        #print(lista_análisis)
        #print("-")

        lista_análisis.sort()
        #print(lista_análisis)

        #ahora convertir el dict en una lista de tuplas en formato (caja, casilla, valor)
        lista_agrupada = []
        for i in range(1,4):
            for j in range(1,4):
                for item in lista_análisis:
                    if (str(i) in item[0]) and (str(j) in item[1]):
                        #print(item)
                        lista_agrupada.append(item)


        return lista_agrupada




def hay_repetidos_fila(lista):


    lista_análisis_filas = []
    lista_análisis_columnas = []
    slice_lista_desde = 0
    slice_lista_hasta = 9
    
    for i in range(9):
        sublista = []       
        for casilla in lista[slice_lista_desde:slice_lista_hasta]:
            #lista_análisis_filas.append(casilla[2])
            sublista.append(casilla[2])
            #print("fila---------:", lista_análisis_filas)
        #print("filas : ", lista_análisis_filas)
        while {} in sublista:
            sublista.remove({})
            #lista_análisis_filas.remove({})
        #print("filas : ", lista_análisis_filas) ######################aca debe estarel error
        #lista_análisis_filas.sort()
        sublista.sort()
        #print("lista anilisis ordenada", lista_análisis_filas)
        item_anterior = 0
        for item in sublista:
            
            if item_anterior == item:
                print("-False-")
                
                return False
                
                
            else:
                item_anterior = item

        lista_análisis_filas.append(sublista)
        slice_lista_desde += 9
        slice_lista_hasta += 9

    return True   
    
        

def probar_sudoku():
    
    
    recuento_intentos = 0
    while True:
        lista = intento_sudoku()
        recuento_intentos = recuento_intentos + 1
        if hay_repetidos_fila(lista) == True:
            break

    mostrar_sudoku(lista)
    print("intentos: ", recuento_intentos)

    
    return lista


        
         
        
         

        







"""
        for fila in range(1,4):
            print("fila:", fila)
            for caja in intento.values():
                print("caja en intento.values:", caja)
                for casilla in caja.values():
                    print("casilla in caja.values:", casilla)
                    if fila in caja.values():
                        print(caja.keys())
                        print(caja.values())
                
"""

        
            
               


        
        #revisar filas
        




    

 





    
    



    
    




