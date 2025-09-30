# esse vai importar o desafio 9
import desafio9

def main():
    # criar um menu para o usuário escolher a operação
    print("Calculadora Estatística")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    opcao = int(input("Digite a opção desejada (1-4): "))
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    if opcao == 1:
        resultado = desafio9.somar(num1, num2)
        operacao = "Soma"
    elif opcao == 2:
        resultado = desafio9.subtrair(num1, num2)
        operacao = "Subtração"
    elif opcao == 3:
        resultado = desafio9.multiplicar(num1, num2)
        operacao = "Multiplicação"
    elif opcao == 4:
        resultado = desafio9.dividir(num1, num2)
        operacao = "Divisão"
    else:
        resultado = "Opção inválida"
        operacao = "Invalida"
    print(f"{operacao} de {num1} e {num2} é: {resultado}")

# if main como função principal
if __name__ == "__main__":
    main()