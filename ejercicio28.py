aire = float(input('Introudce la temperatura del aire:'))
viento = float(input('Introduce la velocidad del viento:'))

sensacion_termica= 13.12 + (0.6215*aire) - (11.37*(viento**0.16)) + (0.3965*aire*(viento**0.16))

print('sensacion termica es ', round(sensacion_termica))