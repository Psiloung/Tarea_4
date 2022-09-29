from grafo import grafo
from nodo import nodo
from a_estrella import a_estrella

if __name__ == "__main__":

    #mapa_1 = grafo("archivo_grafo.txt")
    #print(mapa_1)

    origen = nodo(4.6,0.2, "Origen")
    destino = nodo(4.8, 11.7, "Destino")

    experimento = a_estrella(origen, destino, "archivo_grafo.txt")
    print(experimento.tablero)
    experimento.init()