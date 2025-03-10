# Vuelos con Búsqueda en Amplitud (BFS) 
from arbol import Nodo

def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while nodos_frontera:
        nodo = nodos_frontera.pop(0)  # Sacar el primer nodo (FIFO)
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo 
        
        # Expandir los nodos hijos
        dato_nodo = nodo.get_datos()
        if dato_nodo in conexiones:  
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    hijo.padre = nodo 
                    nodos_frontera.append(hijo)

    return None 

if __name__ == "__main__":
    conexiones = {
        'CDMX': ['SLP', 'MEXICALI', 'CHIHUAHUA'],
        'SAPOPAN': ['ZACATECAS', 'MEXICALI'],
        'GUADALAJARA': ['CHIAPAS'],
        'CHIAPAS': ['CHIHUAHUA'],
        'MEXICALI': ['SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'],
        'SLP': ['CDMX', 'MEXICALI'],
        'ZACATECAS': ['SAPOPAN', 'SONORA', 'CHIHUAHUA'],
        'SONORA': ['ZACATECAS', 'MEXICALI'],
        'MICHOACAN': ['CHIHUAHUA'],
        'CHIHUAHUA': ['MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX', 'CHIAPAS'],
    }

    estado_inicial = 'CDMX'
    solucion = 'ZACATECAS'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse() 
        print(" -> ".join(resultado[:3]))  
    else:
        print("No se encontró un camino a la solución.")
