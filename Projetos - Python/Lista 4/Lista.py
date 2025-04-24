import random
numeros = []

for i in range(5): 
    numero = round(random.uniform(-10.0, 10.0), 2)
    numeros.append(numero)
print(numeros)

numeros_invertidos = list(reversed(numeros))
relacao = {i + 1: numeros_invertidos[i] 
    for i in range(len(numeros_invertidos))}
print(f"Inverse: {list(relacao.values())}")

