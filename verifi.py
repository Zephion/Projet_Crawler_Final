import sqlite3

class Verifi:
    def __init__(self):
       self.connection = 0
       self.cursor = 0
       self.connection = sqlite3.connect("baseDoc.db")
       self.cursor = self.connection.cursor()
       self.cherche = ""
       self.idTheme = ""
       self.idTheme2 = ""

    def verification(self, motAchercher):
       self.cherche = motAchercher
       self.cursor.execute('''select id_theme from Theme where mot =?''', (self.cherche,))
       self.idTheme = self.cursor.fetchone()
       #print("Les id de la table theme: ", self.idTheme) 
       return self.idTheme
