from arbol import Nodo

def buscar_solucion_BFS(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial  # nodo_solucion

    # Expandir los nodos sucesores (hijos)
    dato_nodo = nodo_inicial.get_datos()
    hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
    hijo_izquierdo = Nodo(hijo)
    hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
    hijo_central = Nodo(hijo)
    hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
    hijo_derecho = Nodo(hijo)

    nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])  # Corregido: lista de hijos

    for nodo_hijo in nodo_inicial.get_hijos():
        if nodo_hijo.get_datos() not in visitados:
            # Llamada Recursiva
            sol = buscar_solucion_BFS(nodo_hijo, solucion, visitados)
            if sol is not None:
                return sol
    return None

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    resultado = [] 
    nodo_inicial = Nodo(estado_inicial)

    nodo = buscar_solucion_BFS(nodo_inicial, solucion, visitados)

    # Mostrar resultado
    if nodo is not None:  
        while nodo is not None:  
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse()
        print(resultado)
    else:
        print("No se encontró una solución.")
C o m m i t   1 6  
 C o m m i t   1 7  
 C o m m i t   1 8  
 C o m m i t   1 9  
 C o m m i t   2 0  
 C o m m i t   2 1  
 C o m m i t   2 2  
 C o m m i t   1 6  
 C o m m i t   1 7  
 C o m m i t   1 8  
 C o m m i t   1 9  
 C o m m i t   2 0  
 C o m m i t   2 1  
 C o m m i t   2 2  
 C o m m i t   1 6  
 C o m m i t   1 7  
 C o m m i t   1 8  
 C o m m i t   1 9  
 C o m m i t   2 0  
 C o m m i t   2 1  
 C o m m i t   2 2  
 C o m m i t   1 6  
 C o m m i t   1 7  
 C o m m i t   1 8  
 C o m m i t   1 9  
 C o m m i t   2 0  
 C o m m i t   2 1  
 C o m m i t   2 2  
 C o m m i t   2 3  
 C o m m i t   2 4  
 C o m m i t   2 5  
 C o m m i t   2 6  
 C o m m i t   2 7  
 C o m m i t   2 8  
 C o m m i t   2 3  
 C o m m i t   2 4  
 C o m m i t   2 5  
 C o m m i t   2 6  
 C o m m i t   2 7  
 C o m m i t   2 8  
 C o m m i t   2 3  
 C o m m i t   2 4  
 C o m m i t   2 5  
 C o m m i t   2 6  
 C o m m i t   2 7  
 C o m m i t   2 8  
 C o m m i t   2 3  
 C o m m i t   2 4  
 C o m m i t   2 5  
 C o m m i t   2 6  
 C o m m i t   2 7  
 C o m m i t   2 8  
 