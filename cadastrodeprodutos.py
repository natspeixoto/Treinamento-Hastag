# Precondição: Anota o passo a passo do projeto
# Como você constroi o projeto de automação? Pense como você faria manualmente. O python está simulando minhas ações manuais
# O pyautogui assume a tela, o mouse e o teclado. Se quiser interromper a automação, colocar o cursor no canto superior esquerdo
# Link que ele vai simular o sitema da empresa
# Ctrl + l para selecionar o campo de url
# Passo1: Acessar o link da empresa

import pyautogui
import pandas as pd
import time


#importar a base de produtos
tabela = pd.read_csv("produtos_teste.csv")
print(tabela)


pyautogui.PAUSE= 1.0

# abrir o navegador (chrome)
pyautogui.press("win") 
pyautogui.write("chrome")
pyautogui.press("enter")


# acesar o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) #só afetará a linha 24

#maximizar a janela
pyautogui.click(x=1825, y=53)

# Passo2:Fazer login
pyautogui.click(x=682, y=527),pyautogui.write("aulahas@yopmail.com")
pyautogui.press("tab"),pyautogui.write("321")
pyautogui.click(x=934, y=769)

for linha in tabela.index:
    pyautogui.click(x=563, y=364)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press("tab")
    if not pd.isna(tabela.loc[linha, 'obs']):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.click(x=823, y=797)  
    pyautogui.scroll(5000)
