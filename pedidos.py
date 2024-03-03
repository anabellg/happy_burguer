from database import BaseDatos
from ticket import genera_ticket
class pedidos:
    def menu_pedido(self):
         seleccion=""
         while seleccion!="3":
                           #Muestra menu de pedidos
                           print("Menú del pedidos")
                           print(""" 
                                 1.- Alta de Pedido
                                 2.- Cancelar Pedido
                                 3.- Salir""")
                           seleccion=input()
                           if seleccion=="1":
                                    pedidos.crear_pedido(self)
                           elif seleccion=="2":
                                    print("Seleccionaste Cancelar Pedido")
                           elif seleccion =="3":
                                   print("Menu Principal")

                           else:
                                   print("Seleccion Invalida, intentalo de nuevo")
    #Definicion para crear el pedido en la base de datos
    def crear_pedido(self):
        #Define diccionario para los pedidos
        d_pedido= {'Pedido':'', 'Cliente':'', 'Producto':'', 'Precio':0, 'Unidades':0, 'Total':0 }
        
        try: 
            #Realiza conexion a la base de datos
            conexion = BaseDatos.abrirConexion()
            cursor = conexion.cursor()
            #Pide al usuario el pedido a ingresar
            d_pedido['Pedido']  = (input("Introduce el pedido: \n"))
            #Muestra la lista de clientes que se encuentran dados de alta en la bd para seleccionar si ya existe
            nombre_cliente  = (input("Introduce el nombre del cliente: \n"))
            pedidos.mostrarListaClientes(self,nombre_cliente)
            #De la lista mostrada seleccionar la clave del cliente a utilizar para pedido
            cliente  = (input("Selecciona la clave del cliente: \n"))   
            encuentra_cliente = cursor.execute("SELECT * FROM clientes WHERE clave= ?", (cliente,))
            #Agregar a diccionario el cliente seleccionado
            var_cliente = encuentra_cliente.fetchall()
            for clientes in var_cliente:
                 d_pedido['Cliente'] = clientes[1]

            #Muestra lista de productos que se encuentran en el catalogo de la base de datos
            nom_producto =(input("Introduce el nombre del producto: \n"))
            #lista las coincidencias del producto ingresado
            pedidos.mostrarListaMenu(self,nom_producto)
            #PErmite seleccionar por clave el producto requerido para el pedido
            producto  = (input("Selecciona la clave del producto: \n"))   
            encuentra_producto = cursor.execute("SELECT * FROM menu WHERE clave= ?", (producto,))
            var_producto = encuentra_producto.fetchall()
            #Guarda producto y precio segun clave seleccionada
            for productos in var_producto:
                 d_pedido['Producto'] = productos[1]
                 d_pedido['Precio'] = float(productos[2])

            #Solicita al usuario la cantidad de unidades para el pedido
            d_pedido['Unidades'] = float(input("Cuantas unidades requieres: \n"))
            #Funcion para calcular el total a pagar 
            vcalc = lambda x,y: x * y
            d_pedido['Total'] =  (vcalc(d_pedido['Unidades'], d_pedido['Precio']))
            #Guarda pedido en la base de datos
            pedido = (d_pedido['Pedido'],d_pedido['Cliente'],d_pedido['Producto'],d_pedido['Precio'],d_pedido['Unidades'],d_pedido['Total'])
            sql = '''INSERT INTO pedidos(pedido,cliente,producto,precio,unidades,total)
                    VALUES(?,?,?,?,?,?)'''
            cursor.execute(sql,pedido)
            conexion.commit()
            print("Datos guardados correctamente")
            print("------------------------------------")
            #Genera Ticket 
            genera_ticket.crear_ticket(self,pedido)
            
        except Exception as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
     #Definicion de funcion para mostrar la lista de clientes segun coincidencia ingresada por usuario
    def mostrarListaClientes(self,vcliente):
          try: 
               #Realiza conexion a bd
               conexion = BaseDatos.abrirConexion()
               cursor = conexion.cursor()
               cursor.execute("SELECT * FROM clientes WHERE nombre like ?", (vcliente+'%',))
               clientes = cursor.fetchall()
                #Lista clientes segun coincidencia
               if len(clientes) > 0:
                    print("Lista de Clientes: ")
                    print("------------------------------------")
                    for clave,nombre,direccion,e_mail,telefono in clientes:
                         print('clave: {}, nombre: {}, direccion: {}, e_mail {}, telefono: {}'
                               .format(clave, nombre, direccion, e_mail, telefono))
                         print("------------------------------------")
               else:
                    print("No hay Clientes que mostrar")
                    print("------------------------------------")

          except Exception as e:
                   cursor.close()
                   conexion.close()
     #Define funcion para mostrar menu que se encuentra en base de datos
    def mostrarListaMenu(self,vproducto):
          try:
               conexion = BaseDatos.abrirConexion()
               cursor = conexion.cursor()
               #Ejecuta Query para buscar coincidencias en base de datos
               cursor.execute("SELECT * FROM menu WHERE nombre like ?", (vproducto+'%',))
               productos = cursor.fetchall()
               #Listra productos
               if len(productos) > 0:
                    print("Lista de Productos: ")
                    print("------------------------------------")
                    for clave,nombre,precio in productos:
                         print('clave: {}, nombre: {}, precio: {}'
                               .format(clave, nombre, precio))
                         print("------------------------------------")
               else:
                    print("No hay Productos que mostrar")
                    print("------------------------------------")

          except Exception as e:
                   cursor.close()
                   conexion.close()

    def cancelar_pedido():
        pass