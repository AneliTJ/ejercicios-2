class MiError(Exception):
    def __init__(self,mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

#esto es para crear una excepcion
def escribirNombre(nombre):
    if (nombre == ""):
        raise MiError("No se puede imprimir, pues viene vacio")
    else: 
        print(f"El nombre es {nombre}")

try:
    saludo=escribirNombre("Neli")

except MiError as e:
    print (e)