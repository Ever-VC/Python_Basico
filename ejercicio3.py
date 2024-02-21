"""
ESCRIBIR UN PROGRAMA QUE LEA UN ENTERO POSITIVO, n, INTRODUCIDO POR EL USUAIRO Y DESPUES MUESTRE EN PANTALLA
LA SUMA DE TODOS LOS ENTEROS DESDE 1 HASTA n. LA SUMA DE LOS n PRIMEROS ENTEROS POSITIVOS PUEDE CALCULARSE DE LA
SIGUIENTE FORMA: suma = n(n+1)/2
"""

num_entero_positivo = int(input("Ingrese un numero entero positivo: "))
suma = (num_entero_positivo * (num_entero_positivo+ 1)) / 2
print("LA SUMA DE LOS n primeros enteros es: ", suma)