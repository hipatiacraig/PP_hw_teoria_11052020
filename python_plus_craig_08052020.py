# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:07:52 2020

@author: Victoria
"""

import hangman
import reversegam
import tictactoeModificado
import csv
import PySimpleGUI as sg


#MODULOS

    
def guardo_archivo (file,lista_datos):
    file=open('datos_mr_ocio.csv', 'a+')
    print('nuevos datos:', lista_datos)
    writer = csv.writer(file)
    for row in lista_datos:
        writer.writerow(row)
    file.close()     
    
def actualizar_datos (listbox,lista):
    listbox.Update(map(lambda x:"Nombre: {} - Edad: {} - Juego: {}".format(x[0],x[1], x[2]), lista))    
    
#COLOR INTERFAZ

sg.theme('DarkGrey3')    
#sg.theme('DarkAmber')    
    
#LAYOUT

layout = [  [sg.Text('Hola! Mi nombre es Mr Ocio, Mucho gusto! Cuál es su nombre?'),sg.InputText(key='nombre')],
            [sg.Text('Soy tan viejo como el mundo, usted? cuántos años tiene?'), sg.InputText(key='edad')],
            [sg.Text('Todo lo que haga quedará listado a continuación:')],
            [sg.Listbox(values= [], key='datos', size=(60, 10))],
            [sg.Text('Con qué juego se quiere deleitar el día de hoy?')],
            [sg.Button('The scary hangman'), sg.Button('The boring TicTacToe')],
            [sg.Button('Othello the dramatic'), sg.Button('Vuelvo más tarde')] ]

#WINDOW

window = sg.Window('Con algo de tiempo libre...', layout)
window.Finalize()

#ITERACION DE LLENADO
    
lista_datos=[]
while True:
    event, values = window.read()
    if event is None:
        break
    if event is 'The scary hangman':
        lista_datos.append((values['nombre'],values['edad'], "Hangman"))
        hangman.main()
        actualizar_datos(window.FindElement('datos'),lista_datos)
    if event is 'The boring TicTacToe':
        lista_datos.append((values['nombre'],values['edad'], "TicTacToe"))
        tictactoeModificado.main()
        actualizar_datos(window.FindElement('datos'),lista_datos)
    if event is 'Othello the dramatic':
        lista_datos.append((values['nombre'],values['edad'], "Othello"))
        reversegam.main()
        actualizar_datos(window.FindElement('datos'),lista_datos)
    if event is 'Vuelvo más tarde':
       guardo_archivo('datos_mr_ocio.csv', lista_datos)
       window.close()
       
