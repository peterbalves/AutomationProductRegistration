import pyautogui
import pandas as pd
import time

pyautogui.PAUSE=1
link = ''
tabela = pd.read_csv('produtos.csv')
def position():
    time.sleep(5)
    # x,y = pyautogui.position()
    # print('position x = {} and position y = {}'.format(x,y))
    print(pyautogui.position())
def launchpad():
    pyautogui.click(x=122,y=860)
    
    time.sleep(1.5)

    pyautogui.click(x=718,y=37)

    pyautogui.write('safari')

    time.sleep(1.5)

    pyautogui.click(x=711,y=123)

    time.sleep(1.5)

    pyautogui.click(x=167, y=54)

    pyautogui.click(x=706,y=23)
    pyautogui.write(link)


    time.sleep(1)

    pyautogui.press('enter')
    
    time.sleep(1.5)

    pyautogui.click(x=575,y=296)
    pyautogui.write('blablabla123')

    pyautogui.press('tab')
    pyautogui.write('13122004')

    time.sleep(1)

    pyautogui.click(x=709, y=449)

def cadraastroproduto():
    for linha in tabela.index:
        pyautogui.click(x=809, y=204)
        pyautogui.write(tabela.loc[linha, 'codigo'])
        pyautogui.press('tab')

        pyautogui.write(tabela.loc[linha, 'marca'])
        pyautogui.press('tab')

        pyautogui.write(tabela.loc[linha, 'tipo'])
        pyautogui.press('tab')

        pyautogui.write(str(tabela.loc[linha, 'categoria']))
        pyautogui.press('tab')

        pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
        pyautogui.press('tab')

        pyautogui.write(str(tabela.loc[linha, 'custo']))
        pyautogui.press('tab')

        obs = tabela.loc[linha, 'obs']
        if not pd.isna(obs):
            pyautogui.write(obs)
            pyautogui.click(x=651, y=772)
        else:
            pass
        pyautogui.click(x=651, y=772)
        pyautogui.scroll(-5000)
        time.sleep(2)
        pyautogui.scroll(5000)
        time.sleep(2)
position()
