# programa para identificar si un numero que digite el usuario 
# es par o es impar, siempre y cuando sea positivo


# primero vamos a comprobar que sea un numero mayor o igual a 0.
a = False
num = int(input("Digite un numero mayor a 0: "))
while a == False :
    if num > 0:
        a = True
    else:
        print("El numero es invalido.")
        num = int (input("digite otro numero: "))

# verificacion de que si el numero es par o impar
print("-----------------")
if (num % 2) == 0:
     print ("El numero " + str(num) + " es par")
else:
    print ("El numero " + str(num) + " es impar")
print("-----------------")