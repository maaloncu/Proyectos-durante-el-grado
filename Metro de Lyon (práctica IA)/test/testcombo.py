import PySimpleGUI as sg

data = {f'Company {i+1}':[f'Company {i+1} - Item {j+1}' for j in range(5)] for i in range(3)}


layout = [
    [sg.Text('Company', size=8), sg.Combo([company for company in data], expand_x=True, enable_events=True, key='Company')],
    [sg.Text('Item', size=8), sg.Combo([], size=20, expand_x=True, key='Item')],
    
]
window = sg.Window("Title", layout)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Company':
        company = values['Company']
        window['Item'].update(values=data[company])

window.close()