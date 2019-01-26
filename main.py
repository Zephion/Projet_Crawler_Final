#from Client import Client
from crawler import Crawler
from database import Base_donnee
from verifi import *


TCP_IP = "node.nicopr.fr"
TCP_PORT = 55555
BUFFER_SIZE = 2048


X = Verifi()
#client = Client(TCP_IP,TCP_PORT,BUFFER_SIZE)
#data = client.connectToServer()

MotAchercher = input(">> Entrer un mot a chercher: ")

Y=X.verification(MotAchercher)

#[definition, synonyme] = Crawler().web(1,"https://fr.wiktionary.org/wiki/", MotAchercher)
if(Y == None):
	Crawler().web(1,"https://fr.wiktionary.org/wiki/", MotAchercher)
else:
   print("Le mot: ", MotAchercher," est déjà presente dans la base de donnée.")

#print("\n Partie main:\n")
#print(definition)
#print("\n\n")
#print(synonyme)

