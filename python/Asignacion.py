# Asignacion de strings en python
print("-----------------------------------")
print("Asignacion")
mensaje = "con"
mensaje += " "
mensaje += "Python"
print("Asignacion de strings",mensaje)

# Concatenacion de strings en python
print("-----------------------------------")
print("Concatenacion")
mensaje = "con"
mensaje2 = " "
mensaje3 = "Python"
print("Concatenacion de strings",mensaje+mensaje2+mensaje3)

#Busqueda de Strings en python
#Consiste en buscar dentro de una cadena una subcadena mas pequeña y se hace con el metodo find
print("-----------------------------------")
print("Busqueda")
cadena="obteniendo licencia para hunter hxhdevs"
buscarsubcadena=cadena.find("hxh")
print(buscarsubcadena) #recuperaremos la pocision donde se encuentra la subcadena

#Extraccion de Strings en python
#Consiste en sacar fuera de una cadena una porcion de la misma segun su pocision dentro de ella, es necesario indicar la pocision a extraer, devuelve el string dentro de la pocision establecida exceptando lo previo y siguiente
print("-----------------------------------")
print("Extraccion")
mensaje ="Extrayendo strings"
extraccion=mensaje[3:15]
print(extraccion)

#Comparacion 
#Se utiliza para comparar dos cadena de caracteres
#Como resultado devuelve un true o false
print("-----------------------------------")
print("Busqueda")
cadenaone="HXH"
cadenatwo="HXH"
print(cadenaone==cadenatwo)
print("-----------------------------------")