import PySimpleGUI as sg

# Diccionario de datos para las líneas y estaciones
data = {
    'Linea A': ['Estacion A1', 'Estacion A2', 'Estacion A3', 'Estacion A4', 'Estacion A5'],
    'Linea B': ['Estacion B1', 'Estacion B2', 'Estacion B3', 'Estacion B4', 'Estacion B5'],
    'Linea C': ['Estacion C1', 'Estacion C2', 'Estacion C3', 'Estacion C4', 'Estacion C5']
}

layout = [
    [sg.Text('Linea de Origen', size=15), sg.Combo([linea for linea in data], expand_x=True, enable_events=True, key='LineaOrigen')],
    [sg.Text('Estacion de Origen', size=15), sg.Combo([], size=20, expand_x=True, key='EstacionOrigen')],
    [sg.Text('Linea de Destino', size=15), sg.Combo([linea for linea in data], expand_x=True, enable_events=True, key='LineaDestino')],
    [sg.Text('Estacion de Destino', size=15), sg.Combo([], size=20, expand_x=True, key='EstacionDestino')],
]

window = sg.Window("Selección de estaciones", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'LineaOrigen':
        linea_origen = values['LineaOrigen']
        window['EstacionOrigen'].update(values=data[linea_origen])
    elif event == 'LineaDestino':
        linea_destino = values['LineaDestino']
        window['EstacionDestino'].update(values=data[linea_destino])

window.close()