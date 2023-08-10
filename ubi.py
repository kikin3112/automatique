# ubi.py - Abre la ubicación en el mapa de la direccion que proporcione
# el usuario vía comando o texto en el portapapeles.

import webbrowser, pyperclip, sys

if len(sys.argv) > 1:
    #Correr el script con comandos
    direccion = ' '.join(sys.argv[1:])
else:
    #Correr el script con portapapeles
    direccion = pyperclip.paste().replace('#', ',')

ciudad = 'Cali' #input('Ingrese la ciudad: ')
departamento = 'Valle' #input('Ingrese el departamento: ')
pais = 'Colombia' #input('Ingrese el país: ')

webbrowser.open('https://www.google.com/maps/place/' + direccion + ', {}, {}, {}'.format(ciudad,
                                                                                         departamento,
                                                                                         pais))
