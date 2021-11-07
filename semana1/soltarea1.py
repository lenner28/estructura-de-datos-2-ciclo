#tarea: usar una lista que permite ingresar numero enteros.
#(minimo permitir ingresar 10 numeros)
#luego crear una funcion que los ordene de manera  ascendente,
#por ultimo imprimir la lista ordenada.

Lista = []
swapped = True
Numero = int(input("Ingresar 10 Elementos: "))

for i in range (Numero):
    Valor = int(input("Introducir Elementos de la Lista:# "))
    Lista.append(Valor)

while swapped:
   swapped = False
   for i in range(len(Lista)-1):
        if Lista[i] > Lista[i + 1]:
         swapped = True
         Lista[i],Lista[i + 1]= Lista[i  + 1],Lista[i]
print("\nLISTA ORDENADA: ")
print("-----------------")
print(Lista)
