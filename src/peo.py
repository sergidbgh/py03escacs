from peca import Peca

class Peo(Peca):
    # Variable general de la classe
    tipus = "Servidor Linux"

    # Constructor
    def __init__(self, color_fitxa, id):
        self.id = id
        self.viu = True

    # Mètode que modifica un paràmetre
    def canviar_ip(self, nova_ip):
        self.ip = nova_ip

    # Un altre mètode
    def desactivar(self):
        self.actiu = False

    # Mètode per mostrar la informació
    def mostrar_info(self):
        print("Nom:", self.nom)
        print("IP:", self.ip)
        print("Memòria:", self.memoria, "GB")
        print("Actiu:", self.actiu)


# Crear un objecte de la classe
servidor1 = Servidor("srvweb01", "192.168.1.10", 16)

servidor1.mostrar_info()

# Canviam la IP
servidor1.canviar_ip("192.168.1.20")

print("\nDesprés de canviar la IP:")
servidor1.mostrar_info()