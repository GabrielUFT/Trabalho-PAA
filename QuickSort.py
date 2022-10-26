'''
## Couting Sort

def countingSort(arr):
    size = len(arr)
    output = [0] * size

    # count array initialization
    count = [0] * 10

    # storing the count of each element 
    for m in range(0, size):
        count[arr[m]] += 1

    # storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]

    # place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[arr[m]] - 1] = arr[m]
        count[arr[m]] -= 1
        m -= 1

    for m in range(0, size):
        arr[m] = output[m]

'''

# Implementação do Quick sort

# Implementação utiliza o último elemento da lista como pivô
# Tem um ponteiro para acompanhar os elementos menores que o pivô
# No final da função partition(), o ponteiro é trocado pelo pivô
# para chegar a um número "ordenado" em relação ao pivô


# Função para encontrar o local da partição
def partition(array, low, high):
 
    # Escolhe o elemento mais a direita como pivô
    pivot = array[high]
 
    # Aponta o maior elemento
    i = low - 1
 
    # Percorre todos os elementos
    # Compara cada elemento com o pivô
    for j in range(low, high):
        print('comparate')
        if array[j] <= pivot:
            print('swap')
 
            # Se um elemento menor que o pivô for encontrado
            # Troca ele com o maior elemento apontado por i
            i = i + 1
 
            # Troca o elemento i pelo elemento j
            (array[i], array[j]) = (array[j], array[i])
 
    # Troca o pivô com o maior elemento apontado por i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Retorna a posição onde a partição finalizou
    return i + 1
# Função para executar o QuickSort

def quickSort(array, low, high):
	if low < high:

		#Encontre o elemento pivô tal que
        # elemento menor que pivô está à esquerda
        # elemento maior que pivô está à direita
		pi = partition(array, low, high)

		# Chamada recursiva para a esquerda do pivô
		quickSort(array, low, pi - 1)

		# Chamada recursiva para a direita do pivô
		quickSort(array, pi + 1, high)


data = [3,5,2,7,12,14,10,0,4,5,6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)



