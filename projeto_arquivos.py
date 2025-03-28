"""""
Projeto: Organizador de Arquivos
Autor: Leandra Arruda de Oliveira
Versão: 0.0.1
Data: 28/03/2025
Descrição: Este programa organiza arquivos em pastas de acordo com a extensão do arquivo.
Pacotes utilizados: os e shutil
"""

import os
import shutil

# 1. Mostrar diretório atual
diretorio_de_trabalho = os.getcwd()
print(diretorio_de_trabalho)

# 2. Definir extensões para cada tipo de arquivo
tipos_arquivos = {
    'planilhas': ['.xlsx'],
    'documentos': ['.docx']
}

# 3. Criar pastas necessárias
pastas_necessarias = ['planilhas', 'documentos']
for pasta in pastas_necessarias:
    if not os.path.exists(pasta):
        os.mkdir(pasta)
        print(f"Pasta criada: {pasta}")

# 4. Mover os arquivos para as pastas corretas
for arquivo in os.listdir(diretorio_de_trabalho):
    # Ignorar pastas e arquivos que não são os especificados
    if os.path.isdir(arquivo):
        continue
        
    _, extensao = os.path.splitext(arquivo)  # Obtém a extensão do arquivo
    extensao = extensao.lower()  # Garantir que está em minúsculas

    for pasta, extensoes in tipos_arquivos.items():
        if extensao in extensoes:
            origem = os.path.join(diretorio_de_trabalho, arquivo)
            destino = os.path.join(diretorio_de_trabalho, pasta, arquivo)
            shutil.move(origem, destino)
            print(f"Movido: {arquivo} → {pasta}/")
            break

print("Organização concluída!")