# traductor.py - Traduce cualquier palabra o texto en los idiomas soportados.

import webbrowser, pyperclip
from urllib.parse import quote

idiomas = {'1': 'spa',
           '2': 'fra'
}

entrada = pyperclip.paste()
texto = quote(entrada)

flow = input('[ESP ---> FRA]: 1, [FRA ---> ESP]: 2 ')

if flow == '1':
    webbrowser.open('https://www.reverso.net/traducci%C3%B3n-texto#sl={}&tl={}&text={}'.format(idiomas['1'],
                                                                                               idiomas['2'],
                                                                                               texto))
elif flow == '2':
    webbrowser.open('https://www.reverso.net/traducci%C3%B3n-texto#sl={}&tl={}&text={}'.format(idiomas['2'],
                                                                                               idiomas['1'],
                                                                                               texto))