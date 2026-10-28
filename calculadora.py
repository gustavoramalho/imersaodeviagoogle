# Calculadora Simples em Python

def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração entre dois números."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def dividir(a, b):
    """Retorna a divisão do primeiro número pelo segundo, tratando divisão por zero."""
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

def calculadora():
    print("=" * 30)
    print("      CALCULADORA SIMPLES     ")
    print("=" * 30)
    
    while True:
        print("\nEscolha a operação desejada:")
        print("1 - Soma (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")
        print("0 - Sair")
        
        opcao = input("Digite o número da operação (0 a 4): ")
        
        if opcao == "0":
            print("\nObrigado por usar a calculadora! Até logo.")
            break
            
        if opcao in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Certifique-se de digitar números válidos.")
                continue

            if opcao == "1":
                resultado = somar(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif opcao == "2":
                resultado = subtrair(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif opcao == "3":
                resultado = multiplicar(num1, num2)
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif opcao == "4":
                resultado = dividir(num1, num2)
                if isinstance(resultado, str):
                    print(resultado)
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")
        else:
            print("Opção inválida! Escolha um valor entre 0 e 4.")

# Executa o programa principal
if __name__ == "__main__":
    calculadora()
