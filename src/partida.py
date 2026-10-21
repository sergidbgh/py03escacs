#from peo import Peo

#definició columnes
ca=0
cb=1
cc=2
cd=3
ce=4
cf=5
cg=6
ch=7
#definició files
f1=0
f2=1
f3=2
f4=3
f5=4
f6=5
f7=6
f8=7


#### Notes
# Lletra = columna: a fins a h
# Número = fila: 1 fins a 8

class Partida:
    tipus = "partida"

    # Constructor
    def __init__(self, nom, id):
        self.nom = nom
        self.tauler = [
            ["tb1", "pb1", "nul", "nul", "nul", "nul", "pn1", "tn1"],  # columna a
            ["cb1", "pb2", "nul", "nul", "nul", "nul", "pn2", "cn1"],  # columna b
            ["ab1", "pb3", "nul", "nul", "nul", "nul", "pn3", "an1"],  # columna c
            ["rb1", "pb4", "nul", "nul", "nul", "nul", "pn4", "en1"],  # columna d
            ["eb1", "pb5", "nul", "nul", "nul", "nul", "pn5", "rn1"],  # columna e
            ["ab2", "pb6", "nul", "nul", "nul", "nul", "pn6", "an2"],  # columna f
            ["cb2", "pb7", "nul", "nul", "nul", "nul", "pn7", "cn2"],  # columna g
            ["tb2", "pb8", "nul", "nul", "nul", "nul", "pn8", "tn2"]   # columna h
        ]
        self.id = id
        self.viu = True
        self.taules = False
        self.mostrar_info()
        self.mostrar_tauler_manual()
#        definicio_blanques()
#        definicio_negres()
#        print(peo.nom)
#        print(peo.ip)
#        print(peo.memoria)

#    def definicio_negreses():
#        return

#    def definicio_blanques():
#        peob1 = Peo("blanc",1,"a2")
#        peob2 = Peo("blanc",2,"b2")
#        peob3 = Peo("blanc",3,"c2")
#        peob4 = Peo("blanc",4,"d2")
#        peob5 = Peo("blanc",5,"e2")
#        peob6 = Peo("blanc",6,"f2")
#        peob7 = Peo("blanc",7,"g2")
#        peob8 = Peo("blanc",8,"h2")
#        return

    def mostrar_info(self):
        print("Nom:", self.nom)
        print("ID:", self.id)
        print("Viu:", self.viu)
        print("Taules:", self.taules) 

    def mostrar_tauler_manual(self):
        print("mostrar tauler")
        print(self.tauler[ca][f8],self.tauler[cb][f8],self.tauler[cc][f8],self.tauler[cd][f8],self.tauler[ce][f8],self.tauler[cf][f8],self.tauler[cg][f8],self.tauler[ch][f8])
        print(self.tauler[ca][f7],self.tauler[cb][f7],self.tauler[cc][f7],self.tauler[cd][f7],self.tauler[ce][f7],self.tauler[cf][f7],self.tauler[cg][f7],self.tauler[ch][f7])
        print(self.tauler[ca][f6],self.tauler[cb][f6],self.tauler[cc][f6],self.tauler[cd][f6],self.tauler[ce][f6],self.tauler[cf][f6],self.tauler[cg][f6],self.tauler[ch][f6])
        print(self.tauler[ca][f5],self.tauler[cb][f5],self.tauler[cc][f5],self.tauler[cd][f5],self.tauler[ce][f5],self.tauler[cf][f5],self.tauler[cg][f5],self.tauler[ch][f5])
        print(self.tauler[ca][f4],self.tauler[cb][f4],self.tauler[cc][f4],self.tauler[cd][f4],self.tauler[ce][f4],self.tauler[cf][f4],self.tauler[cg][f4],self.tauler[ch][f4])
        print(self.tauler[ca][f3],self.tauler[cb][f3],self.tauler[cc][f3],self.tauler[cd][f3],self.tauler[ce][f3],self.tauler[cf][f3],self.tauler[cg][f3],self.tauler[ch][f3])
        print(self.tauler[ca][f2],self.tauler[cb][f2],self.tauler[cc][f2],self.tauler[cd][f2],self.tauler[ce][f2],self.tauler[cf][f2],self.tauler[cg][f2],self.tauler[ch][f2])
        print(self.tauler[ca][f1],self.tauler[cb][f1],self.tauler[cc][f1],self.tauler[cd][f1],self.tauler[ce][f1],self.tauler[cf][f1],self.tauler[cg][f1],self.tauler[ch][f1])
        
        


