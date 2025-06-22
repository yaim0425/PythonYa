# ---------------------------------------------------------
# Descripción
# ---------------------------------------------------------
# Esta clase se usa como intermedio con la basa de datos
# toda la información debe pasar por acá.
#
# La base de esté código se tomó de
# https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=88&codigo=89&inicio=75
# ---------------------------------------------------------



# ---------------------------------------------------------
# Librerías a usar
# ---------------------------------------------------------
import sqlite3
# ---------------------------------------------------------



# ---------------------------------------------------------
# Clase a usar
# ---------------------------------------------------------
class Items:
    # -----------------------------------------------------
    def open(self):
        # Conectar a la base de datos
        # Si la base de datos no existe, la crea
        conexion = sqlite3.connect("items.db")

        # Crear la tabla si no existe
        # Si la tabla ya existe, generará un error
        # que se captura con el except
        try:
            sql = ""
            sql += "create table Item ("
            sql += "ID integer primary key autoincrement, "
            sql += "Name text, "
            sql += "price real"
            sql += ")"
            conexion.execute(sql)
        except sqlite3.OperationalError:
            pass

        # Retornar la conexión
        # para que se pueda usar en otras funciones
        return conexion
    # -----------------------------------------------------

    # -----------------------------------------------------
    def add(self, data):
        # Abre la conexión a la base de datos
        cone = self.open()

        # Se usa un cursor para ejecutar la consulta
        cursor = cone.cursor()

        # Se usa un string para crear la consulta
        # Se insertan los datos de un artículo
        # en la base de datos
        sql = ""
        sql += "insert into "
        sql += "Item(Name, Price) "
        sql += "values (?,?)"

        # Se ejecuta la consulta con los datos
        # data debe ser una tupla con los valores
        # a insertar, en este caso (Name, Price)
        cursor.execute(sql, data)

        # Se guardan los cambios
        cone.commit()

        # Se cierra la conexión
        cone.close()
    # -----------------------------------------------------

    # -----------------------------------------------------
    def get_id(self, data):
        try:
            # Abre la conexión a la base de datos
            cone = self.open()
            
            # Se usa un cursor para ejecutar la consulta
            cursor = cone.cursor()

            # Se usa un string para crear la consulta
            # Se busca un artículo por su ID
            sql = ""
            sql += "select "
            sql += "Name, Price "
            sql += "from Item "
            sql += "where ID=?"

            # Se ejecuta la consulta con los datos
            # data debe ser una tupla con el ID a buscar
            # en este caso (ID,)
            cursor.execute(sql, data)

            # Se obtienen los resultados
            return cursor.fetchall()
        finally:
            # Se cierra la conexión
            cone.close()
    # -----------------------------------------------------

    # -----------------------------------------------------
    def get_all(self):
        try:
            # Abre la conexión a la base de datos
            cone = self.open()
            
            # Se usa un cursor para ejecutar la consulta
            cursor = cone.cursor()

            # Se usa un string para crear la consulta
            # Se obtienen todos los artículos
            # de la base de datos
            sql = ""
            sql += "select "
            sql += "ID, Name, Price "
            sql += "from Item"

            # Se ejecuta la consulta
            cursor.execute(sql)

            # Se obtienen los resultados
            # y se retornan como una lista de tuplas
            return cursor.fetchall()
        finally:
            # Se cierra la conexión
            cone.close()
# ---------------------------------------------------------