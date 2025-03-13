jugador1 = '¿Hola Jugador 1 qué elegís, piedra, papel , tijera?'
jugador2 = '¿Hola Jugador 2 qué elegís, piedra, papel , tijera?'

condicion1 = jugador1 == 'piedra' and jugador2 == 'papel'
condicion2 = jugador1 == 'papel' and jugador2 == 'piedra'
condicion3 = jugador1 == 'tijera' and jugador2 == 'papel'

if jugador1 == jugador2:
    print('Empate')
elif condicion1 or condicion2 or condicion3:
    print('Ganó el jugador 1')
else:
    print('Ganó el jugador 2')