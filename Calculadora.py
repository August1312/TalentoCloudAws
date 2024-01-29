

def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        if num2 == 0:
           return print("Nenhum número pode ser dividido por zero")
        else:
            return num1 / num2
    else:
        print("Numero de operação não encontrado no sitema tente outro numero ")
        return  None
    

while True:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = int(input("Escolha a operação (1: Soma, 2: Subtração, 3: Multiplicação, 4: Divisão): "))
    
    resultado = calculadora(num1, num2, operacao)
    if resultado is not None:
        print(f"Resultado: {resultado}")
    
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break