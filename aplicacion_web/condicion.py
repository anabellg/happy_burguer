# from flask import Flask, render_template


# app_web = Flask(__name__, template_folder='templates',static_folder='static')

# class condicion:
#    @app_web.route('/seleccion/<id>')
#    def seleccionar(id):
#     if id=="Pedidos":
#          titulo_pagina = "HAPPY BURGUER"
#          subtitulo_pagina = "PEDIDOS"
#          return render_template("pedidos.html",
#                                titulo_pagina = titulo_pagina,
#                                subtitulo_pagina = subtitulo_pagina,
#                                id = id)
            
#     elif id=="Clientes":
#                 print("Seleccionaste la Opcion Menu")   
#     elif id=="3":
#                 print("Seleccionaste la Opcion Menu")
#     elif id =="4":
#                 print("Gracias por visitarnos")
#     else:
#                 print("Seleccion Invalida, intentalo de nuevo")