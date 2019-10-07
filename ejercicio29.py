tem_celsius = float(input('Introduce la temperatura en celsius:'))

tem_fahrenheit = tem_celsius * (9/5) + 32
tem_kelvin = tem_celsius + 273.15

print('\n En Fahrenheit: %.2f' %(tem_fahrenheit))
print('\n En Kelvin: ',(tem_kelvin))