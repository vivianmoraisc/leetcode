def romanToInt(r):
    correspondente = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
    contagem = 0

    for i in range(len(r) - 1):  # Percorrer ate o penultimo item
        if correspondente[r[i]] >= correspondente[r[i + 1]]:
            contagem += correspondente[r[i]]
        else:
            contagem -= correspondente[r[i]]

    # Somar o valor do ultimo caracter que nao foi considerado no loop
    contagem += correspondente[r[-1]]

    return contagem

print(romanToInt("MCMXII"))
