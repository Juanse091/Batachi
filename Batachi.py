import math

def coords_cercanas(lista_de_coordenadas, coordenada_ingresada):
    print('!!ingreso!!')

    # Inicializar variables para el seguimiento de las dos coordenadas más cercanas
    coordenadas_cercanas = [None, None]
    distancias_minimas = [float('inf'), float('inf')]

    # Calcular la distancia entre la coordenada ingresada y cada coordenada en la lista
    for coordenada in lista_de_coordenadas:
        x, y = coordenada
        distancia = math.sqrt((x - coordenada_ingresada[0]) ** 2 + (y - coordenada_ingresada[1]) ** 2)
        # Comprobar si esta distancia es más pequeña que alguna de las dos distancias mínimas actuales
        if distancia < distancias_minimas[0]:
            distancias_minimas[1] = distancias_minimas[0]
            coordenadas_cercanas[1] = coordenadas_cercanas[0]
            distancias_minimas[0] = distancia
            coordenadas_cercanas[0] = coordenada
        elif distancia < distancias_minimas[1]:
            distancias_minimas[1] = distancia
            coordenadas_cercanas[1] = coordenada

    # Ahora tienes las dos coordenadas más cercanas en la lista "coordenadas_cercanas" y sus distancias mínimas en la lista "distancias_minimas"
    print("Dos coordenadas más cercanas:", coordenadas_cercanas)
    print("Distancias mínimas:", distancias_minimas)
    return coordenadas_cercanas

def no_repeat(coordenada, lista_de_coordenadas):
    print('Coordenada ' + str(coordenada))
    print("lista: " + ', '.join(map(str, lista_de_coordenadas)))
    if coordenada in lista_de_coordenadas:
        x, y = coordenada
        x = (x + 1) % 11
        if x == 0:
            x += 1
        y = (y + 1) % 11
        if y == 0:
            y += 1        
        nueva_coordenada = (x, y)
        return no_repeat(nueva_coordenada, lista_de_coordenadas)
    else:
        return coordenada


#? Traduce de numero a letra (Basicamente para imprimir de manera legible)
def translate(abc, value):
    letter = None
    for key, val in abc.items():
        if value == val:
            letter = key
    return letter

#? DICCIONARIO
abc = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6,'g': 7,'h': 8,'i': 9,'j': 10,}



lista_coordenadas = []
bandera = False

while(bandera == False): 
        entrada = input("Ingrese la posición (letra y número): ")
        y, x = entrada.split()
        print(f'({x},{y})')
        x = int(x)  # Convierte x en un entero
        y = abc.get(y, None)  # Obtiene el valor correspondiente a y del diccionario, o None si no se encuentra

        print(f'({x},{y})')
        coordenadas = (x,y)
        
        if(len(lista_coordenadas) > 1): #? Si la lista no esta vacia y hay mas de un dato se hara la interpolación
            coordenadas_cercanas = coords_cercanas(lista_coordenadas, coordenadas)
            x0 = coordenadas_cercanas[0][0]
            y0 = coordenadas_cercanas[0][1]
            x1 = coordenadas_cercanas[1][0]
            y1 = coordenadas_cercanas[1][1]

            if(x0 != x1 and y0 != y1):
                y_x = y = y0 + (x - x0) * (y1 - y0) / (x1 - x0)
                y_x = y_x % 11
                if y_x == 0:
                    y_x =+ 1
                y_x = int(math.ceil(y_x))


                x_interpolated = x + (y - y0) * (x1 - x0) / (y1 - y0)
                x_interpolated = x_interpolated % 11
                if x_interpolated == 0:
                    x_interpolated += 1
                x_interpolated = int(math.ceil(x_interpolated))



                nueva_coordenada = (x_interpolated,y_x)
                print(f"{nueva_coordenada}  Lista: {lista_coordenadas}")
                nueva_coordenada = no_repeat(nueva_coordenada, lista_coordenadas)

                lista_coordenadas.append(nueva_coordenada)

                print(f'\nEstimación de disparo: ({translate(abc, nueva_coordenada[1])},{nueva_coordenada[0]})')
            else:
                lista_coordenadas.append(coordenadas)

                print('\nHa disparado en la posición: (' + str(translate(abc, coordenadas[1])) + "," + str(coordenadas[0]) + ")")
                    
        else:   
            lista_coordenadas.append(coordenadas)
            print('\nHa disparado en la posición: (' + str(translate(abc, coordenadas[1])) + "," + str(coordenadas[0]) + ")")

        print(lista_coordenadas)
        request = input('Terminar?').lower()
        if(request == 'si'):
            bandera = True
        else:
            bandera = False