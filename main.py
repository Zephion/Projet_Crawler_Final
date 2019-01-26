#from Client import Client
from crawler import Crawler
from database import Base_donnee


TCP_IP = "node.nicopr.fr"
TCP_PORT = 55555
BUFFER_SIZE = 2048
i = 1
X = Base_donnee()

while i == 1:
	MotAchercher = input("\n>> Entrer un mot a chercher: ")

	Y=X.verification(MotAchercher)

	if(Y == None):
		Crawler().web(1,"https://fr.wiktionary.org/wiki/", MotAchercher)
	else:
		print("Le mot: ", MotAchercher," est déjà presente dans la base de donnée.")
		Documentation = X.selection(MotAchercher)
		print(Documentation)
