import sqlite3
import os
class BaseDatos:
   

    def abrirConexion():
        try:
            conexion = sqlite3.connect('store.db') 
            return conexion
        except Exception as e:
            print('Error al conectar a la Base de datos: {}'.format(e))
