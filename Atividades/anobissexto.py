ano = int(input("Informe um ano: "))

if ano > 0: 
    if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")
else: 
    print("O ano deve ser maior que zero.")

def verificar_bissexto(ano):
    return(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)