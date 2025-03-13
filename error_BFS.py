from arbol import Nodo

def buscar_solucion_BFS(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial  # Corregido: devolver el nodo solución correcto

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
    nodo_solucion = []  # No es necesario aquí, pero se mantiene según tu estructura
    visitados = []
    resultado = []
    nodo_inicial = Nodo(estado_inicial)

    nodo = buscar_solucion_BFS(nodo_inicial, solucion, visitados)

    # Mostrar resultado
    resultado = []  # Se inicializa vacío
    if nodo is not None:  # Corregido: Verificar que `nodo` no sea `None`
        while nodo is not None:  # Corregido: Evitar error al acceder a `None`
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse()
        print(resultado)
    else:
        print("No se encontró una solución.")
