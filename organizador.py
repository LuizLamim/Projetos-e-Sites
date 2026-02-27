import os
import shutil

def organizar_pasta(caminho_da_pasta):
    # Dicionário mapeando os nomes das pastas para as extensões de arquivo
    extensoes = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Instaladores": [".exe", ".msi", ".dmg", ".zip", ".rar"],
        "Scripts": [".py", ".js", ".html", ".css"]
    }

    # Verifica se o caminho existe
    if not os.path.exists(caminho_da_pasta):
        print("Caminho não encontrado. Verifique e tente novamente.")
        return

    # Percorre todos os arquivos na pasta
    for arquivo in os.listdir(caminho_da_pasta):
        caminho_arquivo = os.path.join(caminho_da_pasta, arquivo)

        # Pula se for um diretório
        if os.path.isdir(caminho_arquivo):
            continue

        nome, ext = os.path.splitext(arquivo)
        ext = ext.lower()

        # Encontra a pasta correta para a extensão
        pasta_destino = "Outros"
        for pasta, exts in extensoes.items():
            if ext in exts:
                pasta_destino = pasta
                break

        # Cria a pasta de destino se não existir
        caminho_destino = os.path.join(caminho_da_pasta, pasta_destino)
        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)

        # Move o arquivo
        shutil.move(caminho_arquivo, os.path.join(caminho_destino, arquivo))
        print(f"Movido: {arquivo} -> {pasta_destino}")

# Como usar: Troque o caminho abaixo pela pasta que você quer organizar
pasta_alvo = r"C:\Users\SeuUsuario\Downloads"
organizar_pasta(pasta_alvo)
print("Organização concluída!")