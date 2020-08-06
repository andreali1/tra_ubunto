print ("calculadora basica ")
print("ingrese el numero de operacion que desea realizar ")
print("opc 1 .-sumar ")
print("opc 2 .-restar ")
print("opc 3 .-dividir ")
print("opc 4 .-multiplicar ")
a = int (input("operacion ---> "))
b = int (input("ingrese el primer valor"))
c = int (input("ingrese el segundo valor"))
if a == 1:
	d = b + c
	print("el resultado de la suma es -->  ",d)
elif a == 2 :
	d = b - c
	print("el resulñtado de la resta es --> ",d) 
elif a == 4 :
	d = b * c
	d = int(d)
	print("el resultado de la multiplicacion es --> ", d)
elif a == 3 :
	d = b / c 
	print("el resultado de la division es ---> ", d )
else:
	print("el numeor de operacion ingresada no exixte")


