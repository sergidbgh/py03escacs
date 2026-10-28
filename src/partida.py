#from peo import Peo

#### Notes
# Lletra = columna: a fins a h
# Número = fila: 1 fins a 8

class Partida:
    tipus = "partida"

    # Constructor
    def __init__(self, nom, id):
        self.nom = nom
        #self.tauler = [None, None, None, None, None, None, None, None,
        #              None, None, None, None, None, None, None, None,
        #              None, None, None, None, None, None, None, None,
        #              None, None, None, None, None, None, None, None,
        #              None, None, None, None, None, None, None, None,
        #              None, None, None, None, None, None, None, None,
        #              None, None, None, None, None, None, None, None,
        #              None, None, None, None, None, None, None, None]
        
        self.tauler = ["tn1", "cn1", "an1", "dn1", "rn1", "an2", "cn2", "tn2",
                      "pn1", "pn2", "pn3","pn4","pn5","pn6","pn7","pn8",
                      None, None, None, None, None, None, None, None,
                      None, None, None, None, None, None, None, None,
                      None, None, None, None, None, None, None, None,
                      "pb1", "pb2", "pb3","pb4","pb5","pb6","pb7","pb8",
                      "tb1", "cb1", "ab1", "rb1", "db1", "ab2", "cb2", "tb2"]
        #self.tauler = [
        #    ["tb1", "pb1", "nul", "nul", "nul", "nul", "pn1", "tn1"],  # columna a
        #    ["cb1", "pb2", "nul", "nul", "nul", "nul", "pn2", "cn1"],  # columna b
        #    ["ab1", "pb3", "nul", "nul", "nul", "nul", "pn3", "an1"],  # columna c
        #    ["rb1", "pb4", "nul", "nul", "nul", "nul", "pn4", "en1"],  # columna d
        #    ["eb1", "pb5", "nul", "nul", "nul", "nul", "pn5", "rn1"],  # columna e
        #    ["ab2", "pb6", "nul", "nul", "nul", "nul", "pn6", "an2"],  # columna f
        #    ["cb2", "pb7", "nul", "nul", "nul", "nul", "pn7", "cn2"],  # columna g
        #    ["tb2", "pb8", "nul", "nul", "nul", "nul", "pn8", "tn2"]   # columna h
        #]
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

    def posició_a_valor(columna, fila):
        # mos passen el valor de notació d'escacs
        # mos passen el valor "a", "b" ... fins "h"
        # mos passen el valor "1", "a" ... fins "8"
        # retornam el valor de la posició dins del tauler que és columna/fila
        casella = 0
        #tractam FILA (podria fer casella = 8 - int(fila) però prefereix visualitzar tots els valors)
        if fila == "8": casella = 0
        elif fila == "7": casella = 1
        elif fila == "6": casella = 2
        elif fila == "5": casella = 3
        elif fila == "4": casella = 4
        elif fila == "3": casella = 5
        elif fila == "2": casella = 6
        elif fila == "1": casella = 7
        else: casella = 0

        #tractam COMLUMNA
        columna = columna.upper()
        if columa == "A": casella = (casella * 8) + 0
        elif columna == "B": casella = (casella * 8) + 1
        elif columna == "C": casella = (casella * 8) + 2
        elif columna == "D": casella = (casella * 8) + 3
        elif columna == "E": casella = (casella * 8) + 4
        elif columna == "F": casella = (casella * 8) + 5
        elif columna == "G": casella = (casella * 8) + 6
        elif columna == "H": casella = (casella * 8) + 7
        else: casella = 0
        return casella

    def mostrar_info(self):
        print("Nom:", self.nom)
        print("ID:", self.id)
        print("Viu:", self.viu)
        print("Taules:", self.taules) 

    def mostrar_tauler_manual(self):
        print("mostrar tauler")
        for i in range(64): 
            print(i," ")
        for i in range(64): 
            print(self.tauler[i]," ", end="")
            if i in (7,15,23,31,39,47,55,63): print(" ")
        #print(self.tauler[ca][f8],self.tauler[cb][f8],self.tauler[cc][f8],self.tauler[cd][f8],self.tauler[ce][f8],self.tauler[cf][f8],self.tauler[cg][f8],self.tauler[ch][f8])
        #print(self.tauler[ca][f7],self.tauler[cb][f7],self.tauler[cc][f7],self.tauler[cd][f7],self.tauler[ce][f7],self.tauler[cf][f7],self.tauler[cg][f7],self.tauler[ch][f7])
        #print(self.tauler[ca][f6],self.tauler[cb][f6],self.tauler[cc][f6],self.tauler[cd][f6],self.tauler[ce][f6],self.tauler[cf][f6],self.tauler[cg][f6],self.tauler[ch][f6])
        #print(self.tauler[ca][f5],self.tauler[cb][f5],self.tauler[cc][f5],self.tauler[cd][f5],self.tauler[ce][f5],self.tauler[cf][f5],self.tauler[cg][f5],self.tauler[ch][f5])
        #print(self.tauler[ca][f4],self.tauler[cb][f4],self.tauler[cc][f4],self.tauler[cd][f4],self.tauler[ce][f4],self.tauler[cf][f4],self.tauler[cg][f4],self.tauler[ch][f4])
        #print(self.tauler[ca][f3],self.tauler[cb][f3],self.tauler[cc][f3],self.tauler[cd][f3],self.tauler[ce][f3],self.tauler[cf][f3],self.tauler[cg][f3],self.tauler[ch][f3])
        #print(self.tauler[ca][f2],self.tauler[cb][f2],self.tauler[cc][f2],self.tauler[cd][f2],self.tauler[ce][f2],self.tauler[cf][f2],self.tauler[cg][f2],self.tauler[ch][f2])
        #print(self.tauler[ca][f1],self.tauler[cb][f1],self.tauler[cc][f1],self.tauler[cd][f1],self.tauler[ce][f1],self.tauler[cf][f1],self.tauler[cg][f1],self.tauler[ch][f1])
        
        


