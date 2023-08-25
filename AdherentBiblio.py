from datetime import datetime, timedelta


class Adherent:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.listeEmprunts = []

    def emprunterLivre(self, livre):
        # Code pour emprunter un livre
        if livre.empruntable():
            livre.disponible = False
            emprunt = Emprunt(self, livre, datetime.now())
            self.listeEmprunts.append(emprunt)
            return emprunt
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")


    def rendreLivre(self, emprunt):
        # Code pour rendre un livre
        if emprunt in self.listeEmprunts:
            self.listeEmprunts.remove(emprunt)
            emprunt.livre.disponible = True
            emprunt.date_retour = datetime.now()
        else:
            print("Cet emprunt n'est pas associé à cet adhérent.")

    def __str__(self):
        return "[Nom: " + self.nom + " Prénom :  " + str(self.prenom) + "]"