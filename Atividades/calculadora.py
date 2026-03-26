conta = input("Digite a conta a ser calculada: ")

def calcular_conta(conta):
    for i in conta:
        if i == "+":
            num1, num2 = conta.split("+")
            resultado = float(num1) + float(num2)
            return resultado
        elif i == "-":
            num1, num2 = conta.split("-")
            resultado = float(num1) - float(num2)
            return resultado
        elif i == "*":
            num1, num2 = conta.split("*")
            resultado = float(num1) * float(num2)
            return resultado
        elif i == "/":
            num1, num2 = conta.split("/")
            if float(num2) != 0:
                resultado = float(num1) / float(num2)
                return resultado
            else:
                return "Erro: Divisão por zero não é permitida."
    return "Operação inválida."

resultado = calcular_conta(conta)
print("Resultado: ", resultado)

arquivo = open("resultado.txt", "w")

# for i in conta:
    # if i == "+":
    #     num1, num2 = conta.split("+")
    #     resultado = float(num1) + float(num2)
    #     print("Resultado: ", resultado)
    #     break
    # elif i == "-":
    #     num1, num2 = conta.split("-")
    #     resultado = float(num1) - float(num2)
    #     print("Resultado: ", resultado)
    #     break
    # elif i == "*":
    #     num1, num2 = conta.split("*")
    #     resultado = float(num1) * float(num2)
    #     print("Resultado: ", resultado)
    #     break
    # elif i == "/":
    #     num1, num2 = conta.split("/")
    #     if float(num2) != 0:
    #         resultado = float(num1) / float(num2)
    #         print("Resultado: ", resultado)
    #     else:
    #         print("Erro: Divisão por zero não é permitida.")
    #     break