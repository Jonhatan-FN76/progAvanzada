KPal= float(input('Introduce la presion en kilo-pascales: '))

PSI = KPal* 0.145037738
mercurio = KPal* 7.50062
atm = KPal / 101.3

print('\n En Libras por pulgada^2: %.3f'%(PSI),'(PSI)')
print('\n En Millimetros de Mercury: %.3f'%(mercurio),'(mmHg)')
print('\n En Atmosferas: %.3f'%(atm),'(atm)')