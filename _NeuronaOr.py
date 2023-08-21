# -*- coding: utf-8 -*-
"""
Created on Thurs Feb 9 22:40:13 2023

@author: Alan
"""

#Final neurona en Thonny

#ING. Tecnologías de la Información
#Sistemas Inteligentes 
#Alumno: Alan Zaid Hernandez Cruz.
#14/02/23


#Actividad: Crear una Neurona simple en Python. (OR)


#Importamos librerias random para asignar los pesos aleatorios y numpy as para el manejo de los arreglos
import numpy as np
import random



#Asigannamos el bias, en la primer columna y posteriormente asignamos los datos de la tabla OR
entradas = np.array([[1,  0,0,0],
                     [1,  0,1,1],
                     [1,  0,1,0],
                     [1,  0,1,1],
                     [1,  1,0,0],
                     [1,  1,0,1],
                     [1,  1,1,0],
                     [1,  1,1,1]])

#peso de bias
w0= random.uniform(-1,1) 

#declaracion de pesos aleatorios
w1= random.uniform(-1,1)
w2= random.uniform(-1,1)
w3= random.uniform(-1,1)
pesos= np.array([w0,w1,w2,w3])

#Declaramos bias
bias = 1


#Declaramos la variable salidas y en ella agregamos las salidas esperadas de y, mediante un arreglo 
salidas= np.array([0,1,1,1,1,1,1,1])

#Mandamos a imprimir los pesos iniciales generados aleatoriamente
print('Pesos Iniciales: ')
print('w0: ', w0)
print('w1: ', w1)
print('w2: ', w2)
print('w3: ', w3)
print('\n')


#Declaramos la variable de iteraciones, la cual se encargara de llevar el control de todas las iteraciones realizadas 
iteraciones_re= 1

#Declaramos la variable fila y la inicializamos en 0, la cual determinara el numero de las filas de la matriz de entradas
fila= 0

#Imprimimos las iteraciones realizadas
print('Iteraciones: \n', iteraciones_re)


#Ocupamos un ciclo while para para que la neurona aprenda, mediante la iteracion actualizamos
while(fila<8):
    #Calculamos los resultados en base a y, se realiza la suma ponderada 
    y= sum(entradas[fila]*pesos)
    
    #Imprimimos la suma ponderada
    print('Entradas: ',entradas[fila])
    print('Los Pesos son: ', pesos)
    print('El total de la suma ponderada es: ', y, '\n')
    
    
#Aplicamos usos de condicional if para la funcion de activacion
    #comparamos si y es mayor que, entra a la condicion y y es igual a 1
    if(y>0):
        y = 1
        
        #Caso contrario, if else, si y es menor que 0, entra a la condicion y y es igual a 0
    elif(y<0):
        y = 0
        
       #Ocupamos if, si y es igual a la salida entonces, salta a la siguiente fila y aumenta 
    if(y==salidas[fila]):
        fila = fila + 1
        
        #caso contrario, else, se vuelven a calcular los pesos y la variable fila vuelve a 0
    else:
        
        #Asignamos peso de bias, aleatorio
        w0 = random.uniform(-1,1)
        
        #Volvemos a asignar pesos aleatorios 
        w1 = random.uniform(-1,1)
        w2 = random.uniform(-1,1)
        w3 = random.uniform(-1,1)
        pesos = np.array([w0,w1,w2,w3])
        
        
        #Imprimimos la actualizacion de pesos
        print('Actualizacion de Pesos: ')
        print('w0, w1, w2, w3', [w0], [w1], [w2], [w3])
        
        #Inicializamos la fila en 0
        fila=0
        
        #A iteraciones le sumamos 1, para ir contando e imprimimos
        iteraciones_re = iteraciones_re + 1
        print('Iteraciones: ', iteraciones_re)

#Imprimimos los pesos finales
print('Pesos finales: ')
print('w0, w1, w2, w3', [w0], [w1], [w2], [w3])
print('\n')


##Declaramos y asignamos variables de tipo entero, para poder ingresar los valores y comprobar resultados 
print('Comprobacion de la neurona, mediante datos ingresados: ')
x1= int(input('Ingresa el valor de x1: '))
x2= int(input('Ingresa el valor de x2: '))
x3= int(input('Ingresa el valor de x3: '))

#Se calcula la suma ponderada para comprobar los pesos
y= (pesos[0]*bias) + ((pesos[1]*x1) + (pesos[2]*x2) + (pesos[3]*x3))
print('El total de la suma ponderada es*: ', y)
#Ocupamos condicionales para comparar 
if(y>0):
    y = 1
elif(y<0):
    y = 0
#Imprimimos el total de la salida
print('Salida: ', y)

