from peo import Peo


def crear_peo():
    peo = Peo("srvweb01", "192.168.1.10", 16)
    return peo


def main():
    peo = crear_peo()

    print(peo.nom)
    print(peo.ip)
    print(peo.memoria)


if __name__ == "__main__":
    main()