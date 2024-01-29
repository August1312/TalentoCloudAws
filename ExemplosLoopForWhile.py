for i in range(1, 10 +1 ):
    if i % 2 == 0:
        print(f"{i} e um numero par")
    else:
       print(f"{i} numero impar")
    
    
import random 

while True:
    numero = random.randint(1, 10)
    print(numero)
    
    if numero == 5:
        break
    
import time 

tempoInicial = 1
tempoFinal = 45
print("Iniciando descanso....")
for i in range(tempoInicial, tempoFinal +1):
   print(i)
   time.sleep(1)
print("Fim do descanso!")