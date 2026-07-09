def inverter_string(palavra):
    if len(palavra) == 0:
        return palavra
    else:
        return palavra[-1] + inverter_string(palavra[:-1])

print(inverter_string("eduardo"))