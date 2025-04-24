def conta_letras(palavra):
    repetidas = {}
    for letra in palavra:
        if letra in repetidas:
            repetidas[letra] += 1
        else:
            repetidas[letra] = 1
            
    repetidas = {letra:contagem for letra, contagem in repetidas.items() if contagem > 1}
    return repetidas

print(conta_letras('banana'))