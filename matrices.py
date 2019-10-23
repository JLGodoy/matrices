import numpy
import threading as hilos

#MatSize= input("Introduzca el tamaño de la matriz:") # solicita el tamaño de la matriz
MatSize = 4
#Creación de dos matrices de tamaño MatZise x MatZise, utilizando como numeros tope el 0 y el 30
A= numpy.random.randint(0,30,(int(MatSize),int(MatSize)))
B = numpy.random.randint(0,30,(int(MatSize),int(MatSize)))


C= A.dot(B)
print("A = ")
print(A)
print()
print("B = "  )
print(B)
print()
print("C = ")
print(C)
print()

#Programa utilizando hilos
def multiplicar(matriz,size):
    c = numpy.zeros((int(size),int(size)))
    for i in range(0,MatSize):
        for a in range (0,MatSize):
            for k in range(0,MatSize):
                c[i][a] += A[i][k] * B[k][a]
    print("El hilo",hilos.current_thread().getName(),
    "Con identificador", hilos.current_thread().ident, "tiene como valor:")
    print(c)
    print()

hilo1 = hilos.Thread(target = multiplicar(A,MatSize))
hilo2 = hilos.Thread(target = multiplicar(A,MatSize))
hilo1.start()
hilo2.start()



#multiplicar(A, MatSize)
