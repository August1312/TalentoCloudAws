lista_frutas = []

while True:
    fruta = input('Digite a fruta para adicionar à lista ou digite "exit" para sair: ')
    
    if fruta.lower() == 'exit':
        break

    lista_frutas.append(fruta)
    lista_frutas.sort()
    print(f'Sua lista de frutas é {lista_frutas}')

print(f'Sua lista de frutas final é {lista_frutas}')
