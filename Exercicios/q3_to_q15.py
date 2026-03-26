# print("Q3")
# print()

# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))

# print(f"{nome} \n{idade} anos")

# print()
# print("Q4")
# print()

# print("Digite dois números para realizar as operações matemáticas de soma, subtração, multiplicação e divisão: ")
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

# soma = num1 + num2
# sub = num1 - num2
# mult = num1 * num2
# div = num1 / num2

# print()
# print(f"Resultado da soma de {num1} e {num2} é: {soma}")
# print(f"Resultado da subtração de {num1} e {num2} é: {sub}")
# print(f"Resultado da multiplicação de {num1} e {num2} é: {mult}")
# print(f"Resultado da divisão de {num1} e {num2} é: {div}")

# print()
# print("Q5")
# print()

# raio = int(input("Digite o valor do raio: "))
# resultado = 3.14159 * (raio**2)
# print()
# print(f"O resultado da área do círculo com raio {raio} é: {resultado}")

# print()
# print("Q6")
# print()

# celsius = int(input("Digite o valor da temperatura em Celsius: "))
# farenheit = 32 + (celsius*1.8)
# print("")
# print(f"O valor da temperatura em Fahrenheit é: {farenheit}")

# print()
# print("Q7")
# print()

# salario_mensal = float(input("Digite o salário mensal: "))
# meses_trabalhados = int(input("Digite o número de meses: "))

# salario_anual = salario_mensal * meses_trabalhados

# with open("resultado_q7.txt", mode="w") as file:
#     file.write(f"O resultado da multiplicação de {salario_mensal} e {meses_trabalhados} é: {salario_anual}")

# print()
# print("Q8")
# print()

# num = int(input("Digite um número inteiro: "))

# if num % 2 == 0:
#     print(f"O número {num} é par.")
# else:
#     print(f"O número {num} é ímpar.")

# print()
# print("Q9")
# print()

# valor = input("Digite 1 para verdadeiro ou 0 para falso: ")
# valor2 = input("Digite 1 para verdadeiro ou 0 para falso: ")

# if valor == "1":
#     valor = True
# else:    valor = False

# if valor2 == "1":
#     valor2 = True
# else:    valor2 = False

# print()
# print(f"{valor} e {valor2} é: {valor and valor2}")
# print(f"{valor} ou {valor2} é: {valor or valor2}")
# print(f"A negação de {valor} é: {not valor}")
# print(f"A negação de {valor2} é: {not valor2}")

# print()
# print("Q10")
# print()

# from rich import print as cprint

# a = input("Digite a primeira frase: ")
# b = input("Digite a segunda frase: ")

# if a == b:
#     cprint(f"As frases [i]'{a}'[/i] e [i]'{b}'[/i] são iguais.")
# else:    cprint(f"As frases [i]'{a}'[/i] e [i]'{b}'[/i] são diferentes.")

# print()
# print("Q11")
# print()

# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))

# if num1 > num2:
#     print(f"O número {num1} é maior que o número {num2}.")
# else: print(f"O número {num1} é menor ou igual ao número {num2}.")

# with open("resultado_q11.txt", mode="w") as file:
#     file.write(f"{num1} , {num2}.")

# print()
# print("Q12")
# print()

# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Você é maior de idade.")
# else: print("Você é menor de idade.")

# print()
# print("Q13")
# print()

# num = int(input("Digite um número inteiro: "))
# num2 = int(input("Digite outro número inteiro: "))

# num1 = num
# num = num2
# num2 = num1

# print()
# print(f"O valor do primeiro número digitado é: {num}")
# print(f"O valor do segundo número digitado é: {num2}")

# print()
# print("Q14")
# print()

# velocidade = 1500
# tempo = 40
# altitude = velocidade * tempo

# print()
# print(f"A altitude do foguete é: {altitude} metros.")

# altitude_km = altitude / 1000

# print()
# print(f"A altitude do foguete é: {altitude_km} km.")

print()
print("Q15")
print()

import time
print("A data deve ser maior que primeiro de janeiro de 1970")
dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês: "))
ano = int(input("Digite um ano: "))

if ano > 1970:
    dataEPOCH = time.mktime((ano, mes, dia, 0, 0, 0, 0, 0, 0))
    print()
    print(f"A data {dia}/{mes}/{ano} em segundos desde o primeiro de janeiro de 1970 é: {dataEPOCH} segundos.")
else: print("A data deve ser maior que primeiro de janeiro de 1970.")

help(time.mktime)