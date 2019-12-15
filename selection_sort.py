from time import perf_counter

#----------- selection sort -------------#

def selectionsort(vetor):
    inicio = perf_counter()
    for i in range(0, len(vetor) - 1):
        menor = i
        print('1°menor: ',menor)
        #busca o menor elemento
        for j in range(i + 1, len(vetor)):
            if vetor[j] < vetor[menor]:
                menor = j
                print('2°menor: ',menor)
        
        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            print('vetor[i], vetor[menor]: ',vetor[i], vetor[menor])

    fim = perf_counter() - inicio

    return vetor, fim


lista = [2,8,5,3,1]
print(selectionsort(lista))
