#varlog.py
#variable sortida (definida a variables.py)
#1 = pantalla
#2 = pantalla+fitxer
#3 = fitxer sols
import time
fitxerSortida = '../log/sortida'+str(time.strftime("%Y%m%d%H%M%S"))+'.log'
	
def sortida(cadena):	
	#print("tipusSortida:", tipusSortida)
	print(time.strftime("%Y%m%d %H:%M:%S"),cadena)
	ff = open(fitxerSortida, 'a') 
	ff.write(str(time.strftime("%Y%m%d %H:%M:%S"))+" "+cadena+"\n")	
	ff.close()




