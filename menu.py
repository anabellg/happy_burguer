from database import BaseDatos
class menu:
    def menu_productos(self):
         seleccion=""
         while seleccion!="4":
                            #Muestra el menu principal 
                           print("Menú de Productos")
                           print(""" 
                                 1.- Alta de Menu
                                 2.- Baja de Menu
                                 3.- Actualizacion
                                 4.- Salir""")
                           seleccion=input()
                           #manda llamar el siguiente menu de la opcion seleccionada (agregar producto)
                           if seleccion=="1":
                                    menu.agregar_producto(self)
                           elif seleccion=="2":
                           #manda llamar el siguiente menu de la opcion seleccionada (eliminar producto)
                                    menu.eliminar_producto(self)
                           elif seleccion=="3":
                           #manda llamar el siguiente menu de la opcion seleccionada (actualizar producto)
                                    menu.actualizar_producto(self)
                           elif seleccion =="4":
                                   print("Menu Principal")
                           else:
                                   print("Seleccion Invalida, intentalo de nuevo")
    def agregar_producto(self):
        d_menu= {'Clave':'', 'Nombre':'', 'Precio': 0}

        try:
            conexion = BaseDatos.abrirConexion()
            cursor = conexion.cursor()
             #guarda en diccionario los valores ingresados por el usuario 
            d_menu['Clave']  = (input("Introduce la clave del producto: \n"))
            d_menu['Nombre'] = (input("Introduce el nombre del producto: \n"))
            d_menu['Precio'] = float(input("Introduce el precio: \n"))
            productos = (d_menu['Clave'],d_menu['Nombre'],d_menu['Precio'])
            #Guarda en la base de datos los valores capturados
            sql = '''INSERT INTO menu(clave,nombre,precio)
                    VALUES(?,?,?)'''
            cursor.execute(sql,productos)
            conexion.commit()
            print("Datos guardados correctamente")
            print("------------------------------------")
        except Exception as e:
            print('Error al intentar insertar los datos: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    #Define funcion para eliminar un producto
    def eliminar_producto(self):
        try: 
             #Realiza la conexion a la base de datos
             conexion = BaseDatos.abrirConexion()
             cursor = conexion.cursor()
             cursor.execute("SELECT * FROM menu")     
             productos = cursor.fetchall()

             if len(productos) > 0:
                  menu.mostrarProductos(self)
                  print("------------------------------------")
                  clave_producto = (input("Introduce la clave del Producto: \n"))
                  #Busca todas las coincidencias del producto ingresado
                  busca_producto = cursor.execute("SELECT * FROM menu WHERE clave= ?", (clave_producto,))
                  #ejecuta funcion para eliminar el producto por clave seleccionada
                  if len(busca_producto.fetchall()) == 1:
                       #Eliminar el registro en la base de datos
                       sql = ''' DELETE FROM menu WHERE clave = ? '''
                       cursor.execute(sql,(clave_producto,))
                       conexion.commit()
                       print("Registro eliminado correctamente")
                       print("------------------------------------")
                  else:
                       print("No existen registros con esa clave")
                       print("------------------------------------")
             else:
                  print("No hay Productos para eliminar")
                  print("------------------------------------")

        except Exception as e:
             print('Error al intentar eliminar el registro: {}'.format(e))
        finally:
            if conexion:
                cursor.close()
                conexion.close()
    #Definicion para listar los productos que se encuentra en la base de datos.
    def mostrarProductos(self):
          try:
               conexion = BaseDatos.abrirConexion()
               cursor = conexion.cursor()
               cursor.execute("SELECT * FROM menu")
               productos = cursor.fetchall()
               #Si encuentra registros lista
               if len(productos) > 0:
                    print("Lista de Productos: ")
                    print("------------------------------------")
                    for clave,nombre,precio in productos:
                         print('clave: {}, nombre: {}, precio: {}'
                               .format(clave, nombre, precio))
                         print("------------------------------------")
               #Si no encuentra coincidencias envia siguiente mensaje
               else:
                    print("No hay Productos que mostrar")
                    print("------------------------------------")

          except Exception as e:
                   cursor.close()
                   conexion.close()

     #Definicion para actualizar o modificar datos de registros que se encuentran en la base de datos
    def actualizar_producto(self):
         try:
             conexion = BaseDatos.abrirConexion()
             cursor = conexion.cursor()
             cursor.execute("SELECT * FROM menu")     
             productos = cursor.fetchall()
             #Busca todos los productos que se encuentran registrados
             if len(productos) > 0:
                  menu.mostrarProductos(self)
                  print("------------------------------------")
                  clave_producto = (input("Introduce la clave del producto: \n"))
                  #Busca coincidencias de productos por clave seleccionada
                  encuentra_producto = cursor.execute("SELECT * FROM menu WHERE clave= ?", (clave_producto,))   
                  producto= encuentra_producto.fetchone()
                  #Permiter introducir los datos a actualizar
                  if producto:
                     nombre = (input("Introduce el Producto: \n"))
                     precio = (input("Introduce el precio del producto: \n"))
                     sql = ''' UPDATE menu SET nombre = ?, precio = ? WHERE clave = ? '''
                     datos_producto = (nombre,precio,clave_producto)
                     cursor.execute(sql,datos_producto)
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