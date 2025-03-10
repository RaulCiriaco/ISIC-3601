# Puzle Lineal con búsqueda en amplitud.
from arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()  # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:  # Solución encontrada
            solucionado = True  # Detenemos la búsqueda al encontrar la primera solución óptima
            return nodo

        dato_nodo = nodo.get_datos()  # Obtener estado actual del nodo

        # Definir los posibles intercambios para generar hijos
        movimientos = [(0, 1), (1, 2), (2, 3)]

        for i, j in movimientos:
            hijo = dato_nodo[:]
            hijo[i], hijo[j] = hijo[j], hijo[i]
            nuevo_nodo = Nodo(hijo)
            nuevo_nodo.padre = nodo  # Asignar su padre

            if not nuevo_nodo.en_lista(nodos_visitados) and not nuevo_nodo.en_lista(nodos_frontera):
                nodos_frontera.append(nuevo_nodo)

    return None  # Si no se encuentra solución

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)

    # Mostrar resultado
    resultado = []
    nodo = nodo_solucion

    while nodo and nodo.get_padre() is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)  # Se imprime solo una solución con 5 pasos
