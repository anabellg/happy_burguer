#Solo se utiliza para hacer pruebas por fuera durante el desarrollo

from database import BaseDatos
d_pedido= {'Pedido':'', 'Cliente':'', 'Producto':'', 'Precio':0}
        
try:
            conexion = BaseDatos.abrirConexion()
            cursor = conexion.cursor()
            d_pedido['Pedido']  = (input("Introduce el pedido: \n"))
            # d_pedido['Cliente'] = (input("Introduce el nombre del cliente: \n"))
            nombre_cliente  = (input("Introduce el nombre del cliente: \n"))
            cliente  = (input("Selecciona la clave del cliente: \n"))   
            encuentra_cliente = cursor.execute("SELECT * FROM clientes WHERE clave= ?", (cliente,))
            var_cliente = encuentra_cliente.fetchall()
            for nombre in var_cliente:
                    print(nombre[1])
          #        d_pedido['Cliente'] = nombre
          #   d_pedido['Producto'] = (input("Introduce el nombre del producto: \n"))
          #   d_pedido['Precio'] = float(input("Introduce el precio: \n"))

          #   pedido = (d_pedido['Pedido'],d_pedido['Cliente'],d_pedido['Producto'],d_pedido['Precio'])

          #   sql = '''INSERT INTO pedidos(pedido,cliente,producto,precio)
          #           VALUES(?,?,?,?)'''
          #   cursor.execute(sql,pedido)
          #   conexion.commit()
          #   print("Datos guardados correctamente")
          #   print("------------------------------------")
except Exception as e:
            print('Error al intentar insertar los datos: {}'.format(e))
finally:
            if conexion:
                cursor.close()
                conexion.close()