from datetime import datetime

# Classe de base pour tous les documents
class Document:
    def __init__(self, titre):
        self.titre = titre

# Classe représentant un document avec un auteur
class Volume(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

# Classe représentant un livre
class Livre(Volume):
    def __init__(self, titre, auteur, disponible=True):
        super().__init__(titre, auteur)
        self.disponible = disponible

# Classe représentant une bande dessinée
class BandeDessinee(Volume):
    def __init__(self, titre, auteur, dessinateur):
        super().__init__(titre, auteur)
        self.dessinateur = dessinateur

# Classe représentant un dictionnaire
class Dictionnaire(Volume):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur)

# Classe représentant un journal
class Journal(Document):
    def __init__(self, titre, date_parution):
        super().__init__(titre)
        self.date_parution = date_parution

# Classe représentant un adhérent de la bibliothèque
class Adherent:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

# Classe représentant un emprunt de document par un adhérent
class Emprunt:
    def __init__(self, adherent, document, date_emprunt, date_retour = None):
        self.adherent = adherent
        self.document = document
        self.date_emprunt = date_emprunt
        self.date_retour = date_retour






