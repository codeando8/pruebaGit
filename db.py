import pymysql

class DataBase:
   

    def seleccionarCantidad(self, codigo):
        sql = 'SELECT cantidad FROM Datos_articulo WHERE Codigo_articulo={}'.format(codigo)
        cantidad = -2
        try:
            self.cursor.execute(sql)
            item = self.cursor.fetchone()
            cantidad = item[0]
        except Exception as e:
            raise 
        return cantidad
    
    def actualizarCantidad(self, codigo, cantidad):
        sql = 'UPDATE Datos_articulo SET cantidad={} where Codigo_articulo={}'.format(cantidad,codigo)
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise 
    
    def nombreProducto(self, codigo):
        sql = 'SELECT nombre FROM Datos_articulo WHERE Codigo_articulo={}'.format(codigo)
        nombre = ''
        try:
            self.cursor.execute(sql)
            item = self.cursor.fetchone()
            nombre = item[0]
        except Exception as e:
            raise 
        return nombre

    def close(self):
        self.connection.close()
