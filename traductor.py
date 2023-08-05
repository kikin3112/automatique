# traductor.py - Traduce cualquier palabra o texto.

import webbrowser
from urllib.parse import quote

idiomas = {'1': 'spa',
           '2': 'eng',
           '3': 'fra',
           '4': 'por',
           '5': 'ger'
}

idioma_entrada = input('Traducir de: (ESP: 1; ING: 2; FRA: 3; POR: 4; ALE: 5) ')
idioma_salida = input('Traducir a: (ESP: 1; ING: 2; FRA: 3; POR: 4; ALE: 5) ')
de = idiomas[idioma_entrada]
a = idiomas[idioma_salida]

entrada = input('Escribe para traducir: ')
texto = quote(entrada)
#print(texto)

webbrowser.open('https://www.reverso.net/traducci%C3%B3n-texto#sl={}&tl={}&text={}'.format(de,
                                                                                           a,
                                                                                           texto))