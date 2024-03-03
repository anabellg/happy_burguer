from database import BaseDatos
class cclientes:
     def menu_clientes(self):
         seleccion=""
         #Muestra menu para la opcion seleccionada clientes
         while seleccion!="4":
                           print("Menú de clientes")
                           print(""" 
                                 1.- Alta de Clientes
                                 2.- Baja de Clientes
                                 3.- Actualizacion
                                 4.- Salir""")
                           seleccion=input()
                           if seleccion=="1":
                                    #Ejecuta funcion para agregar clientes
                                    cclientes.agregar_cliente(self)
                           elif seleccion=="2":
                                    #Ejecuta funcion para eliminar clientes
                                    cclientes.eliminar_cliente(self)
                           elif seleccion=="3":
                                    #Ejecuta funcion para actualizar clientes
                                    cclientes.actualizar_cliente(self)
                           elif seleccion =="4":
                                   print("Menu Principal")
                           else:
                                   print("Seleccion Invalida, intentalo de nuevo")
     #Definicion de funcion para agregar clientes
     def agregar_cliente(self):
        #Declaracion de diccionario para guardar datos de clientes
        d_clientes = {'Clave':'', 'Nombre':'', 'Direccion':'', 'E-mail':'', 'Telefono': ''}

        try:
            #Realiza conexion a base de datos
            conexion = BaseDatos.abrirConexion()
            cursor = conexion.cursor()
            #Solicita a usuario datos para dar de alta cliente y almacena en diccionario
            d_clientes['Clave'] = (input("Introduce la clave del cliente: \n"))
            d_clientes['Nombre'] = (input("Introduce el nombre del cliente: \n"))
            
            d_clientes['Direccion']= (input("Introduce la direccion del cliente: \n"))
            d_clientes['E-mail'] = (input("Introduce el e_mail del cliente: \n"))
            d_clientes['Telefono'] = (input("Introduce el telefono del cliente:  \n"))

            valores = (d_clientes['Clave'],d_clientes['Nombre'],d_clientes['Direccion'],d_clientes['E-mail'],d_clientes['Telefono'])
            #Guarda en base de datos valores de cliente
            sql = '''INSERT INTO clientes(clave,nombre,direccion,e_mail,telefono)
                    VALUES(?,?,?,?,?)'''

            cursor.execute(sql,valores)
            conexion.commit()
            print("Datos guardados correctamente")
            print("------------------------------------")
        except Exception as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
     #Define funcion para eliminar clientes
     def eliminar_cliente(self):
        try:
             #Realiza conexion con la base de datos
             conexion = BaseDatos.abrirConexion()
             cursor = conexion.cursor()
             cursor.execute("SELECT * FROM clientes")     
             clientes = cursor.fetchall()
             #Mostrar lista de clientes dados de alta con la coincidencia ingresada por usuario
             if len(clientes) > 0:
                  cclientes.mostrarListaClientes(self)
                  print("------------------------------------")
                  clave_cliente = (input("Introduce la clave del cliente: \n"))
                  #Realiza consulta en bd para seleccionar por clave usuario a dar de baja
                  find_cliente = cursor.execute("SELECT * FROM clientes WHERE clave= ?", (clave_cliente,))
                  if len(find_cliente.fetchall()) == 1:
                       #Ejecuta query en bd para baja de cliente
                       sql = ''' DELETE FROM clientes WHERE clave = ? '''
                       cursor.execute(sql,(clave_cliente,))
                       conexion.commit()
                       print("Registro eliminado correctamente")
                       print("------------------------------------")
                  else:
                       print("No existen registros con esa clave")
                       print("------------------------------------")
             else:
                  print("No hay Clientes para eliminar")
                  print("------------------------------------")

        except Exception as e:
             print('Error al intentar eliminar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    #Define funcion para mostrar clientes 
     def mostrarListaClientes(self):
          try:
               conexion = BaseDatos.abrirConexion()
               cursor = conexion.cursor()
               cursor.execute("SELECT * FROM clientes")
               clientes = cursor.fetchall()

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
     #Define funcion para actualizar o modificar clientes dados de alta
     def actualizar_cliente(self):
        try:
             conexion = BaseDatos.abrirConexion()
             cursor = conexion.cursor()
             cursor.execute("SELECT * FROM clientes")     
             clientes = cursor.fetchall()

             if len(clientes) > 0:
                  cclientes.mostrarListaClientes(self)
                  print("------------------------------------")
                  clave_cliente = (input("Introduce la clave del cliente: \n"))

                  find_cliente = cursor.execute("SELECT * FROM clientes WHERE clave= ?", (clave_cliente,))   
                  cliente = find_cliente.fetchone()

                  if cliente:
                     nombre = (input("Introduce el nombre del cliente: \n"))
                     direccion= (input("Introduce la direccion del cliente: \n"))
                     e_mail= (input("Introduce el e_mail del cliente: \n"))
                     telefono = (input("Introduce el telefono del cliente:  \n"))

                     sql = ''' UPDATE clientes SET nombre = ?, direccion = ?, e_mail = ?, telefono = ? WHERE clave = ? '''
                     datos_cliente = (nombre,direccion,e_mail,telefono,clave_cliente)
                     cursor.execute(sql,datos_cliente)
                     conexion.commit()
                     print("Registro modificado correctamente")
                     print("------------------------------------")
                  else:
                    print("No hay registro con esa clave")
                    print("------------------------------------")
             else:  
                print("No hay productos para modificar")
                print("------------------------------------")
            
        except Exception as e:
            print('Error al intentar modificar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()