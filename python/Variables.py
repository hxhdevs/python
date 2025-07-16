print("Esto es una suma")
operacion = "suma"
numero_uno =2
numero_dos =7
resultado = numero_dos+numero_uno

# 1. Usando f-string (moderno y limpio)
print(f"El resultado de la suma de {numero_uno} + {numero_dos} es: {resultado}")
print(f"La accion ejecutada fue una {operacion}")
# 2. Usando str.format()
print("El resultado de la suma de {} + {} es: {}".format(numero_uno, numero_dos, resultado))
print("La accion ejecutada fue una {}".format(operacion))
# 3. Concatenando strings con +
print("El resultado de la suma de " + str(numero_uno) + " + " + str(numero_dos) + " es: " + str(resultado))
print("La accion ejecutada fue una "+str(operacion))
#4. Usando múltiples argumentos en print()
print("El resultado de la suma de", numero_uno, "+", numero_dos, "es:", resultado)
print("La accion ejecutada fue una ",operacion)
#5. Usando % (formato estilo C, más antiguo)
print("El resultado de la suma de %d + %d es: %d" % (numero_uno, numero_dos, resultado))
print("La accion ejecutada fue una %s" %(operacion))