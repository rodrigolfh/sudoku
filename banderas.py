azul = [0,38,84]
blanco = [255,255,255]
rojo= [237, 41, 57]
verde = [0, 140, 69]

#cada macropixel de 9x6 (proporción 3:2)

def macropixel(color):
    filas = 6
    columnas = 9
    macropx = []
    
    for i in range(filas):
        for j in range(columnas):
            macropx.append(color)
    macropx_final = []
    macropx_final.append(macropx[0:3])
    macropx_final.append(macropx[3:])
    return macropx_final



#países
francia = {"orientación" : "vertical", "colores": (azul, blanco, rojo)}
italia = {"orientación": "vertical", "colores": (verde, blanco, rojo)}
rusia = {"orientación": "horizontal", "colores": (blanco, azul, rojo)}


def bandera(país):
    franja_bandera = []
    
    if país["orientación"] == "vertical":
        for fila in range(3):
           
            for color in país["colores"]:
                franja_bandera.append(macropixel(color))
        

    if país["orientación"] == "horizontal":
        for color in país["colores"]:
           
            
            for fila in range(3):
                franja_bandera.append(macropixel(color))
    return franja_bandera

bandera(francia)
