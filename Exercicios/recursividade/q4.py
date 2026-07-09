def exponenciar(base, expoente):
    if expoente == 0:
        return 1
    elif expoente < 0:
        return 1 / exponenciar(base, -expoente)
    else:
        return base * exponenciar(base, expoente - 1)

print(exponenciar(4.102, 3))