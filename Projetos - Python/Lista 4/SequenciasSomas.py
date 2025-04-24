def somatorio(x, y):
    soma = 0
    for i in range(1,4,1):
        y = 1
        while y < 3:
            valor = (x*y-5)
            soma += valor
            print(f"Resultado: {valor} - Soma: {soma}")
            y += 1
        x +=1
    return print(f"Somatório = {soma}")
        
x = 1
y = 1
(somatorio(x,y))


