# ano = int(input("Informe um ano: "))

# if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#     print(f"{ano} é um ano bissexto.")
# else:
#     print(f"{ano} não é um ano bissexto.")

def verificar_ano_bissexto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(verificar_ano_bissexto(2000))