# donnees.py - Les personnages et les objets du cybercafe

class Personnage:
    """Parent de tous les personnages"""
    def __init__(self, nom, argent):
        self.nom = nom
        self.argent = argent

    def presenter(self):
        return f"{self.nom} a {self.argent} FCFA"

class Client(Personnage):
    """Un client du cybercafe, il herite de Personnage"""
    def __init__(self, nom, argent, dette=0):
        super().__init__(nom, argent)
        self.dette = dette

class Fournisseur(Personnage):
    """Le fournisseur qui vend le credit, il herite de Personnage"""
    def __init__(self, nom, argent, stock=20):
        super().__init__(nom, argent)
        self.stock = stock

class Objet:
    """Un objet a vendre dans le cybercafe"""
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix