# Implementação do Counting Sort


def countingSort(array):
    size = len(array)
    output = [0] * size
    global increment

    # Inicializa o array de contagem
    count = [0] * 10

    # Incrementa um contador para cada elemento no array de contagem
    for i in range(0, size):
        count[array[i]] += 1
        increment = increment + 1


    # Armazena o contador acumulado
    for i in range(1, 10):
        count[i] += count[i - 1]
        increment = increment + 1

    # Encontra o índice de cada elemento do array original no array de contagem
    # Coloca os elementos no array de saída
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        increment = increment + 1

    # Copia os elementos ordenados no array original
    for i in range(0, size):
        array[i] = output[i]


data = [4, 2, 2, 8, 3, 3, 1]
increment = 0
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)

print("Number of Increments: ")
print(increment)




