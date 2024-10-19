import numpy as np

class Casa:
    def __init__(self, n_habitaciones = 1, m_cuadrados = 20, propietario = '', precio = 50000.0): #Puede ser una casa sin dueño
        if m_cuadrados < 20 or precio < 50000:
            raise ValueError("La casa debe tener tamaño minimo y precio real")

        self.n_habitaciones = n_habitaciones
        self.m_cuadrados = m_cuadrados
        self.propietario = propietario
        self.precio = float(precio)

    @property
    def n_habitaciones(self):
        return self.__n_habitaciones

    @property
    def m_cuadrados(self):
        return self.__m_cuadrados

    @property
    def propietario(self):
        return self.__propietario

    @property
    def precio(self):
        return self.__precio

    @n_habitaciones.setter
    def n_habitaciones(self, n_habitaciones):
        if not isinstance(n_habitaciones, int):
            raise ValueError('Error. Invalid input, input a valid integer.')
        self.__n_habitaciones = n_habitaciones

    @m_cuadrados.setter
    def m_cuadrados(self, m_cuadrados):
        if not isinstance(m_cuadrados, int):
            raise ValueError('Error. Invalid input, input a valid number.')
        self.__m_cuadrados = m_cuadrados

    @propietario.setter
    def propietario(self, propietario):
        if not isinstance(propietario, str):
            raise ValueError('Error. Invalid input, input a valid string.')
        self.__propietario = propietario

    @precio.setter
    def precio(self, precio):
        if not isinstance(precio, float):
            raise ValueError('Error. Invalid input, input a valid number.')
        self.__precio = precio

    def mostrar_datos(self):
        return "Numero de habitaciones: " + str(self.__n_habitaciones) + "\nTamaño en metros cuadrados: " + str(self.__m_cuadrados) + "m^2\nPropietario de la vivienda: " + self.__propietario + "\nPrecio: " + str(self.__precio) + "€"

    def build_rooms(self, n_habitaciones, m_cuadrados):
        self.__m_cuadrados += m_cuadrados
        self.__n_habitaciones += n_habitaciones
        print(f"Se han construido {n_habitaciones} habitaciones y se han ganado {m_cuadrados}m^2")


class PisoAlquiler(Casa):

    def __init__(self, n_habitaciones = 1, m_cuadrados = 20, propietario = '', precio = 50000, alquilerMensual = 400.0, arrendador = ''):
        super().__init__(n_habitaciones, m_cuadrados, propietario, precio)
        self.alquilerMensual = alquilerMensual
        self.arrendador = arrendador

    @property
    def alquilerMensual(self):
        return self.__alquilerMensual

    @property
    def arrendador(self):
        return self.__arrendador

    @alquilerMensual.setter
    def alquilerMensual(self, alquilerMensual):
        if not isinstance(alquilerMensual, float):
            raise ValueError('Error. Invalid input, input a valid integer.')
        self.__alquilerMensual = alquilerMensual

    @arrendador.setter
    def arrendador(self, arrendador):
        if not isinstance(arrendador, str):
            raise ValueError('Error. Invalid input, input a valid string.')
        self.__arrendador = arrendador

    def mostrar_datos(self):
        return "\nDatos piso alquiler: \n" + super().mostrar_datos() + "\nAlquilado por: " + str(self.__alquilerMensual) + "€\nArrendado por: " + self.__arrendador

    #We will supose that the extra payments are for waste, neighbour community etc. and that are calculated in base of number of rooms and m^2
    def calcular_gastos(self):
        gastos_extra = self.n_habitaciones*self.m_cuadrados/2
        return self.__alquilerMensual + gastos_extra



class Hotel(Casa):
    def __init__(self, n_habitaciones = 10, m_cuadrados = 20, propietario = '', precio = 50000, n_clientes = 5, precio_por_noche = 20):
        if n_clientes < 0:
            raise ValueError("El hotel no puede tener menos de 0 clientes")
        if n_habitaciones < 10:
            raise ValueError("El hotel debe tener minimo 10 habitaciones")
        if n_clientes > n_habitaciones:
            raise ValueError("El hotel no puede tener mas clientes que habitaciones")
        if m_cuadrados<n_habitaciones*5:
            raise ValueError("El hotel no puede ser tan pequeño")
        super().__init__(n_habitaciones, m_cuadrados, propietario, precio)
        self.n_clientes = n_clientes
        self.precio_por_noche = float(precio_por_noche)

    @property
    def n_clientes(self):
        return self.__n_clientes

    @property
    def precio_por_noche(self):
        return self.__precio_por_noche

    @n_clientes.setter
    def n_clientes(self, n_clientes):
        if not isinstance(n_clientes, int):
            raise ValueError('Error. Invalid input, input a valid number.')
        self.__n_clientes = n_clientes

    @precio_por_noche.setter
    def precio_por_noche(self, precio_por_noche):
        if not isinstance(precio_por_noche, float):
            raise ValueError('Error. Invalid input, input a valid number.')
        self.__precio_por_noche = precio_por_noche

    def habitaciones_libres(self):
        return self.n_habitaciones - self.__n_clientes

    def check_in(self, n_cliente):
        if self.habitaciones_libres() >= n_cliente:
            self.__n_clientes += n_cliente
            print("Numero de habitaciones restantes: ", self.habitaciones_libres())
        else:
            print("Lo sentimos, no hay habitaciones libres")

    def check_out(self, n_cliente):
        if n_cliente <= self.__n_clientes:
            self.__n_clientes -= n_cliente
            print(f"Check-out de {n_cliente} clientes realizado. Habitaciones disponibles: {self.habitaciones_libres()}")
        else:
            raise ValueError("No hay tantos clientes en el hotel")

    def mostrar_datos(self):
        return "\nDatos del hotel: \n" + super().mostrar_datos() + "\nNumero de clientes: " + str(self.__n_clientes) + "\nPrecio por noche: " + str(self.__precio_por_noche) +"€"

if __name__ == '__main__':
    c1 = Casa(n_habitaciones=3, m_cuadrados=80, propietario='Jose', precio=200000)
    print(c1.mostrar_datos())

    pa1 = PisoAlquiler(propietario='Paco', arrendador='Monica')
    print(pa1.mostrar_datos())
    pa1.build_rooms(2, 40)
    print("Gastos mensuales: ", pa1.calcular_gastos(), "€") #No entiendo bien porque si pongo self.__n_habitaciones y self.__m_cuadrados no me va

    h1 = Hotel(n_habitaciones=30, m_cuadrados=300)
    print(h1.mostrar_datos())
    print("Habitaciones disponibles: ", h1.habitaciones_libres())
    h1.build_rooms(4, 40)
    print("Habitaciones disponibles: ", h1.habitaciones_libres()) #hereda bien los metodos
    n_clientes = np.random.randint(0,10)
    print(f"Intentando dar {n_clientes} habitaciones")
    h1.check_in(n_clientes)
    print(f"Haciendo el check_out de {n_clientes} clientes: ")
    h1.check_out(n_clientes + 1)
    h1.check_out(n_clientes)