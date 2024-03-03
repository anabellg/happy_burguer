class genera_ticket:
      #Funcion para generar ticket del pedido realizado
      def crear_ticket(self,pedido):
            f = open('ticket.txt', 'w')
            f.write('HAPPY BURGUER \n')
            f.write("Pedido No. :" +str(pedido[0]) +'\n')
            f.write("Cliente.: "  +str(pedido[1]) +'\n')
            f.write("Producto: " +str(pedido[2]) +'\n')
            f.write("Precio: " +str(pedido[3]) +'\n')
            f.write("Unidades: " +str(pedido[4]) +'\n')
            f.write('-----------------------------\n')
            f.write("Total: " +str(pedido[5]) +'\n')
            f.write('-----------------------------\n')
            f.write('GRACIAS POR SU COMPRA\n')
            f.write('REGRESE PRONTO\n')

           
            print('Ticket Generado correctamente')
            f.close()