#ejercicio 12

di1 = int ( input ( ' Ingrese el valor de distancia 1 ' ))
ga1 = int ( input ( ' Ingrese el valor de grados 1 ' ))
di2 = int ( input ( ' Ingrese el valor de distancia 2 ' ))
ga2 = int ( input ( ' Ingrese el valor de grados 2 ' ))

g1 = matem�ticos radiales (ga1)
g2 = matem�ticos.radianes (ga2)
t1 = matem�ticos.radianes (di1)
t2 = matem�ticos.radianes (di2)

distancia =  6371.01  * math.acos (math.sin (t1) * math.sin (t2) + math.cos (t1) * math.cos (t2)
* math.cos (g1 - g2))

imprimir ( ' Distancia entre los puntos ' , distancia)