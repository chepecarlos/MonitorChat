#!/usr/bin/env pytho3
import PySimpleGUI as sg

cprint = sg.cprint

LineaSuper = '-super-'
LineaMiembro = '-mienbro-'
LineaNormal = '-nomral-'
LineaDepurar = '-depurar-'

layout = [
            [sg.Text('ID Striming Youtube:'), sg.InputText(key='-youtube-', size=(20, 1)), sg.Button('Conectar'), sg.Text('Estado ??', key='-estado-')],
            [sg.Text('Chat SuperChat')],
            [sg.Multiline('Esperando...\n', size=(60, 5), key=LineaSuper)],
            [sg.Text('Chat Miembro')],
            [sg.Multiline('Esperando...\n', size=(60, 5), key=LineaMiembro)],
            [sg.Text('Chat Normal')],
            [sg.Multiline('Esperando...\n', size=(60, 20), key=LineaNormal)],
            [sg.Text('Chat de Youtube')],
            [sg.Text('Ingrese el ID:'), sg.InputText(key='-ID-')],
            [
                sg.Button('Enviar1'),
                sg.Button('Enviar2'),
                sg.Button('Enviar3'),
                sg.Button('Salir')
            ],
          ]

window = sg.Window('MonitorChat de ALSW', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        print("Saliendo de APP")
        break
    elif event == 'Enviar1':
        print('ID', values['-ID-'])
        cprint(values['-ID-'], key=LineaSuper)
    elif event == 'Enviar2':
        print('ID', values['-ID-'])
        cprint(values['-ID-'], key=LineaMiembro)
    elif event == 'Enviar3':
        print('ID', values['-ID-'])
        cprint(values['-ID-'], key=LineaNormal)
    elif event == 'Conectar':
        print('ID', values['-youtube-'])
        cprint(values['-youtube-'])
    # print(event)

window.close()
