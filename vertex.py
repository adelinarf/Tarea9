from collections import defaultdict 

class Grafo:

	def __init__(self, vertices):
		
		#Numero de vertices del grafo
		self.V = vertices 
		
		#Se guardan los lados del grafo dentro de un diccionario como 
		#lista de adyacencias
		self.graph = defaultdict(list) 

	#Agrega un lado al grafo
	def agregarLado(self, u, v):
		self.graph[u].append(v)

	def minCover(self): #O(V*E)
		
		# Lista de los elementos que han sido visitados 
		visited = [False] * (self.V)
		
		#Se itera sobre todos los vertices del grafo
		for u in range(self.V):  #O(V)
			
			# Se consideran solo los vertices que no
			#han sido visitados aun 
			if not visited[u]:
				
				#Se buscan los lados para el lado u 
				for v in self.graph[u]:  #O(E)
					if not visited[v]:
						#Se agregan los vertices sobre los 
						#que incide u en visitados para
						#que se ignoren luego y no sean 
						#incluidos en el arbol minimo
						#cobertor
						visited[v] = True
						visited[u] = True
						break
		x = []
		for j in range(self.V):
			if visited[j]:
				x.append(j)
		return x

g = Grafo(6)
g.agregarLado(0, 1)
g.agregarLado(0, 2) 
g.agregarLado(1, 2) 
g.agregarLado(1, 3) 
g.agregarLado(1, 5) 
g.agregarLado(1, 4) 

print("Los nodos para el min-cover del grafo son:",g.minCover())