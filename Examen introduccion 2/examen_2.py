from math import comb
from pickle import TRUE

veces=0
menu=TRUE
while veces<3:
        nombre="majo"
        contraseña="super"
        print("Digite el nombre de usuario:")
        usuario=input()
        usuario=usuario.lower()
        print("Digite la contraseña:")
        contraseña=input()
        if usuario == nombre and contraseña=="super":
            
            saldo=0
            deposito=0
            menu=True
            while menu==True:    
                print("\t Menu")
                print("1. Depositar dinero a la cuenta")
                print("2. Sacar dinero de la cuenta")
                print("3. Ver saldo")
                print("4.Salir")
                opcion=True
                while opcion == True:
                    print("Digite una opcion en numero")
                    opcion=int(input())
                    if opcion == 1:
                            print("Cuanto dinero desea depositar") 
                            deposito=input()
                            if (deposito.isnumeric()):
                                deposito=float(deposito)
                                if deposito%1000 == 0:
                                    saldo=(saldo + deposito)
                                    print("Usted realizo un deposito de:",deposito)
                                    print("Su saldo actual es de:",saldo)
                                else:
                                    print("Error.Debe ser multiplo de 1000")
                            else:
                                print("Error,solo se pueden ingresar numeros \nVuelva a intentarlo desde el menu" )

                            opcion=False
                    elif opcion == 2:
                        print("Cuanto dinero desea usted retirar")
                        retiro=float(input())
                        if retiro%1000 == 0:
                            if retiro <= saldo:
                                saldo=(saldo-retiro)
                                print("Usted realizo un retiro de:",retiro)
                                print("Su saldo actual es de:",saldo)
                            elif retiro > saldo:
                                print("No se puede realizar la transacción")
                            opcion=False
                        else:
                            print("Error.Debe ser multiplo de 1000")
                    elif opcion == 3:
                        print("Su saldo actual es de:",saldo)
                        opcion=False
                    elif opcion == 4:
                        print("Gracias por utilizar nuestros servicios \nVuelva pronto ")
                        opcion=False
                        menu=False
                    else:
                        print("Error.Vuelva a intentarlo")
                        opcion=True

        else:
            veces=veces+1
            print("Usuario o contraseña incorrecta,vuelva a intentalo")

        if menu == False:
            break
if (veces <= 3):
    print("Acceso bloqueado")    

