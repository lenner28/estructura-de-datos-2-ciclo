
def encriptar(val):
    numero = ["1","2","3","4","5"]
    if val in numero:
        return val
    return None

#val = input("Ingresa un valor: ")
#print("El valor ingresado es: ",val)
############################################################
#if encriptar(val)!=None:
#    print("El valor encriptado  es: ",len(encriptar(val)))
#else:
#    print("No se logro encriptar")
###############################################################
lista = [1,2,3]
if len(lista) > 0:
    print("Funcion pop de la lista", lista.pop())

########Excepcio 1#############################
"""try:
    num = input("Ingresar numero: ")
    print("{}/{}={}".format(num,10,num/10))
    lista=[1,2,3,4,]
    print("elemento 5: ", lista[1])
    #print(str(num +"/10"+ "="+ num/10))
except IndexError:
    print("Indice no encontrado")
except ValueError:
    print("Error al ingresar el numero")
except ZeroDivisionError:
    print("No se puede dividir entre 0 ")
except:
    print("ocurrio un  error inesperado")
else:
    print("Se fenalizo con exito")
"""
##################### excepciones 2##############
while True:
    try:
        numero=float(input("ingresar numero: "))
    except:
        print("valor ingresado es correcto")
    else:
        print("no se presento la excepcion")
        break
    finally:
        print("fin del programa")
