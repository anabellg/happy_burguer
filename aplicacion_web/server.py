from flask import Flask, render_template


app_web = Flask(__name__, template_folder='templates',static_folder='static')

#Index principal/Muestr menu principal
@app_web.route('/')
def burger_happy():
    titulo_pagina = "HAPPY BURGUER"
    subtitulo_pagina = "BIENVENIDO"
    menu={
        '1': 'Pedidos',
        '2': 'Clientes',
        '3': 'Menu',
        '4': 'Salir'
        }    #Se pasan variable a traves de la funcion render_template
    return render_template("index.html",
                           titulo_pagina = titulo_pagina,
                           subtitulo_pagina = subtitulo_pagina,
                           menu = menu)
#Muestra opciones para opcion seleccionada menu
@app_web.route('/seleccion/<id>')
def seleccionar(id):
   
    if id=="Menu":
         titulo_pagina = "HAPPY BURGUER"
         subtitulo_pagina = "MENU"
         menu_ped={
        '1': 'Alta de Menu',
        '2': 'Baja de Menu',
        '3': 'Actualizacion',
        '4': 'Salir'
        } 
         return render_template("menu.html",
                               titulo_pagina = titulo_pagina,
                               subtitulo_pagina = subtitulo_pagina,
                               menu_ped = menu_ped)
    
    



# @app_web.route('/hola')
# def hola_mundo():
#     return 'Hola mundo'