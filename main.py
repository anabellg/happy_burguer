from clientes import cclientes
from menu import menu
from pedidos import pedidos
class Aplicacion:
       def __init__(self):
        self.iniciarApp()
       
       def iniciarApp(self):
              
              seleccion=""
              #Muestra el menu principal 
              while seleccion!="4":
                           print("Menú del inventario")
                           print(""" 
                                 1.- Pedidos
                                 2.- Clientes
                                 3.- Menu
                                 4.- Salir""")
                           seleccion=input()
                           if seleccion=="1":
                                    #manda llamar el siguiente menu de la opcion seleccionada (pedidos)
                                    print("Seleccionaste la Opcion Pedidos")
                                    pedidos.menu_pedido(self)
                           elif seleccion=="2":
                                     #manda llamar el siguiente menu de la opcion seleccionada (clientes)
                                    print("Seleccionaste la Opcion Clientes")
                                    cclientes.menu_clientes(self)
                                    
                           elif seleccion=="3":
                                    #manda llamar el siguiente menu de la opcion seleccionada (menu)
                                   print("Seleccionaste la Opcion Menu")
                                   menu.menu_productos(self)
                           elif seleccion =="4":
                                   print("Gracias por visitarnos")
                           else:
                                   print("Seleccion Invalida, intentalo de nuevo")
#Inicia aplicacion
Burguer = Aplicacion()
        