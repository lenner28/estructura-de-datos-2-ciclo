from matematica import geaometria
from matematica import calculadora

try:
    lado= int(input("ingresar el  lado del cuadro: "))
    print("el perimetro del cuadrado de lado {} es {}".format(lado,geaometria.perimetro_cuadrado(lado)))

    num1=int(input("ingresar un valor: "))
    num2=int(input("ingresar otro valor: "))
    print("la division de los numeros ingrsados es ", calculadora.division(num1,num2))
except TypeError:
    print("se ingreso un valor incorrecto")

except ZeroDivisionError:
    print("no es posible realizar  una division por cero")
    #num2=1
    #print("la division de los numeros ingrsados es ", calculadora.division(num1,num2))

except:
    print("ocurrio un error")


