

import pyautogui

quantidade = int(input("insira quantidade de nomes"))

def copio():
    pyautogui.moveTo(1700,75,duration=0.1)
    pyautogui.dragTo(1506,77,button='left',duration=2)
    pyautogui.hotkey('ctrl','c')

    pyautogui.moveTo(909,291,duration=1)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('tab')

    pyautogui.moveTo(1639,58,duration=0.1)
    pyautogui.dragTo(1506,60,button='left',duration=2)
    pyautogui.hotkey('ctrl','c')

    pyautogui.moveTo(909,291,duration=1)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('tab')

    pyautogui.moveTo(1878,132,duration=0.1)
    pyautogui.dragTo(1506,133,button='left',duration=2.5)
    pyautogui.hotkey('ctrl','c')

    pyautogui.moveTo(909,291,duration=1,)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('tab')

    pyautogui.moveTo(1761,113,duration=0.1)
    pyautogui.dragTo(1508,114,button='left',duration=2.5)
    pyautogui.hotkey('ctrl','c')

    pyautogui.moveTo(909,291,duration=1)
    pyautogui.leftClick()
    pyautogui.hotkey('ctrl','v')
    pyautogui.hotkey('down','left') 
    pyautogui.hotkey('left')
    pyautogui.hotkey('left')

   

    pyautogui.moveTo(1700,75,duration=0.1)
    pyautogui.leftClick()
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    pyautogui.hotkey('down')
    


for _ in range(quantidade):
    copio()
