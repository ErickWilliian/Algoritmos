numeros = [1, 2, 3, 4, 5, 6, 71, 10, 8, 9]
        # [1, 2, 3, 4, 5, 6, 8, 9, 10, 71]

def busca_binaria():
    number = 1 # int(input("Digite o número você quer: "))
    numeros.sort()
    minValue = 0
    maxValue = len(numeros)
    naoEncontrado = True

    while naoEncontrado:
        meio = (maxValue + minValue) // 2

        if number == numeros[meio - 1]:
            return f"O numero {number} está na posição {meio - 1}"

        elif number >= numeros[meio]:
            minValue = meio + 1

        elif number <= numeros[meio - 1]:
            maxValue = maxValue - meio

        else:
            return "Esse número não esta presente na lista !"


print(busca_binaria())
