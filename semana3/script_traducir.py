from traductor import espaniol
from traductor import english
from traductor import frances
#ingresar la abreviaturas  ES, EN, FR para que funcione el
#programa

try:

   idioma=input("Ingresar Idioma = ES/EN/FR: ")

   if (idioma == "ES"):
       espaniol.saludar() 
   if (idioma == "EN"):
       english.saludar() 
   if (idioma == "FR"):
       frances.saludar() 
       
except:
   print("Ocurrio un error")





         

    