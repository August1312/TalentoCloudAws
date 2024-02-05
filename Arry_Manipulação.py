
lista_teste = []
max_lista = 50
i = 1

# Sem o ranger
while len(lista_teste) < max_lista:
    lista_teste.append(i)
    i += 1
    
for j in range(25):
    lista_teste.pop(j)

print(f'\t {j}')    
print(lista_teste)
print(len(lista_teste))
