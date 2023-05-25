import time
import math
n1 = float(input('Digite um número: '))
n2 = 'Analisando'
n3 = 'Fim'
time.sleep(1)
print('{:=^50}' .format(n2))
time.sleep(1)
print(' O dobro de {:.2f} é {:.2f}' .format(n1, n1 + n1))
time.sleep(1)
print(' O triplo de {:.2f}  é {:.2f}' .format(n1, n1*3))
time.sleep(1)
print(' A raiz quadrada de {:.2f} é {:.2f}' .format(n1, math.sqrt(n1)))
time.sleep(1)
print('{:=^50}' .format(n3))
