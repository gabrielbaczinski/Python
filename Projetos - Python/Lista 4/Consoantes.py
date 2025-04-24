import random
import string

letras = []
consoantes = []

def verifica_consoante(letra):
    return letra not in "aeiou"

def sorteia_letras():
    for i in range(6):
        letra = random.choice(string.ascii_lowercase)  
        letras.append(letra)
        if verifica_consoante(letra): 
            consoantes.append(letra)
    return print(f"Letras sorteadas: {letras}")

def mapear_consoante():
    print(f"Número de consoantes lidas: {len(consoantes)}")
    relacao = {letra for letra in consoantes}  
    print(f"Relação das consoantes: {relacao}")  


sorteia_letras()
mapear_consoante()










