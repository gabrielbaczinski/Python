import random
num = []

def sorteia():
    for i in range(6):
        num.append(random.randint(1, 10))
    print(num)
    
def somaPar(num):
    pares = []
    for n in num:
        if n % 2 == 0:
            pares.append(n)
    soma = sum(pares)
    pares_ordenados = [(i + 1, pares[i]) for i in range(len(pares))]
    print(f"Pares ordenados: {pares_ordenados}")  
    return print(f"Soma dos números pares: {soma}")

sorteia()
somaPar(num)

