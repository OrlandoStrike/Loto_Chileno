#El Loto se basa en acertar 6 números del 1 al 41
import random
import time
import sys
numlet = [' el Primer ',' el Segundo ',' el Tercer ',' el Cuarto ',' el Quinto ', ' y el Sexto ']
numt = ['Primera','Segunda','Tercera','Cuarta','Quinta','Sexta']
boljug = []
bolgan = []
aci = []
for i in range (0,6):
    nx = input('Elija'+numlet[i]+'numero: ')
    nx = int(nx)
    while nx>41 or nx<=0 or boljug.count(nx)>0:
        print('Su numero debe ser entre 1 y 41, ademas no puede repetirse...')
        nx = input('Elija' + numlet[i] + 'numero: ')
        nx = int(nx)
    else:
        pass
    boljug.append(nx)
boljug = sorted(boljug)
print('Boleto jugado cerrado y sellado!!!(no hay devoluciones)\n')
time.sleep(0.5)
print('A sortear las bolitas!!!')
time.sleep(0.2)
for i in range (0,6):
    winnum = random.randint(1, 41)
    while bolgan.count(winnum)>0:
        winnum = random.randint(1, 41)
    bolgan.append(winnum)
    sys.stdout.write(numt[i]+' bolita ganadora es la')
    time.sleep(0.2)
    sys.stdout.write('.')
    time.sleep(0.2)
    sys.stdout.write('.')
    time.sleep(0.2)
    sys.stdout.write('. ')
    time.sleep(0.2)
    print('¡►',winnum,'◄!')
bolgan = sorted(bolgan)
for i in range (0,6):
    if boljug[i] in bolgan:
        aci.append(boljug[i])
    else:
        pass
time.sleep(0.2)
#print('El boleto sorteado es: ')
#print(bolgan)
#time.sleep(0.5)
print('\nTu jugaste el boleto: ')
time.sleep(0.2)
print('¡►',boljug,'◄!')
time.sleep(0.5)
sys.stdout.write('\nCalculando tus aciertos a traves de la IA de loteria,\nalimentada por "Washin Learnin"* (patente pendiente*)\n')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.2)
sys.stdout.write('.')
time.sleep(0.15)
sys.stdout.write('.')
time.sleep(0.15)
sys.stdout.write('.')
time.sleep(0.15)
sys.stdout.write('.')
time.sleep(0.15)
sys.stdout.write('.')
time.sleep(0.1)
sys.stdout.write('.')
time.sleep(0.1)
sys.stdout.write('.')
time.sleep(0.1)
sys.stdout.write('.')
time.sleep(0.1)
sys.stdout.write('.')
time.sleep(0.1)
sys.stdout.write('.')
time.sleep(0.1)
sys.stdout.write('.')
nacs = 0
for i in range (0,6):
    if boljug[i] in bolgan:
        nacs = nacs + 1
    else:
        pass
if nacs == 0:
    time.sleep(0.5)
    print('\nNo le achuntate a ninguno pirilonji...\nmas suerte pa la prox locowom')
else:
    print('\nLe achuntaste al: ')
    time.sleep(0.5)
    print(aci)
    nach = str(len(aci))
    time.sleep(0.5)
    print('Terrile suertuo, le achuntate a ' + nach +' numeros\nte ganaste la terrible pulenta croqueta,\nperro bomba!')