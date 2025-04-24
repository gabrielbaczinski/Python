import random
vetorA = []

def calcularVetor():
    soma = 0
    for i in range(5):
        vetorA.append(random.randint(-50,50))
    print(f'Lista de Vetores: {vetorA}')
    
    for i in vetorA:
        quadrado = i ** 2
        soma += quadrado
    print(f'Soma dos quadrados: {soma}')
    
calcularVetor() 

