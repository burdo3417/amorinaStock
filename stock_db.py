import MySQLdb


class Database:
    host= "localhost"
    user= "root"
    password=""
    db= "stock_test"

    def __init__(self):
        self.connection = MySQLdb.connect(self.host, self.user, self.password, self.db)
        self.cursor = self.connection.cursor()

    def insert (self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("INSERT succesfully")
        except:
            self.connection.rollback()
            print("INSERT error")

    def query (self, query):
            cursor = self.connection.cursor( MySQLdb.cursors.DictCursor )
            cursor.execute(query)
            return cursor.fetchall()

    def __del__(self):
            self.connection.close()

db = Database()

producto_name = input("Producto: \n")
cantidad= int(input("Cantidad: \n"))



query = """INSERT INTO stock_test (producto, stock)
        VALUES ("%s" , "%d")
        ON DUPLICATE KEY UPDATE stock = stock + "%d"
        """ % (producto_name,cantidad, cantidad)

db.insert(query)
