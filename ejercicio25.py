#ejercicio 25. unidades de tiempo 1
#crear un programa que le pida al usuario la duracion en dias,
#horas, minutos y segundos. calcular y desplegar la cantidad total
#de segundos de duracion.

DD= float (input('insertar dias'))
HH= float (input('insertar horas'))
MM= float (input('insertar minutos'))
SS= float (input('insertar segundos'))

dias = DD*86400
horas = HH*3600
minutos = MM*60
segundos = SS

Total= dias+horas+minutos+segundos
print('segundos totales:', Total)