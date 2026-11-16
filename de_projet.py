"""Tirage au dé de votre projet « Mon Quartier en 30 jours ».

À lancer UNE SEULE FOIS, en classe, quand l'enseignant annonce le mot secret :
    python de_projet.py

Le programme :
  1. calcule vos trois lancers à partir de votre matricule et du mot secret ;
  2. enregistre le résultat dans tirage.json ;
  3. ajoute le résultat à la fin de JOURNAL.md.

Ensuite : git add tirage.json JOURNAL.md, git commit, git push.
Toute modification de ces fichiers après coup sera détectée.
"""
import datetime
import hashlib
import json
import random
import sys

from tables_des import ACTIVITES, CONTRAINTES, EVENEMENTS

FICHIER_TIRAGE = "tirage.json"
FICHIER_JOURNAL = "JOURNAL.md"


def lancer_des(matricule, mot_secret):
    """Renvoie trois entiers entre 1 et 6, toujours les mêmes pour un même couple."""
    graine = hashlib.sha256(f"{mot_secret}|{matricule}".encode("utf-8")).hexdigest()
    generateur = random.Random(graine)
    return [generateur.randint(1, 6) for _ in range(3)]


def construire_tirage(nom, matricule, mot_secret):
    des = lancer_des(matricule, mot_secret)
    return {
        "nom": nom,
        "matricule": matricule,
        "des": des,
        "activite": ACTIVITES[des[0] - 1],
        "evenement": EVENEMENTS[des[1] - 1],
        "contrainte": CONTRAINTES[des[2] - 1],
        "date": datetime.datetime.now().isoformat(timespec="seconds"),
    }


def tirage_existe():
    try:
        with open(FICHIER_TIRAGE, encoding="utf-8"):
            return True
    except FileNotFoundError:
        return False


def ecrire_tirage(tirage):
    with open(FICHIER_TIRAGE, "w", encoding="utf-8") as fichier:
        json.dump(tirage, fichier, ensure_ascii=False, indent=2)
    with open(FICHIER_JOURNAL, "a", encoding="utf-8") as fichier:
        fichier.write("\n## Mon tirage au dé\n")
        fichier.write(f"- **Lancers :** {tirage['des'][0]}, {tirage['des'][1]}, {tirage['des'][2]}\n")
        fichier.write(f"- **Mon activité :** {tirage['activite']}\n")
        fichier.write(f"- **Mon événement imposé :** {tirage['evenement']}\n")
        fichier.write(f"- **Ma contrainte technique :** {tirage['contrainte']}\n")


def principal():
    if tirage_existe():
        print(f"Le fichier {FICHIER_TIRAGE} existe déjà : le tirage ne peut se faire qu'une fois.")
        sys.exit(1)
    nom = input("Votre nom et prénom : ").strip()
    matricule = input("Votre matricule : ").strip()
    mot_secret = input("Le mot secret annoncé par l'enseignant : ").strip()
    if not nom or not matricule or not mot_secret:
        print("Les trois informations sont obligatoires.")
        sys.exit(1)
    tirage = construire_tirage(nom, matricule, mot_secret)
    ecrire_tirage(tirage)
    print("\nLancers :", tirage["des"])
    print("Activité   :", tirage["activite"])
    print("Événement  :", tirage["evenement"])
    print("Contrainte :", tirage["contrainte"])
    print("\nRésultat enregistré. Faites maintenant : git add . puis git commit puis git push.")


if __name__ == "__main__":
    principal()
