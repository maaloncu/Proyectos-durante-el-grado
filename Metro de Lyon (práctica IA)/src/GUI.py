import PySimpleGUI as sg

from Algoritmo import Algoritmo
from Metro import Metro


def segunda_pantalla():

    data = {
            'Linea A': ["Perrache", "Ampère – Victor Hugo", "Bellecour", "Cordeliers",
                        "Hôtel de Ville–Louis Pradel", "Foch", "Masséna", "Charpennes – Charles Hernu",
                        "République – Villeurbanne", "Gratte-Ciel", "Flachet – Alain Gilles", "Cusset", 
                        "Laurent Bonnevay – Astroballe", "Vaulx-en-Velin – La Soie"],

            'Linea B': ["Charpennes – Charles Hernu", "Brotteaux", "Gare Part-Dieu – Vivier Merle", 
                        "Place Guichard – Bourse du Travail", "Saxe-Gambetta", "Jean Macé", "Place Jean Jaurès", 
                        "Debourg", "Stade de Gerland", "Oullins Gare"],

            'Linea C': ["Hôtel de Ville–Louis Pradel", "Croix-Paquet", "Hénon", "Cuire", ],

            'Linea D': ["Gare de Vaise", "Valmy", "Gorge de Loup", "Vieux Lyon – Cathédrale Saint-Jean", 
                        "Bellecour", "Guillotière – Gabriel Péri", "Saxe-Gambetta", "Garibaldi", 
                        "Sans Souci", "Monplaisir-Lumière", "Grange Blanche", "Laënnec", "Mermoz-Pinel", 
                        "Parilly", "Gare de Vénissieux"]
        }
        # Colores específicos para cada opción
    #colores_lineas = {
     #       'Linea A': 'green',
      #      'Linea B': 'blue',
       #     'Linea C': 'orange',
        #     'Linea D': 'red'
        #}
    
  

    trasbordo = ["Si", "No"]
    tipo = ["Tiempo", "Distancia"]

    menu_def = [["Ayuda", ["Sobre la aplicacion",  "Exit"]]]


    layout2columder  = [[sg.Text("Linea de Origen"), sg.Combo([linea for linea in data], expand_x=True, enable_events=True, key='LineaOrigen')],
                        #[sg.Text("Linea de Origen"), sg.Combo([linea for linea in data], expand_x=True, enable_events=True, key='LineaOrigen', background_color=colores_lineas )],



                       [sg.Text("Estacion de Origen"), sg.Combo([], size=20, expand_x=True, key='_origen_')],
                       [sg.Text("Linea de Destino"), sg.Combo([linea for linea in data], expand_x=True, enable_events=True, key='LineaDestino')],
                       [sg.Text("Estacion de Destino"), sg.Combo([],size=20, expand_x=True, key='_destino_')],

                       [sg.Text("Criterio:", key='_textotipo_', visible=True),
                        sg.Combo(tipo, key='_combotipo_', visible=True, readonly=True)],
                       [sg.Text("Trasbordo:", key='_textotrasbordo_', visible=True),
                        sg.Combo(trasbordo, key='_combotrasbordo_', visible=True, readonly=True)],
                       [sg.pin(sg.Text("Tiempo: ", key='_resultadoT_', visible=False)),
                        sg.Text(text="", key='_tiempo_', visible=False)],
                       [sg.pin(sg.Text("Distancia: ", key='_resultadoD_', visible=False)),
                        sg.Text(text="", key='_distancia_', visible=False)],
                       [sg.Exit(), sg.Button("Buscar ruta"), sg.Button("Volver")],
                       ]
    layout2columizq = [[sg.Image(filename="metro_lyon_700.PNG")]]
    layout2 = [[sg.Column(layout2columizq), sg.VSeperator(), sg.Column(layout2columder)],
               [sg.MenubarCustom(menu_def, tearoff=False)]        
               ]
    window2 = sg.Window("Selección de ruta", layout2, modal=True, element_justification='c')
    while True:
        event, values = window2.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        elif event == 'LineaOrigen':
            linea_origen = values['LineaOrigen']
            window2['_origen_'].update(values=data[linea_origen])
        
        elif event == 'LineaDestino':
            linea_destino = values['LineaDestino']
            window2['_destino_'].update(values=data[linea_destino])
          

        if event == "Sobre la aplicacion":
            window2.close()
            pantalla_extra()
            
        if event == "Volver":
            window2.close()
            primera_pantalla()
        if event == "Buscar ruta":
            if window2['_origen_'].get() == "" or window2['LineaOrigen'].get() == "" or window2['LineaDestino'].get() == "" or window2['_destino_'].get() == "" or \
                    window2['_combotipo_'].get() == "" or window2['_combotrasbordo_'].get() == "":
                sg.popup_error("Rellena todos los campos")
            else:
                metro = Metro()
                if window2['_combotrasbordo_'].get() == "No":
                    trasbordo = False
                else:
                    trasbordo = True
                algoritmo = Algoritmo(origen=metro.map[window2['_origen_'].get()],
                                      destino=metro.map[window2['_destino_'].get()], tipo=window2['_combotipo_'].get(),
                                      trasbordo=trasbordo, metro=metro)
                res = algoritmo.aestrella()
                if res is None:
                    sg.popup_error("No es posible llegar a la estación destino sin hacer trasbordo")
                    continue
                tiporecibido = window2['_combotipo_'].get()
                trans = window2['_combotrasbordo_'].get()
                window2.close()
                tercera_pantalla(res, tiporecibido, trans)


