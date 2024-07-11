import pyautogui
import time

# PASSO 1 - Entrar no sistema
 
pyautogui.PAUSE = 1.0 # Definindo um tempo para cada execução de comando, para que o pc tenha tempo para reconhecer cada comando 

# Abrir o navegador (apertar botão windows e pesquisar por edge (nome do navegador))
pyautogui.press("win") # botão do windows
pyautogui.write("edge") # Digitar edge (nome do navegador)
pyautogui.press("enter") # Pressionar Enter
 
# Entrar no link do sistema (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # Digitar na barra de pesquisa o link do site
pyautogui.press("enter") # Pressionar Enter


# Usando time.sleep para esperar 3 segundos até o carregamento completo do site, como precaução
time.sleep(3) 
#               time.sleep                 !=               pyautogui.PAUSE  
# Tempo de espera em um momento específico / Tempo de espera na execução de cada comando

# PASSO 2 - Fazer login no sistema

# Selecionar o campo de Email e escrever o email
# Selecionar o campo de Senha e escrever a senha
# E clicar em enter

# Para selecionar um campo na tela (campo de email no caso), é preciso direcionar o mouse ao local do campos para clicar.
# É preciso pegar as coordenadas (x, y) da tela -> 'auxiliar.py'
pyautogui.click(x=656, y=357) # Coordenadas adquiridas com o código auxiliar

# Agora é digitar o email
pyautogui.hotkey("ctrl", "a") # Tratando para evitar falhas caso esteja preenchendo o email automaticamente
pyautogui.write("teste@gmail.com") # Digitar o email

 # Para passar pro campo de senha, posso tanto especificar as coordenadas em click(), ou somente pressionar 'tab'
 # Em formulários, a tecla tab avança para o próximo campo
pyautogui.press("tab")
pyautogui.hotkey("ctrl", "a")
pyautogui.write("senhaTeste")

# E agora, clicar no botão de logar
# Para isso vou especificar as coordenadas
pyautogui.click(x=651, y=508) 

time.sleep(3)

# PASSO 3 - Importar a base de dados

import pandas

produtos = pandas.read_csv("produtos.csv")


# PASSO 4 - Cadastrar produtos


# No .loc[] se menciona a linha e coluna da tabela - como no for, o contador 'linha' está percorrendo sobre as linhas da tabela (produtos.index), o contador 'linha' ja assume as linhas
# Então é so mencionar o nome da coluna.
# str() serve para converter o que está no parentesis para uma string.
for linha in produtos.index: # Para cada linha dentro de uma lista com todas as linhas da tabela.
    # codigo 
    pyautogui.click(x=715, y=246)
    codigo = str(produtos.loc[linha, "codigo"]) #.loc: Localiza um item em uma linha em tal coluna (função do pandas)
    pyautogui.write(codigo)
    # marca
    pyautogui.press("tab")
    marca = str(produtos.loc[linha, "marca"])
    pyautogui.write(marca)
    # tipo
    pyautogui.press("tab")
    tipo = str(produtos.loc[linha, "tipo"])
    pyautogui.write(tipo)
    # categoria
    pyautogui.press("tab")
    categoria = str(produtos.loc[linha, "categoria"])
    pyautogui.write(categoria)
    # preco unitario
    pyautogui.press("tab")
    preco = str(produtos.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    # custo
    pyautogui.press("tab")
    custo = str(produtos.loc[linha, "custo"])
    pyautogui.write(custo)
    # obs
    pyautogui.press("tab")
    obs = str(produtos.loc[linha, "obs"])
    # Para tratar linhas nulas (nan) em OBS:
    if obs != "nan":
        pyautogui.write(obs)
    else:
        pyautogui.write("Sem Observacao")
    # Enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

# Scroll para subir a página ao topo e repetir o processo de cadastro
pyautogui.scroll(5000) # Se o número for positivo o scroll é pra cima, se for negativo é pra baixo. É medido em pixel.

# PASSO 5 - Repetir o passo 4 para todos os itens da tabela
# For linha in produtos.index()
# produtos.index() -> o index assume cada linha da tabela, por isso de: 'Para cada linha dentro de uma lista com todas as linhas da tabela.'