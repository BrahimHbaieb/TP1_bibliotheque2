from classes import *
import os

class Bibliotheque:
    def __init__(self):
        self.documents = []
        self.adherents = []
        self.emprunts = []
        self.charger_adherents("Adherents.txt")
        self.charger_documents("Biblio.txt")
        self.charger_emprunts("Emprunts.txt")

    # Chargement des adhérents depuis un fichier texte
    def charger_adherents(self, fichier):
        if os.path.exists(fichier):
            with open(fichier, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():
                        nom, prenom = line.strip().split(",")
                        adherent = Adherent(nom, prenom)
                        self.adherents.append(adherent)

    # Chargement des documents depuis un fichier texte
    def charger_documents(self, fichier):
        if os.path.exists(fichier):
            with open(fichier, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():
                        data = line.strip().split(",")
                        if data[0] == "L":
                            document = Livre(data[1], data[2], data[3] == "True")
                        elif data[0] == "BD":
                            document = BandeDessinee(data[1], data[2], data[3])
                        elif data[0] == "D":
                            document = Dictionnaire(data[1], data[2])
                        elif data[0] == "J":
                            document = Journal(data[1], data[2])
                        self.documents.append(document)

    # Chargement des emprunts depuis un fichier texte
    def charger_emprunts(self, fichier):
        if os.path.exists(fichier):
            with open(fichier, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():

                        data = line.strip().split(",")

                        adherent = Adherent(data[0], data[1])
                        document = None
                        for doc in self.documents:
                            if doc.titre == data[2]:
                                document = doc
                                break
                        date_emprunt = datetime.strptime(data[3], "%Y-%m-%d").date()
                        date_retour = datetime.strptime(data[4], "%Y-%m-%d").date() if data[4] != "None" else None

                        emprunt = Emprunt(adherent, document, date_emprunt)
                        emprunt.date_retour = date_retour
                        self.emprunts.append(emprunt)

    # Sauvegarde des adhérents dans un fichier texte
    def sauvegarder_adherents(self, fichier):
        with open(fichier, "w") as f:
            for adherent in self.adherents:
                f.write(f"{adherent.nom},{adherent.prenom}\n")

    # Sauvegarde des document dans un fichier texte
    def sauvegarder_documents(self, fichier):
        with open(fichier, "w") as f:
            for document in self.documents:
                if isinstance(document, Livre):
                    f.write(f"L,{document.titre},{document.auteur},{document.disponible}\n")
                elif isinstance(document, BandeDessinee):
                    f.write(f"BD,{document.titre},{document.auteur},{document.dessinateur}\n")
                elif isinstance(document, Dictionnaire):
                    f.write(f"D,{document.titre},{document.auteur}\n")
                elif isinstance(document, Journal):
                    f.write(f"J,{document.titre},{document.date_parution}\n")

    # Sauvegarde des emprunts dans un fichier texte
    def sauvegarder_emprunts(self, fichier):
        with open(fichier, "w") as f:
            for emprunt in self.emprunts:
                if emprunt.document:
                    f.write(
                        f"{emprunt.adherent.nom},{emprunt.adherent.prenom},{emprunt.document.titre},{emprunt.date_emprunt},{emprunt.date_retour}\n")

    # Ajout d'un nouvel adhérent à la bibliothèque
    def ajouter_adherent(self):
        nom = input("Nom de l'adhérent : ")
        prenom = input("Prénom de l'adhérent : ")
        adherent = Adherent(nom, prenom)
        self.adherents.append(adherent)
        self.sauvegarder_adherents("Adherents.txt")
        print(f"{prenom} {nom} a été ajouté comme adhérent.")

    # Suppression d'un adhérent de la bibliothèque
    def enlever_adherent(self):
        nom = input("Nom de l'adhérent à supprimer : ")
        prenom = input("Prénom de l'adhérent à supprimer : ")
        adherent_trouve = None
        for adherent in self.adherents:
            if adherent.nom == nom and adherent.prenom == prenom:
                adherent_trouve = adherent
                break
        if adherent_trouve:
            self.adherents.remove(adherent_trouve)
            self.sauvegarder_adherents("Adherents.txt")
            print(f"{prenom} {nom} a été supprimé comme adhérent.")
        else:
            print(f"L'adhérent {prenom} {nom} n'a pas été trouvé.")

    # Afficher tous les adhérents
    def afficher_adherents(self):
        if not self.adherents:
            print("Aucun adhérent enregistré.")
        else:
            print("Liste des adhérents :")
            for adherent in self.adherents:
                print(f"{adherent.prenom} {adherent.nom}")
                print("=" * 30)


    # Ajouter un document selon son type
    def ajouter_document(self):
        print("Choisissez le type de document à ajouter :")
        print("1. Livre")
        print("2. Bande Dessinée")
        print("3. Dictionnaire")
        print("4. Journal")
        choix = input("Votre choix : ")

        if choix == "1":
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            disponible = input("Le livre est-il disponible ? (Oui/Non) : ").lower() == "oui"
            document = Livre(titre, auteur, disponible)
            self.documents.append(document)
            self.sauvegarder_documents("Biblio.txt")
            print(f"Le livre '{titre}' a été ajouté.")

        elif choix == "2":
            titre = input("Titre de la bande dessinée : ")
            auteur = input("Auteur de la bande dessinée : ")
            dessinateur = input("Dessinateur de la bande dessinée : ")
            document = BandeDessinee(titre, auteur, dessinateur)
            self.documents.append(document)
            self.sauvegarder_documents("Biblio.txt")
            print(f"La bande dessinée '{titre}' a été ajoutée.")

        elif choix == "3":
            titre = input("Titre du dictionnaire : ")
            auteur = input("Auteur du dictionnaire : ")
            document = Dictionnaire(titre, auteur)
            self.documents.append(document)
            self.sauvegarder_documents("Biblio.txt")
            print(f"Le dictionnaire '{titre}' a été ajouté.")

        elif choix == "4":
            titre = input("Titre du journal : ")
            date_parution = input("Date de parution du journal (AAAA-MM-JJ) : ")
            document = Journal(titre, date_parution)
            self.documents.append(document)
            self.sauvegarder_documents("Biblio.txt")
            print(f"Le journal '{titre}' a été ajouté.")

        else:
            print("Choix invalide. Aucun document n'a été ajouté.")

    # Supprimer un document
    def enlever_document(self):
        titre = input("Titre du document à supprimer : ")
        document_trouve = None

        for document in self.documents:
            if document.titre == titre:
                document_trouve = document
                break

        if document_trouve:
            self.documents.remove(document_trouve)
            self.sauvegarder_documents("Biblio.txt")
            print(f"Le document '{titre}' a été supprimé du fichier et de la bibliothèque.")
        else:
            print(f"Le document '{titre}' n'a pas été trouvé.")

    # Supprimer un document de la bibliotheque
    def afficher_documents(self):
        if not self.documents:
            print("Aucun document enregistré.")
        else:
            print("Liste des documents :")
            for document in self.documents:
                if isinstance(document, Livre):
                    doc_type = "Livre"
                    disponible = "Disponible" if document.disponible else "Non disponible"
                    print(f"{doc_type} : {document.titre} - Auteur: {document.auteur} - {disponible}")
                elif isinstance(document, BandeDessinee):
                    doc_type = "Bande Dessinée"
                    print(
                        f"{doc_type} : {document.titre} - Auteur: {document.auteur} - Dessinateur: {document.dessinateur}")
                elif isinstance(document, Dictionnaire):
                    doc_type = "Dictionnaire"
                    print(f"{doc_type} : {document.titre} - Auteur: {document.auteur}")
                elif isinstance(document, Journal):
                    doc_type = "Journal"
                    print(f"{doc_type} : {document.titre} - Date de parution: {document.date_parution}")
                print("=" * 30)

    # Enregister un emprunt de document par adhérent
    def ajouter_emprunt(self):
        nom = input("Nom de l'adhérent : ")
        prenom = input("Prénom de l'adhérent : ")

        adherent_trouve = None
        for adherent in self.adherents:
            if adherent.nom == nom and adherent.prenom == prenom:
                adherent_trouve = adherent
                break

        if adherent_trouve:
            titre_document = input("Titre du document à emprunter :")

            document_trouve = None
            for document in self.documents:
                if document.titre == titre_document:
                    document_trouve = document
                    break

            if document_trouve:
                if isinstance(document_trouve, Livre) and document_trouve.disponible:
                    date_emprunt = datetime.now().date()
                    emprunt = Emprunt(adherent_trouve, document_trouve, date_emprunt)
                    self.emprunts.append(emprunt)
                    document_trouve.disponible = False
                    self.sauvegarder_emprunts("Emprunts.txt")
                    self.sauvegarder_documents("Biblio.txt")
                    print(f"Emprunt enregistré pour {prenom} {nom} : {titre_document}")
                elif isinstance(document_trouve, Livre) and not document_trouve.disponible:
                    print("Le livre n'est pas disponible pour l'emprunt.")
                else:
                    print("Le document n'est pas disponible pour l'emprunt.")
            else:
                print("Le document n'existe pas dans la bibliothèque.")
        else:
            print("L'adhérent n'a pas été trouvé dans la liste des adhérents.")

    # Retourner livre
    def retourner_livre(self):
        titre_document = input("Titre du document à retourner : ")

        emprunt_trouve = None
        for emprunt in self.emprunts:
            if emprunt.document and emprunt.document.titre == titre_document and emprunt.date_retour is None:
                emprunt_trouve = emprunt
                break

        if emprunt_trouve:
            emprunt_trouve.date_retour = datetime.now().date()
            print(emprunt_trouve.date_retour)
            emprunt_trouve.document.disponible = True
            self.sauvegarder_emprunts("Emprunts.txt")
            self.sauvegarder_documents("Biblio.txt")
            print(f"Le document '{titre_document}' a été retourné.")
        else:
            print("Le livre n'a pas été emprunté ou a déjà été retourné.")

    # Aafficher la liste des emprunts
    def afficher_emprunts(self):
        if not self.emprunts:
            print("Aucun emprunt enregistré.")
        else:
            print("Liste des emprunts :")
            for emprunt in self.emprunts:
                adherent = f"{emprunt.adherent.prenom} {emprunt.adherent.nom}"
                document = emprunt.document.titre
                date_emprunt = emprunt.date_emprunt.strftime("%Y-%m-%d")
                if emprunt.date_retour is None :
                    date_retour = "Non retourné"
                else:
                    date_retour = emprunt.date_retour.strftime ("%Y-%m-%d")



                print(f"Adhérent : {adherent}")
                print(f"Document emprunté : {document}")
                print(f"Date d'emprunt : {date_emprunt}")
                print(f"Date de retour : {date_retour}")
                print("=" * 30)
