import random
alunos = []
media = []

def notasAlunos():
    for i in range(6):
        notas = [] 
        for j in range(4):
            #nota = float(input(f'Digite a nota {j+1} do aluno {i+1}: '))
            nota = round(random.uniform(0.1, 10.0), 1)
            notas.append(nota)
    
        media_aluno = round(sum(notas) / len(notas), 2)
        media.append(media_aluno)  
        alunos.append(notas)  
        
    print("Médias dos alunos:", media)
    
    acimaM = 0
    for m in media:
        if m >= 7.0:
            acimaM += 1
    print(f'Número de alunos com média maior ou igual a 7.0: {acimaM}')
        
    
notasAlunos()


