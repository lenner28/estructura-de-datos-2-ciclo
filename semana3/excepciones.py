def llenar():
    n=3
    i=0
    while i<n:
        lista.append(input("ingrsar un numero "))
        i=i+1
def mostrar_elemento():
    try:
        pos=int(input("ingrese posicion a mostrar: "))
        print(lista[pos])
    
    except ValueError:
        print("no ingreso un valor correcto")
    except ImportError:
        print("la posicion no ingresada no existe")
    except:
        print("ocurrio un error")

lista = []
llenar()
mostrar_elemento()
