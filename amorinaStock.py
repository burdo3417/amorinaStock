import dill
import os.path

if os.path.isfile("dill.pkl"):
   dill.load_session('dill.pkl')
else:
   exit

class Producto:
   def __init__ (self, nombre, talle, precio):
      self.nombre = nombre
      self.talle = talle
      self.produccion = 0
      self.precio = precio
      print("\n")    
      
   def print_producto(self):
      print("Nombre: " + self.nombre)
      print("Talle: " + str(self.talle))
      print("Unidades Producidas: " + str(self.produccion))
      print("Precio: " + str(self.precio))
      print("\n")
  
   def agregarProduccion(self, cantidadProducida):
      print("\n")
      self.produccion += cantidadProducida
      print("Se produjeron " + str(cantidadProducida) + " unidades del producto " + self.nombre) 
      print("El total producido es " + str(self.produccion))
      print("\n")
      
      
class Local:
   def __init__ (self,nombre,direccion, tel, mail):
      self.nombre = nombre
      self.direccion = direccion
      self.tel = tel
      self.mail = mail
      self.balance = 0
      self.unidadesVendidas = 0
      
   def print_local(self):
      print ("Nombre: " + self.nombre)
      print("Direccion: " + self.direccion)
      print("Telefono: " + self.tel)
      print("Mail: " + self.mail)
      print( "Debe :" + str(self.balance))
      print("Unidades Vendidas: " + str(self.unidadesVendidas))
      print("\n")
      
   def agregarDeuda(self,deuda):
      self.balance += deuda
      print("Debe " + str(deuda) + " mas.")
      print ("Deuda Total asciende a: "+ str(self.balance))
      print("\n")
      
      
def grabarSesion():
      dill.dump_session("dill.pkl")
      print("\n")
      print("Sesion Grabada")
      
  
#corpIbizaNegroSmall = Producto("Corpiño Ibiza Negro","Small",240)
#corpIbizaNegroSmall.agregarProduccion(50)
corpIbizaNegroSmall.print_producto()

#culloteNegroRomaMedium = Producto("Culotte","Medium",140)
#culloteNegroRomaMedium.agregarProduccion(50)
culloteNegroRomaMedium.print_producto()


#fiona = Local("fiona","Sarmiento 881","448466","fiona@fiona.com.ar")
#fiona.agregarDeuda(1000)
#fiona.agregarDeuda(500)
fiona.print_local()






grabarSesion()


                   

