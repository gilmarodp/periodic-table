﻿#!/usr/bin/python3
# :()
from menu import show_menu
from choice import get_option
import os

CLEAR_SCREEN_DOS = 'cls'
CLEAR_SCREEN_UNIX = 'clear'

def clear_screen():
	if os.name == 'nt':
		os.system(CLEAR_SCREEN_DOS)
	else:
		os.system(CLEAR_SCREEN_UNIX)
answer = None

while answer != 0:
	# TODO tratar limite por numero atomico
	# TODO ajeitar massa atomica no csv
	# TODO busca por peso mostra os elmentos mais proximos

	# TODO fazer busca por distribuição
        clear_screen()
        show_menu()
        answer = int(input('--> '))
        # TODO melhorar filtro por distribuição
        get_option(answer)
