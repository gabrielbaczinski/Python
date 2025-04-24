def produto_cartesiano(conjunto_a, conjunto_b):
    conjunto_a = set(conjunto_a)
    conjunto_b = set(conjunto_b)
    return {(a, b) for a in conjunto_a for b in conjunto_b}
def montar_conjuntos(a, b):
    preencher_a = input('Digite os números do conjunto A separados por " ": ')
    preencher_b = input('Digite os números do conjunto B separados por " ": ')
    a.clear()
    b.clear()
    a.extend(map(int, preencher_a.split()))
    b.extend(map(int, preencher_b.split()))
    conjunto_a = set(a)
    conjunto_b = set(b)
    return conjunto_a, conjunto_b

def verificar_subconjunto(conjunto_a, conjunto_b):
    subconjunto = conjunto_a.issubset(conjunto_b)
    subconjunto_proprio = subconjunto and conjunto_a != conjunto_b
    return subconjunto, subconjunto_proprio
def menu(selector):
    menu = ('1 - União\n'
            '2 - Intersecção\n'
            '3 - Diferença\n'
            '4 - Produto Cartesiano\n'
            '5 - Subconjuntos AB\n'
            '6 - Subconjuntos BA\n'
            '7 - Alterar conjuntos\n'
            '8 - Sair\n')
    print(menu)
    return menu


print('Seja bem-vindo')
a = []
b = []
conjunto_a, conjunto_b = montar_conjuntos(a, b)
menu(None)

loop = True
while loop:
    selector = int(input('O que deseja fazer? '))
    if selector == 1:
        print(f"União de A e B: {conjunto_a.union(conjunto_b)}")
    elif selector == 2:
        print(f"Interseção de A e B: {conjunto_a.intersection(conjunto_b)}")
    elif selector == 3:
        print(f"Diferença de A e B: {conjunto_a.difference(conjunto_b)}")
    elif selector == 4:
        plano_cartesiano = produto_cartesiano(conjunto_a, conjunto_b)
        print("Plano cartesiano entre A e B:", plano_cartesiano)
    elif selector == 5:
        subconjunto, proprio = verificar_subconjunto(conjunto_a, conjunto_b)
        print(f"A é subconjunto de B: {subconjunto}")
        print(f"A é subconjunto próprio de B: {proprio}")
    elif selector == 6:
        subconjunto, proprio = verificar_subconjunto(conjunto_b, conjunto_a)
        print(f"B é subconjunto de A: {subconjunto}")
        print(f"B é subconjunto próprio de A: {proprio}")
    elif selector == 7:
        conjunto_a, conjunto_b = montar_conjuntos(a, b)
    elif selector == 8:
        loop = False
        print('Encerrando...')