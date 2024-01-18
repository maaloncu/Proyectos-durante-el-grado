
import PySimpleGUI as sg
def primera_pantalla():
    layout1 = [ [sg.Image(filename="Logo.PNG")], [sg.Button("Comenzar")]]
    window1 = sg.Window("Inicio", layout1, element_justification='c')
    event, values = window1.read()
    if event in ("Exit", sg.WIN_CLOSED):
        window1.close()
    elif event == "Comenzar":
        window1.close()
        


class GUI:
    sg.theme('GreenMono')
    primera_pantalla()
