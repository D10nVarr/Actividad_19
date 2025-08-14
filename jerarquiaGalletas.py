class Galleta:
    def __init__(self, nombre, precio, peso):
        self.nombre = nombre
        self.precio = precio
        self.peso = peso

    def mostrar_galleta(self):
        print(f"Nombre: {self.nombre}, Precio: {self.precio}, Peso: {self.peso}", end=" ")

class GalletaChispas(Galleta):
    def __init__(self, nombre, precio, peso, cantidad_chispas):
        super().__init__(nombre, precio, peso)
        self.cantidad_chispas = cantidad_chispas

    def mostrar_galleta(self):
        super().mostrar_galleta()
        print(f"Cantidad de chispas: {self.cantidad_chispas}")

class Relleno:
    def __init__(self, sabor_relleno):
        self.sabor_relleno = sabor_relleno

    def describir_relleno(self):
        print(f"Galleta rellena de {self.sabor_relleno}")

class GalletaRellena(Galleta, Relleno):
    def __init__(self, nombre, precio, peso, sabor_relleno):
        Galleta.__init__(self, nombre, precio, peso)
        Relleno.__init__(self, sabor_relleno)

    def mostrar_galleta(self):
        super().mostrar_galleta()
        print(f"Relleno de: {self.sabor_relleno}")

class AgregarGalletasSimples:
    def __init__(self):
        self.galletas = []

    def registrar_galleta(self):
        try:
            while True:
                nombre=input("Ingrese el nombre de la galleta: ").lower()
                if nombre.strip() == "":
                    print("El nombre no puede quedar vacio")
                else:
                    break
            while True:
                precio=int(input("Ingrese el precio de la galleta: "))
                if precio<0:
                    print("El precio no puede ser menor a 0")
                else:
                    break
            while True:
                peso=int(input("Ingrese el peso de la galleta: "))
                if peso<0:
                    print("El peso no puede ser menor a 0")
                else:
                    break
            return nombre, precio, peso
        except ValueError:
            print("El valor ingresado no es valido")
        except Exception as e:
            print("Error inesperado", e)

    def agregar_galleta(self):
        nombre, precio, peso = self.registrar_galleta()
        self.galletas.append(Galleta(nombre,precio,peso))

    def mostrar_charola(self):
        if not self.galletas:
            print("No hay galletas registradas.\n")
        else:
            print("\nLista de de galletas:")
            for i, cookie in enumerate(self.galletas, start=1):
                print(f"{i}. {cookie.mostrar_info()}")
            print()

    def buscar_galleta(self):
        if not self.galletas:
            print("No hay galletas registradas.\n")
        buscador=input("Ingrese el nombre de la galleta: ").lower()
        if buscador not in self.galletas:
            print("La galleta no existe")
        else:
            for i in self.galletas:
                if buscador==i:
                    print(f"La galletas es {i}")
                    break

    def eliminar_galleta(self):
        if not self.galletas:
            print("No hay galletas registradas.\n")
        eliminador = input("Ingrese el nombre de la galleta que desea eliminar: ").lower()
        if eliminador not in self.galletas:
            print("La galleta no existe")
        else:
            for i in self.galletas:
                if eliminador == i:
                    self.galletas.remove(i)
                    break


class AgregarGalletasChispas(GalletaChispas, AgregarGalletasSimples):
    def agregar_galleta(self):
        nombre, precio, peso = self.registrar_galleta()#Para reutilizar el ingreso da los datos
        try:
            while True:
                chispas=int(input("Ingrese el cantidad de chispas de su galleta: "))
                if chispas<0:
                    print("El cantidad de chispas no puede ser menor a 0")
                elif chispas==0:
                    print("Esta es una galleta normal, no una de chispas")
                else:
                    break
            self.galletas.append(GalletaChispas(nombre, precio, peso, chispas))
        except ValueError:
            print("La cantidad de chispas debe ser un numero")

class AgregarGalletasRellenas(GalletaRellena, AgregarGalletasSimples):
    def agregar_galleta(self):
        nombre, precio, peso = self.registrar_galleta()
        try:
            while True:
                relleno=input("Ingrese el sabor de relleno de su galleta: ")
                if relleno.strip()==0:
                    print("Debe agregar un sabor de relleno")
                else:
                    break
            self.galletas.append(GalletaRellena(nombre, precio, peso, relleno))
        except Exception as e:
            print("Error inesperado", e)

simple=AgregarGalletasSimples()
chispa=AgregarGalletasChispas(None,None,None,None)
sabor=AgregarGalletasRellenas(None,None,None,None)

while True:
    print("__REPOSTERIA DE GALLETAS__")
    print("1. Registrar galleta básica")
    print("2. Registrar galleta con chispas")
    print("3. Registrar galleta rellena")
    print("4. Listar galletas")
    print("5. Buscar por nombre")
    print("6. Eliminar por nombre")
    print("7. Salir")

    opcion=input("\nEscoja una opción: ")

    match opcion:
        case "1":
            simple.agregar_galleta()
            print("Galleta simple registrada\n")
        case "2":
            chispa.agregar_galleta()
            print("Galleta con chispas registrada\n")
        case "3":
            sabor.agregar_galleta()
            print("Galleta rellena registrada\n")
        case "4":
            simple.mostrar_charola()
        case "5":
            simple.buscar_galleta()
        case "6":
            simple.eliminar_galleta()
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opción no existente")

