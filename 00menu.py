import os
from Lista import Listita
from Pilas import Pilitas
from Colas import Colitas


class Menu_cc:
    def __init__(self,titulo,opciones=[]):
        self.titulo=titulo
        self.opciones=opciones

    def menu(self):
        print(self.titulo)
        for opcion in self.opciones:
            print(opcion)
        while True:
            try:
                opc = input("Por favor, escoja cualquiera de las opciones [1....{}]: ".format(len(self.opciones)))
                break
            except ValueError:
                print("ERROR! Por favor, ingresa una opción correcta")
        return opc
opc = ""
while True:
    try:
        print(" ")
        print(" ")
        tamaniox = int(input("Por favor, ingrese el tamaño que tendrá 'lista, pila y cola': "))
        break
    except ValueError:
        print("ERROR! Haz ingresado un dato incorrecto. Por favor, vuelve a intentarlo.")
pila_menu= Pilitas(tamaniox)
lista_menu = Listita(tamaniox)
cola_menu = Colitas(tamaniox)
while opc != "4":
    os.system("cls")
    menu1 = Menu_cc("       *** MENÚ ***        ",["1) LISTAS", "2) PILAS", "3) COLAS", "4) SALIR"])
    opc = menu1.menu()
    if opc == "1":
        opcion1 =""
        while opcion1 != "8":
            os.system("cls")
            menu1 = Menu_cc("       *** LISTAS ***      ", ["1) INGRESAR", "2) OBTENER", "3) PRESENTA DATO ELIMINADO", "4) BUSCAR EN LISTA", 
                "5) INGRESA NUEVOS VALORES A LA LISTA YA EXISTENTE", "6) ELIMINA VALORES" , "7) MOSTRAR LISTA", "8) SALIR"])
            opcion1 = menu1.menu()
            if opcion1 == "1":
                os.system("cls")
                print("     AGREGAR VALORES A LA LISTA")
                print(" "*10)
                for i in range(tamaniox):
                    dato = int(input("Por favor, ingrese un número para agregarlo a su lista: "))
                    lista_menu.append(dato)
                    print("Dato ingresado correctamente!")
                    print(" "*10)
                input("Presiona una tecla para continuar...")
                
            elif opcion1 == "2":
                os.system("cls")
                print("     OBTENER EL VALOR DENTRO DE LA LISTA MEDIANTE SU POSICIÓN")
                print(" "*10)
                pos =int(input("INGRESE LA POSICIÓN DEL VALOR: "))
                print(lista_menu.obtener(pos))
                print(" "*10)
                input("Presiona una tecla para continuar...")
                
            elif opcion1 == "3":
                os.system("cls")
                print("     PRESENTA UN VALOR ELIMINADO A UN LADO DE LA LISTA")
                print(" "*10)
                pos = int(input("INGRESE LA POSICIÓN DEL VALOR: "))
                lista_menu.presentareliminado(pos)
                input("Presiona una tecla para continuar...")
                
            elif opcion1== "4":
                os.system("cls")
                print("     RETORNAR LA POSICIÓN DE UN ELEMENTO EN LA LISTA")
                print(" "*10)
                pos = int(input("INGRESE EL ELEMENTO PARA  SABER SU POSICIÓN: "))
                print(lista_menu.buscar_valor(pos))
                input("Presiona una tecla para continuar...")
                                
            elif opcion1 == "5":
                os.system("cls")
                print("     AGREGA NUEVOS ELEMENTOS EN LA LISTA")
                print(" "*10)
                dato = int(input("INGRESE UN VALOR NUEVO PARA PODER AÑADIRLO A LA LISTA:  "))
                print(lista_menu.adiciona_v(dato))
                input("Presione cualquier tecla para continuar...")
                
            elif opcion1 == "6":
                os.system("cls")
                print("     ELIMINA DATOS EXISTENTES EN LA LISTA")
                print(" "*10)
                dato = int(input("INGRESE EL ELEMNTO DE LA LISTA QUE DESEA ELIMINAR: "))
                print(lista_menu.eliminar(dato))
                input("Presione cualquier tecla para continuar...")
                
            elif opcion1 == "7":
                os.system("cls")
                print("     MOSTRAR LISTA")
                print(" "*10)
                lista_menu.mostrar()
                input("Presione cualquier tecla para continuar...")
                
            elif opcion1 == "8":
                print("Regresando al menú principal...")
                input("Presione cualquier tecla para continuar...")
            else:
                print("ERROR! No valido.")
                input("Presione cualquier tecla para continuar...")
                
    elif opc == "2":
        opc2 =""
        while opc2 != "6":
            os.system("cls")
            men2 = Menu_cc("        *** PILAS ***       ",["1)PUSH","2)POP","3)SHOW","4)LONGITUD DE LISTA","5)EMPTY","6)SALIR"])
            opc2 = men2.menu()
            
            if opc2 =="1":
                os.system("cls")
                print("     INGRESAR NÚMEROS A LA PILA")
                print(" "*10)
                for i in range(tamaniox):
                    while True:
                        try:
                            dato = int(input("INGRESE LOS NÚMEROS PARA AGREGARLOS A LA PILA:  "))
                            break
                        except ValueError:
                            print("ERROR! El dato ingresado no es correcto. Por favor, intente otra vez...")
                    pila_menu.push(dato)
                    print("LOS DATOS FUERON INGRESADOS DE MANERA CORRECTA.")
                input("Presione cualquier tecla para continuar...")
            elif opc2 == "2":
                os.system("cls")
                print("     ELIMINA EL ULTIMO DIGITO DE LA PILA")
                print(" "*10)
                while True:
                    try:
                        x = int(input("INGRESE LA CANTIDAD DE ELEMNTOS QUE DESEA ELIMINAR: "))
                        break
                    except ValueError:
                        print("ERROR! la cantidad ingresada no es correcta. Por favor, intente otra vez...")
                if x <= tamaniox:
                    for i in range(x):
                        print("USTED HA ELIMINADO: {}".format(pila_menu.pop()))
                    input("Presione cualquier tecla para continuar...")
                else:
                    print("ERROR! El número ingresado es mayor al tamaño de la pila...")
                    input("Presione cualquier tecla para continuar...")
            
            elif opc2 =="3":
                os.system("cls")
                print("     PRESENTA LOS VALORES DE LA PILA")
                print(" "*10)
                pila_menu.show()
                input("Presione cualquier tecla para continuar...")            
            elif opc2 == "4":
                os.system("cls")
                print("     LONGITUD DE LA PILA")
                print(" "*10)
                print("SU LONGITUD ES: {}".format(pila_menu.longitud()))
                input("Da click para continuar")           
            elif opc2 =="5":
                os.system("cls")
                print("     MOSTRAR SI LA PILA SE ENCUENTRA VACÍA O NO")
                print(" "*10)
                print("Se presentará FALSE si la pila se encuentra llena y TRUE si esta se encuentra vacia")
                print(" {} ".format(pila_menu.empty()))
                input("Presione cualquier tecla para continuar...")
            elif opc2 =="6":
                print("regresando al menú principal...")
                input("Presione cualquier tecla para continuar...")
            else:
                print("ERROR! No valido.")
                input("Presione cualquier tecla para continuar...")
    
    elif opc == "3":
        opc3 = ""
        while opc3 != "6":
            os.system("cls")
            men3 = Menu_cc("        *** COLA ***        ", ["1) INGRESAR", "2) ELIMINAR", "3) MOSTRAR", "4) LONGITUD", "5) EMPTY", "6) SALIR"])
            opc3 = men3.menu()
            if opc3 == "1":
                os.system("cls")
                print("     INGRESAR ELEMENTOS A LA COLA")
                print(" "*10)
                for i in range(tamaniox):
                    dato = int(input("INGRESE EL VALOR QUE DESEA AGREGAR EN LA COLA: "))
                    cola_menu.insentar(dato)
                    print("EL VALOR FUE INGRESADO CORRECTAMENTE")
                    print(" "*10)
                input("Presione cualquier tecla para continuar...")
            elif opc3 == "2":
                os.system("cls")
                print("     SACAR EL PRIMER VALOR DE LA COLA")
                print(" "*10)
                x = int(input("INGRESE LA CANTIDAD DE ELEMENTOS QUE DESEA ELIMINAR DE LA COLA "))
                if x <= tamaniox:
                    for i in range(x):
                        print("SE HA ELIMINADO: {}".format(cola_menu.quitar()))
                    input("Presione cualquier tecla para continuar...")
                else:
                    print("ERROR! La cantidad ingresada es mayor al tamaño de la cola...")
                    input("Presione cualquier tecla para continuar...")
            elif opc3 == "3":
                os.system("cls")
                print("     MOSTRAR LOS ELEMENTOS DE LA COLA")
                print(" "*10)
                cola_menu.mostrar()
                input("Presione cualquier tecla para continuar...")
            elif opc3 == "4":
                os.system("cls")
                print("     LONGITUD DE LA COLA")
                print(" "*10)
                print("LA LINGITUD ES: {}".format(cola_menu.longitud()))
                input("Presione cualquier tecla para continuar...")
            elif opc3 == "5":
                os.system("cls")
                print("     MOSTRAR SI LA COLA SE ENCUENTRA VACÍA O NO")
                print(" "*10)
                print("Se presentará FALSE si la cola se encuentra llena y TRUE si esta se encuentra vacia")
                print("{}".format(cola_menu.empty()))
                input("Presione cualquier tecla para continuar...")
            elif opc3 == "6":
                print("     Regresando al menú principal...")
                print(" "*10)
                input("Presione cualquier tecla para continuar...")
            else:
                print("no valida")
                input("Da click para continuar")
    elif opc == "4":
        print(" ")
        print("Saliendo...")
        print(" ")
        print ("HASTALAA PROCSIMmMaAAAaaa...")
        print(" ")
    else:
        print("Error! No valido.")
        input("Presione cualquier tecla para continuar...")        