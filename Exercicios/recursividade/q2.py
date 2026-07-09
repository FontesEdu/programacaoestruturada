def somar_array(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + somar_array(array[1:])

print(somar_array([2,4,6,8,10]))