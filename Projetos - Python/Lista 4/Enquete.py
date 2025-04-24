def contagem_votos():
  votos = [0] * 6  

  while True:
    voto = int(input("Digite seu voto (1-6) ou 0 para sair: "))
    if voto == 0:
      break
    elif 1 <= voto <= 6:
      votos[voto - 1] += 1
    else:
      print("Voto inválido. Digite um número entre 1 e 6 ou 0 para sair.")

  total_votos = sum(votos)

  print("Linguagem\tVotos\t%")
  print("-------------------------")
  linguagens = ["Python", "C++", "Java", "Rust", "C#", "Outro"]
  for i in range(len(votos)):
    percentual = (votos[i] / total_votos) * 100
    print(f"{linguagens[i]}\t{votos[i]}\t{percentual:.1f}%")
  print(("-------------------------"))
  print(f"Total\t{total_votos}")

contagem_votos()




