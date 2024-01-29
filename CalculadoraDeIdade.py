from datetime import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922 a 2024): "))
            if 1922 <= ano_nascimento <= 2024:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo permitido.")
        except ValueError:
            print("Por favor, digite um ano válido.")

def main():
    nome_completo = input("Digite o nome completo: ")

    ano_nascimento = obter_ano_nascimento()

    idade = calcular_idade(ano_nascimento)

    print(f"\nNome: {nome_completo}")
    print(f"Idade em 2024: {idade} anos")

if __name__ == "__main__":
    main()