uno = int(input('Introduce el primer numero:'))
dos = int(input('Introduce el segundo numero:'))
tres = int(input('Introduce el tercer numero:'))

menor = min(uno, dos, tres)
mayor = max(uno, dos, tres)
medio = (uno+dos+tres) - menor - mayor

print("\n El orden de menor a mayor es: " ,menor, ',', medio, ',', mayor)
