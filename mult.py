# A B nxn n>0
#B = A^-1
#Error e
#Tiempo O(n^2 log 1/e)

import random 
import numpy as np


# Algoritmo de Freivald
def freivald(A,B,C) :
	N = len(A)
	
	# Genera el vector random
	X = [0] * N
	random.seed(100)
	for i in range(0, N) :
		X[i] = (int)(random.randrange(100000000) % 2)

	B_X = [0] * N
	#Multiplicacion de B*X
	for i in range(0, N) :
		for j in range(0, N) :
			B_X[i] = B_X[i] + B[i][j] * X[j]

	#Multiplicacion de C*X
	C_X = [0] * N
	for i in range(0, N) :
		for j in range(0, N) :
			C_X[i] = C_X[i] + C[i][j] * X[j]

	#Multiplicacion de A*B*X
	A_B_X = [0] * N
	for i in range(0, N) :
		for j in range(0, N) :
			A_B_X[i] = A_B_X[i] + A[i][j] * B_X[j]

	# Verificar si A*B*X - C*X = 0
	# Se verifica si A*B*X = C*X
	# A * (B*r) - (C*r) is 0 or not
	for i in range(0, N) :
		if (A_B_X[i] - C_X[i] != 0) :
			return False
			
	return True

# k iteraciones
def producto(A,B,C, k) :
	for i in range(k) :
		if (freivald(A,B,C) == False) :
			return False
	return True

k = 300

def inversa(A,B,k):
	C = np.identity(len(A))
	RES = producto(A,B,C,k)
	if RES:
		print("La matriz\n",np.array(B),"\n es la inversa de \n",np.array(A))
	else:
		print("La matriz\n",np.array(B),"\n NO es la inversa de \n",np.array(A))
	return RES

def correcto(r,correcto):
	if r==correcto:
		print("RESULTADO CORRECTO")
	else:
		print("RESULTADO INCORRECTO")

def tests():
	A = np.array([ [ 1, 1 ], [ 1, 0 ] ])
	B = np.array([ [ 1, 1 ], [ 1, 1 ] ])
	r=inversa(A,B,k)
	correcto(r,False) 

	n = np.linalg.inv(A)
	r=inversa(A,n,k)
	correcto(r,True)

	m = np.array([[3,4,-1],[2,0,1],[1,3,-2]])
	n = np.linalg.inv(m)
	r=inversa(m,n,k)
	correcto(r,True)

	l = np.array([[1,2,3],[-2,3,-4],[3,4,5]])
	s = np.linalg.inv(l)
	r=inversa(l,s,k)
	correcto(r,True)

tests()