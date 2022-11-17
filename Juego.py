from Prisioneros import Prisioneros
juego = Prisioneros.generar_cajas_prisioneros()
tamaño_bucle = 0
bucle = []
print(juego)
for i in range (1,101):
    eleccion = juego[i]
    while eleccion != i:
        bucle.append(eleccion)
        eleccion = juego[eleccion]
        tamaño_bucle += 1
        if tamaño_bucle > 50:
            print(f'el prisionero {i} no pudo encontrar su numero en menos de 50 intentos')
            print(bucle)
            print(f'El tamaño de este bucle es de {len(bucle)}')
            break
    else:
        tamaño_bucle = 0
        bucle = []

        