def tercera_pantalla(res, tiporecibido, trans):
    layout3inicial = [[sg.Text("Estacion Origen:"), sg.Text(res[1][0].name),
                       sg.Text("Estacion Destino:"), sg.Text(res[1][len(res[1]) - 1].name),
                       sg.Text("Criterio:", key='_textotipo_', visible=True), sg.Text(tiporecibido),
                       sg.Text("Trasbordo:", key='_textotrasbordo_', visible=True), sg.Text(trans)]]
    layout3fin = [[sg.Exit(), sg.Button("Volver")]]
    layout3columizq = [[sg.Image(filename="metro_lyon_700.PNG")]]

    camino = ""
    for i in res[1]:
        camino += i.name + "\n"
    if tiporecibido == "Tiempo":
        layout3columder = [[sg.pin(sg.Text("Tiempo: ", key='_resultadoT_', visible=True)),
                            sg.Text(str(res[0]) + " minutos", key='_tiempo_', visible=True)],
                           [sg.pin(sg.Text("Distancia: ", key='_resultadoD_', visible=False)),
                            sg.Text(text="", key='_distancia_', visible=False)],
                           [sg.Text("Recorrido: ", key='_recorrido_')], [sg.Text(camino, key='_camino_')], ]
    else:
        layout3columder = [[sg.pin(sg.Text("Tiempo: ", key='_resultadoT_', visible=False)),
                            sg.Text(text="", key='_tiempo_', visible=False)],
                           [sg.pin(sg.Text("Distancia: ", key='_resultadoD_', visible=True)),
                            sg.Text(str(res[0]) + " kilómetros", key='_distancia_', visible=True)],
                           [sg.Text("Recorrido: ", key='_recorrido_')], [sg.Text(camino, key='_camino_')], ]
    layout3 = [[layout3inicial], [sg.Column(layout3columizq), sg.VSeperator(), sg.Column(layout3columder)],
               [layout3fin]]
    window3 = sg.Window("Selección de ruta", layout3, modal=True, element_justification='c')
    while True:
        event, values = window3.read()
        if event in (sg.WINDOW_CLOSED, "Exit"):
            window3.close()
            break

        if event == "Volver":
            window3.close()
            segunda_pantalla()


def primera_pantalla():
    layout1 = [[sg.Image(filename="logo_metro_lyon_escalado_mas_pequeno.PNG")], [sg.Button("Comenzar")]]
    window1 = sg.Window("Inicio", layout1, element_justification='c')
    event, values = window1.read()
    if event in ("Exit", sg.WIN_CLOSED):
        window1.close()
    elif event == "Comenzar":
        window1.close()
        segunda_pantalla()

def pantalla_extra():
    layout4ini= [[sg.Text("Este es un ejecutable que te permitira poder calcular la ruta más eficiente para viajar en el metro de Lyon")],
                 [sg.Text("La actividad cuenta como parte de la Practica de Búsqueda de la Asignatura de Inteligencia Artificial de la Universidad Politecnica de Madrid ")],
                 [sg.Text("Los compañeros que hemos hecho posible este trabajo han sido:")],
                 [sg.Text("Ángel Astiazarán Gafo")],
                 [sg.Text("Lucía Fuentes González")],
                 [sg.Text("Julen Peralta Azagra")],
                 [sg.Text("Danrui Wang")],
                 [sg.Text("Raquel Pérez López")],
                 [sg.Text("Mario Alonso Cuero")]

    ],


    layout4fin = [[sg.Exit(), sg.Button("Volver")]]

    layout4 = [[layout4ini],[layout4fin]]

    window4 = sg.Window("Sobre la aplicacion", layout4, element_justification='c')
    event, values = window4.read()

    if event in ("Exit", sg.WIN_CLOSED):
        window4.close()
    elif event == "Comenzar":
        window4.close()
        segunda_pantalla()
    if event == "Volver":
        window4.close()
        segunda_pantalla()



class GUI:
    sg.theme('DarkTeal9')
    primera_pantalla()
