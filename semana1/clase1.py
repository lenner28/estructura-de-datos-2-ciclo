#si  tienes que ingresar 3 numeros, y de ellos  deve imprimir cual es el mayo
#p.e.5..6.3 me deve imprimir 6
#primera forma estructuras repetitivas
#lista = []
#def max(lista):
#    max = 0
#    for b in lista:
#        if b > max:
#            max=b
#    return max
#print("ingresar 3 numeros: ")
#for  c in range(3):
#    numero = int(input("ingresar numero: "))
#    lista.append(numero)
#print("el numero mayor es : ",max(lista))
#segunda forma  mas eficiente
def buscar_mayor(a,b,c):
    mayor = None
    if a>b:
        if a>c:
            mayor = a
        else:
            mayor =c
    else:
        if b>c:
            mayor =b
        else:
            mayor=c
    return mayor
def leer_numero():
    number = int(input("Ingrese numero: "))
    return number
a = leer_numero()
b = leer_numero()
c = leer_numero()
print("El mayor es: ",buscar_mayor(a, b, c))
