interes=0.04
deposito=float(input('Ingrese la cantidad a depositar en el año:$'))
ano1=deposito*interes
ano1T=ano1+deposito
print('El total en su cuenta en este año es:$%.2f' %ano1T)
ano2=ano1T*interes
ano2T=ano1T+ano2
print('El total en su cuenta en este año es:$%.2f' %ano2T)
ano3=ano2T*interes
ano3T=ano2T+ano3
print('El total en su cuenta en este año es:$%.2f' %ano3T)