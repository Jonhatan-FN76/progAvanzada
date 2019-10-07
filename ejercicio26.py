#ejercicio 26. unidades de tiempo 2.
#en este ejercicio usted revertira el proceso descrito en el ejercicio
#previo. desarolle un programa que comienze por leer una cantidad de
#segundos introducidos por el usuario. su programa debe desplegar la 
#cantidad equivalente en la forma de D:HH:MM:SS, donde Dson los dias,
#HH son las horas, MM son los minutos y SSson los segundos. Las horas,
#minutos y segundos deben estar en formato de 2 digitos con un 0 al 
#inicio si es necesario.

segundos_por_dia = 86400
segundos_por_hora = 3600
segundos_por_minuto = 60
segundos = 51673123

dias= segundos/segundos_por_dia
segundos= segundos % segundos_por_dia
print(dias)
print(segundos)
print(int(dias))
horas =segundos/segundos_por_hora
print(int(horas))