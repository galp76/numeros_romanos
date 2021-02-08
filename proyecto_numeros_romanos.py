import time 

romanos = {'0': '', '00': '', '000': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X', '20': 'XX', '30': 'XXX', '40': 'XL', '50': 'L', '60': 'LX', '70': 'LXX', '80': 'LXXX', '90': 'XC', '100': 'C', '200': 'CC', '300': 'CCC', '400': 'CD', '500': 'D', '600': 'DC', '700': 'DCC', '800': 'DCCC', '900': 'CM', '1000': 'M'}


print('Por favor indique el numero de inicio.')
x = int(input())

print('Por favor indique el numero de fin.')
y = int(input())

for i in range(x, y+1, 10):
  for g in range(i, i+10):
    imprimir = ''
    lista_previa = []
    romanos_previa = []
    inicio = list(str(g))
    
    for j in range(len(inicio)):
      lista_previa.append(inicio[j]+'0'*(len(inicio)-j-1))
      
    for k in range(len(inicio)):
      romanos_previa.append(romanos[inicio[k]+'0'*(len(inicio)-k-1)])
      
    for m in range(len(romanos_previa)):
      imprimir = imprimir + romanos_previa[m]
      
    print(g, ' - ', imprimir)
    time.sleep(1)
  print('Presione ENTER para continuar.')
  q = input()
