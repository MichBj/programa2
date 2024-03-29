#Empezamos creando nuestra variable dimensional
b=[
    [7,8,9],
    [1,2,3],
    [4,5,6]
    ]
#imprimimos nuestra variable original
print("Arreglo Bibimensional 3x3 original ",b)
#haciendo uso del sorf ordenamos los valores de nuestra variable de forma ascendente
b.sort()
#inprimimos la variable  ordenadad
print("Arreglo Bibimensional 3x3 ordenado ",b)
#con esto finaliza el codigo
def burbuja(arreglo):
    # Calculamos la longitud del arreglo para tener un código más limpio
    longitud = len(arreglo)
    # Recorremos todo el arreglo
    for i in range(longitud):
        # Dentro del ciclo, volvemos a recorrerlo. Pero ahora hasta el penúltimo elemento
        for indice_actual in range(longitud - 1):
            indice_siguiente_elemento = indice_actual + 1
            # Si el actual es mayor que el siguiente, ...
            # Nota: para un orden inverso, cambia `>` por `<`
            if arreglo[indice_actual] > arreglo[indice_siguiente_elemento]:
                # ... intercambiamos los elementos
                arreglo[indice_siguiente_elemento], arreglo[indice_actual] = arreglo[indice_actual], arreglo[indice_siguiente_elemento]
    # No hace falta regresar nada, pues el arreglo ya fue modificado


# Modo de uso.
mi_arreglo = [3, 4, 1, 2, 3, 7, 55, 34, 43, 3]
print("Original: ")
print(mi_arreglo)
burbuja(mi_arreglo)
print("Ordenado: ")
print(mi_arreglo)