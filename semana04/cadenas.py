#######concatenar cadenas
"""cad1 = "bienevenido"
cad2 = "a piura"
val = 10
print(cad1+cad2)
print(cad1+cad2+str(val))
print("{} {} {}".format(cad1,cad2, val))"""

########replicado#####
"""cad = "hola "
cad2= 10
print(10*cad)"""

###########chr() ord()###
"""print(ord("a"))          
print(ord("A") )         
print(chr("99")  )   """  

#################cadenas como listas#$#######
"""cadena = "estructura de datos"
for i in range(len(cadena)):
    print(cadena[i],end="")"""
#############rebanadas
"""cadena = "computador"
#0: c 1:o
#parametros por defecto son[:::]
#star(inclusivo,defecto en 0), end(exclusico),step(por defecto 1)
print(cadena[4:6]) #ut
print(cadena[5:])#tadora
print(cadena[:5])#compu
print(cadena[4:-2])#utado
print(cadena[-5:7])#utado
print(cadena[1:7:2])#opt
print(cadena[::2])#cmuao"""

#######in
"""cad = "hola mundo"
find = "ola"
print(cad in find)"""

####min() and  max ()
"""numeros= [6,3,5]
cadena="holamundo"
print(min("numeros"))
print(min("cadena"))
print(max("numeros"))
print(max("cadenas"))"""
#########find()
"""cadena= "bienevenido a piura"
find = "piura"
print(cadena.find(find))"""
##################### upper() lower()
"""cadena= " hola mundo"
print(cadena.upper())
print(cadena.lower())"""

#############comparaciom  de cadenas
cad1 = "hola"
cad2="Hola"
print(cad1==cad2)
print(cad1!=cad2)
print("10"<"@10")
