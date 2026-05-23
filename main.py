import pyautogui
import subprocess
import pyperclip
import time
import pandas as pd

pyautogui.FAILSAFE = True

# Função para escrever o texto corretamente
def escrever_texto(texto):
    pyperclip.copy(texto)
    pyautogui.hotkey('ctrl', 'v')

# Função para clicar à direita do campo
def direita(posicoes_imagem):
    return (
        posicoes_imagem[0] + posicoes_imagem[2],
        posicoes_imagem[1] + posicoes_imagem[3] / 2
    )

# Abrir Fakturama
subprocess.Popen(
    [r'C:\Program Files\Fakturama2\Fakturama.exe']
)
print('Abrindo Fakturama...')

# Esperar a janela abrir
while True:
    janelas = pyautogui.getWindowsWithTitle('Fakturama')
    if len(janelas) > 0:
        janelas[0].maximize()
        print('Fakturama aberto!')
        break
    time.sleep(1)

# Pequena pausa para carregar totalmente
time.sleep(3)

# fazendo isso para varias produto
tabela_produtos = pd.read_excel(r'C:\Users\Thinkpad\Desktop\Códigos\AVANCADO\RPA_Python\Produtos.xlsx')

for linha in tabela_produtos.index:
    nome = tabela_produtos.loc[linha, 'Nome']
    produto_id = tabela_produtos.loc[linha, 'ID']
    categoria = tabela_produtos.loc[linha, 'Categoria']
    gtin = tabela_produtos.loc[linha, 'GTIN']
    supplier = tabela_produtos.loc[linha, 'Supplier']
    descricao = tabela_produtos.loc[linha, 'Descrição']
    imagem = tabela_produtos.loc[linha, 'Imagem']
    preco = tabela_produtos.loc[linha, 'Preço']
    custo = tabela_produtos.loc[linha, 'Custo']
    estoque = tabela_produtos.loc[linha, 'Estoque']

    # Clique no menu New
    pyautogui.click(125, 29)

    # Clique em New Product
    time.sleep(1)
    pyautogui.click(182, 262)
    time.sleep(2)

    # Campo Item Number
    pyautogui.click(417, 179)
    escrever_texto(str(produto_id))

    # --------------------------------------------------------------------------------

    # Name
    pyautogui.press('tab')
    escrever_texto(str(nome))

    # --------------------------------------------------------------------------------

    # Category
    pyautogui.press('tab')
    escrever_texto(str(categoria))

    # --------------------------------------------------------------------------------

    # GTIN
    pyautogui.press('tab')
    escrever_texto(str(gtin))

    # --------------------------------------------------------------------------------

    # Supplier Code
    pyautogui.press('tab')
    escrever_texto(str(supplier))

    # --------------------------------------------------------------------------------

    # Description
    pyautogui.press('tab')
    escrever_texto(str(descricao))

    # --------------------------------------------------------------------------------

    # Price Gross
    pyautogui.press('tab')
    preco_texto = f'{preco:.2f}'.replace('.', ',')
    escrever_texto(str(preco_texto))

    # --------------------------------------------------------------------------------

    # Cost Price
    pyautogui.press('tab')
    custo_texto = f'{custo:.2f}'.replace('.', ',')
    escrever_texto(str(custo_texto))

    # --------------------------------------------------------------------------------

    # Pular campos
    pyautogui.press('tab')
    pyautogui.press('tab')

    # --------------------------------------------------------------------------------

    # Stock
    pyautogui.press('tab')
    estoque_texto = f'{estoque:.2f}'.replace('.', ',')
    escrever_texto(str(estoque_texto))

    # --------------------------------------------------------------------------------

    # selecionar a imagem
    caminho_imagem = fr'C:\Users\Thinkpad\Desktop\Códigos\AVANCADO\RPA_Python\Imagens Produtos\{imagem}'

    # clicar no botão de adicionar imagem
    time.sleep(1)
    pyautogui.moveTo(1139, 348, duration=0.2)
    pyautogui.click()
    time.sleep(2)

    # escrever o caminho da imagem
    escrever_texto(caminho_imagem)
    time.sleep(1)
    pyautogui.press('enter')
    
    # clicar em salvar
    time.sleep(2)
    pyautogui.click(137, 75)