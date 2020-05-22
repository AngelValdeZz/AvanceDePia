#Se usa para importar los datos de fecha.
import datetime
#Se usa para acceder un archivo de tipo CSV.
import csv
#Se importa una clase que nos permite extraer elementos de un objeto.
from operator import attrgetter
#Se declara una clase.
#Se utiliza Pascal Casing.
class Contacto :
    # Es un constructor que se encarga de generar un objeto con ciertos parametros establecidos.
    # Esta clase cuenta con seis propiedades que se pueden identificar entre los parentesis. 
    # self no se usa como una propiedad porque es como se le ordena al objeto que tiene que
    # hacerse referencia a si mismo.
    def __init__( self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANACIMIENTO,GASTO):
        #NICKNAME: Se registrara el apodo. Es tipo de dato (str).
        #NOMBRE: Se registrara el nombre. Es tipo de dato (str).
        #CORREO: Se registrara el correo. Es tipo de dato (str)
        #TELEFONO: Se registrara el telefono. Es tipo de dato (int).
        #FECHANACIMIENTO: Se registrara la fecha de nacimiento. Es tipo de dato (datetime).
        #GASTO: Se registrara el gasto. Es tipo de dato (float).
        self.NICKNAME = NICKNAME
        self.NOMBRE = NOMBRE
        self.CORREO = CORREO
        self.TELEFONO = TELEFONO
        self.FECHANACIMIENTO = FECHANACIMIENTO
        self.GASTO = GASTO