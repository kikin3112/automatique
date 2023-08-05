# enciclopedia.py - Realiza la búsqueda del término que proporcione el usuario
# vía entrada escrita.

import webbrowser

entrada = input('Escriba un término: ')
termino = entrada.split()
busqueda = '_'.join(termino)

webbrowser.open('https://es.wikipedia.org/wiki/' + busqueda)

