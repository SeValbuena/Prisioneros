import random
class Prisioneros():
    numeros_cajas = [i for i in range (1,101)]

    def generar_cajas_prisioneros():
        numeros_aleatorios = []
        while len(numeros_aleatorios) < 100:
            numero = random.choice(Prisioneros.numeros_cajas)
            numeros_aleatorios.append(numero)
            Prisioneros.numeros_cajas.remove(numero)
        asignacion = {i:j for i,j in enumerate(numeros_aleatorios, start=1)}
        return asignacion
    
