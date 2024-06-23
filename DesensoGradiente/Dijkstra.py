import matplotlib.pyplot as plt
import networkx as nx 

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.aristas = {}
    
    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)
        if vertice not in self.aristas:
            self.aristas[vertice] = {}
    
    def agregar_arista(self, inicio, fin, peso):
        self.aristas[inicio][fin] = peso
        self.aristas[fin][inicio] = peso
    
    def dijkstra(self, origen):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[origen] = 0
        visitados = set()
        iteraciones = 0
        
        while visitados != self.vertices:
            nodo_actual = None
            for vertice in self.vertices:
                if vertice not in visitados and (nodo_actual is None or distancias[vertice] < distancias[nodo_actual]):
                    nodo_actual = vertice
            
            visitados.add(nodo_actual)
            
            for vecino, peso in self.aristas[nodo_actual].items():
                if distancias[nodo_actual] + peso < distancias[vecino]:
                    distancias[vecino] = distancias[nodo_actual] + peso
            
            iteraciones += 1
        
        return distancias, iteraciones

    def mejor_ruta(self, origen, destino):
        distancias, _ = self.dijkstra(origen)
        ruta = [destino]
        actual = destino
        
        while actual != origen:
            for vecino, peso in self.aristas[actual].items():
                if distancias[actual] == distancias[vecino] + peso:
                    ruta.append(vecino)
                    actual = vecino
                    break
        
        return ruta[::-1] 

grafo = Grafo()
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
grafo.agregar_vertice('F')
grafo.agregar_vertice('G')
grafo.agregar_vertice('H')
grafo.agregar_vertice('I')

grafo.agregar_arista('E', 'A', 3)
grafo.agregar_arista('A', 'F', 4)
grafo.agregar_arista('A', 'C', 8)
grafo.agregar_arista('F', 'C', 1)
grafo.agregar_arista('C', 'B', 6)
grafo.agregar_arista('C', 'G', 5)
grafo.agregar_arista('G', 'I', 3)
grafo.agregar_arista('I', 'D', 2)
grafo.agregar_arista('I', 'H', 3)
grafo.agregar_arista('B', 'D', 2)
grafo.agregar_arista('B', 'H', 7)

inicio = 'E'
destino = 'H'

mejor_ruta = grafo.mejor_ruta(inicio, destino)

distancias, num_iteraciones = grafo.dijkstra(inicio)
distancia_total = distancias[destino]

print(f"Mejor ruta desde {inicio} a {destino}: {' -> '.join(mejor_ruta)}")
print(f"Distancia total de la ruta: {distancia_total}")
print(f"Número de iteraciones: {num_iteraciones}")

G = nx.DiGraph()

for nodo in grafo.vertices:
    G.add_node(nodo)

for inicio, conexiones in grafo.aristas.items():
    for fin, peso in conexiones.items():
        G.add_edge(inicio, fin, weight=peso)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')

edges = G.edges()
edge_colors = ['r' if edge in zip(mejor_ruta, mejor_ruta[1:]) else 'k' for edge in edges]

nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, width=2, arrowsize=20)

edge_labels = {(inicio, fin): peso for inicio, conexiones in grafo.aristas.items() for fin, peso in conexiones.items()}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()