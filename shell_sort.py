from time import perf_counter

#---------------- shellsort ----------------#

def shellsort(lista): 
    inicio = perf_counter()

    n = len(lista) 
    divisao = n//2 
    while divisao > 0:   
        for i in range(divisao,n): 
            temp = lista[i] 
            j = i 
            while  j >= divisao and lista[j-divisao] >temp: 
                lista[j] = lista[j-divisao]
                j -= divisao 
            lista[j] = temp 
        divisao //= 2

    fim = perf_counter() - inicio
    return lista, fim
