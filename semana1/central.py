#clases extras -----modulos
import repaso1
import repaso4
#import repaso3

num1=int(input("ingrese num1: "))
num2=int(input("ingrese num2: "))
#calcular(num1,num2)
print(repaso1.calcular(num1,num2))
#--------------------------------------------
for i in range(5):
    est=input("ingresa al nuevo estudiante: ")
    repaso4.agregar_estudiante(est)


input()