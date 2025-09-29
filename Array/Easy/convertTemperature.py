def convertTemperature(celsius):
    res = []

    kelvin = celsius + 273.15
    res.append(kelvin)

    fahrenheit = celsius * 1.80 + 32.00
    res.append(fahrenheit)

    return res

celsius = 36.50
print(convertTemperature(celsius))