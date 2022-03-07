#soy un comentario de linea 
 
'''
    esto es un comentario de
    bloque
'''
 
#salida por consola(impresion en patalla)
from turtle import left
 
print('Hola mundo saludando desde PYTHON')
 
#variables con python
#Datos PRIMITIVOS
nombreUsuario="Naime Juliet"
edadUsuario=31
estaturaUsuario=1.62
hinchaDelMejor=False
nombreUsuario="Julieta"
 
#Salida de mensajes + variables por consola(concatenar)
#print("Buenas tardes",nombreUsuario)
 
#impresion por referencia o fprint de python
#print(f'Buenas tardes {nombreUsuario}')
 
#print("buenas tardes",nombreUsuario,"su edad es",edadUsuario)
 
#print(f'Buenas tardes {nombreUsuario} su edad es: {edadUsuario} su estatura es: {estaturaUsuario}')
 
#Recibiendo entradas por teclado (consola)
#variables reciben datos (no quedan quemadas)
#numero1=input("Digita un numero entero: ")
#numero2=input("Digita un segundo numero entero: ")
#print(f' El primer numero fue: {numero1} y el segundo numero es: {numero2}')
 
#suma=numero1+numero2
#print(f'{numero1}+{numero2}={suma}')
 
#castear o convertir el tipo de dato de una variable 
#numero1=int(input("Digite un numero: "))
#numero2=int(input("Digite otro numero"))
#suma=numero1+numero2
#print(f'{numero1}+{numero2}={suma}')
 
#Condiciones logicas
# IF (sirve para comparar)
 
numero=int(input("Digite un numero entero: "))
if (numero>=0):
    print("Soy un numero positivo")
else:
    print("Soy un numero negativo")
    print("OE fuck  you me Gono.....")
