#-------vectores--clase particular
#listas
#nombre=[]
#numero=None
nombres=["julio","juan","pedro"]
nombres.append("paola")#agregar al final
print(nombres)#mostrar los elementos de la lista
nombres[1]="sonia"#cambiar um valor de un elemento
print(nombres)
print(len(nombres))#cantidad de la lista

#comprobar si un elemento esta en la lista if..(for es para todos los elementos)
if "julio" in nombres:
    print("julio esta registrado")
#comprobar todo los elememtos
for i in nombres:
    print("se reguistro a: ", i)
#cambiar varios elementos
print("--------------------")
nombres[1:3]=["rocio","luis"]
print(nombres)
#agrgar elementos en otra posicion
nombres.insert(2,"rosa")
#ordenar los elementos
nombres.sort()#ordenar de formam desendente(reverse=true)
print(nombres)
#eliminar
del nombres[3]#por indice
nombres.pop(2)#por indice
nombres.remove("julio")#por nombre
print(nombres)
#quitar todo los elementos
nombres.clear()
print(nombres)
input()