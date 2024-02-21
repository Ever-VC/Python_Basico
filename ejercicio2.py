"""
ESCRIBIR UN PROGRAMA QUE PREGUNTE AL USUARIO POR EL NUMERO DE HORAS TRABAJADAS Y EL COSTE POR HORA.
DESPUES DEBE MOSTRAR POR PANTALLA LA PAGA QUE CORRESPONDE.
"""

num_horas_trabajo = int(input("Ingrese la cantidad de horas trabajadas: "))
coste_hora_trabajo = float(input("Ingrese el coste por cada hora de trabajo: "))
total_pago = num_horas_trabajo * coste_hora_trabajo

print("El total de paga que le corresponde es de: ", total_pago)