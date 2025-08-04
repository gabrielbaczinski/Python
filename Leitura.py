import pyautogui
import time
import pyautogui as pag

# Tempo para você abrir o jogo
for i in range(3, 0, -1):
    print(f"Iniciando em {i}...")
    time.sleep(1)

print("Começando a monitorar a tela!")

# Caminho da imagem de referência
imagem_botao = "proxima_fase_auto.png"

# Loop infinito que verifica a cada 1 segundo
while True:
    try:
        local = pyautogui.locateCenterOnScreen(imagem_botao, confidence=0.8)
        if local:
            print(f"Botão encontrado em {local}, clicando!")
            pyautogui.click(local)
            time.sleep(2)

    except pyautogui.ImageNotFoundException:
        print("Erro ao buscar imagem, tentando novamente...")
    time.sleep(1)
