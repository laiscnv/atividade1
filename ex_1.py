def contar_menores(lista, num):
    inicio = 0
    fim = len(lista) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] < num:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return inicio

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
resultado = contar_menores(primos, 67)

print(f"A quantidade de números primos menores que 67 é {resultado}")