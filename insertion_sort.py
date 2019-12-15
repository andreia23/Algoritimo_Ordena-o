from time import perf_counter

#------------- insertion sort ------------#

def insertionsort(vetor):
    inicio = perf_counter()
    i = 1
    while i < len(vetor):
        temp = vetor[i]
        print('temp: ',temp)
        trocou = False
        j = i - 1
        print('j: ',j)
        
        while j >= 0 and vetor[j] > temp:
            vetor[j + 1] = vetor[j]
            print('1° vetor: ',vetor)
            trocou = True
            j -= 1

        if trocou:
            vetor[j + 1] = temp
            print('2° vetor: ',vetor)
            print()
        i += 1

    fim = perf_counter() - inicio
    return vetor, fim




lista = [2,8,5,3,1]
print(insertionsort(lista))
