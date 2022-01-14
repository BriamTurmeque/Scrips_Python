r=int (0)
auxSalida=int (1)
p=bool(0)
q=""
s=""
guardarDatosEmpleados=" "
guardarDatosVisitantes=" "
while r<4:
    x= str (input ("Usuario: "))
    y= str (input ("Contraseña: "))
    if x=="admin" and y=="MisionTic2021":
        r=4
        p=True
    else:
        print("Credenciales incorrectas")
        r+=1
if p==True:
    while auxSalida!=0:
        if p==True:
                print ("\n------Menú de registro de personal-----")
                print ("1. Registrar ingreso de empleado.")
                print ("2. Ver empleados ingresados.")
                print ("3. Registrar ingreso de visitantes.")
                print ("4. Ver visitantes ingresados.")
                print ("\n0. Salir")
                r=int(input("\nIngresa un número válido de opción del menú: "))
                auxSalida=r
        while r>4 or r<0:
            print ("Por favor ingresa una opción válida\n")
               
            print ("------Menú de registro de personal-----")
            print ("1. Registrar ingreso de empleado.")
            print ("2. Ver empleados ingresados.")
            print ("3. Registrar ingreso de visitantes.")
            print ("4. Ver visitantes ingresados.")
            print ("\n0. Salir")
                
            r=int(input("\nIngresa un número válido de opción del menú: "))
        if r==0:
            print ("¡Hasta luego!") 
            break
        elif r==1:
            while q!="SALIR":
                q=str(input("Ingresa el nombre del empleado (Si no deseas agregar más, oprime la tecla SALIR): "))
                if q=="SALIR":
                    break
                else:
                    guardarDatosEmpleados+=q+","
        elif r==2:
                print("Los empleados registrados son:"+guardarDatosEmpleados)
                guardarDatosEmpleados=" "
                q="continuar"
        elif r==3:
                while s!="SALIR":
                    s=str(input("Ingresa el nombre del visitante (Si no deseas agregar más, digite SALIR): "))
                    if s=="SALIR":
                        break
                    else:
                        guardarDatosVisitantes+=s+","
        elif r==4:
            print("Los visitantes registrados son:"+guardarDatosVisitantes)
            guardarDatosVisitantes=" "
            s="continuar"
else :
    print ("Has agotado la cantidad de intentos, por favor inicie de nuevo el programa")