import pyautogui
import time

def preencher_formulario_repetitivo():
    print("O script vai começar em 5 segundos. Clique na caixa de texto onde deseja digitar!")
    
    # Dá 5 segundos para você clicar no campo onde o texto deve ser inserido
    time.sleep(5)
    
    # Lista de mensagens ou dados que você quer preencher
    dados_para_digitar = [
        "Primeiro formulário preenchido com sucesso.",
        "Segundo envio automatizado.",
        "Terceiro teste de automação."
    ]
    
    for dado in dados_para_digitar:
        # Digita o texto como se fosse um humano (intervalo de 0.05s entre as teclas)
        pyautogui.write(dado, interval=0.05)
        
        # Pressiona a tecla 'Enter' para enviar ou pular de linha
        pyautogui.press('enter')
        
        # Espera 1 segundo antes de ir para o próximo
        time.sleep(1)
        
    print("Automação concluída!")

preencher_formulario_repetitivo()