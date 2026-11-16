"""Tables de correspondance du tirage au dé (identiques à celles du Cahier du projet)."""

ACTIVITES = [
    "Boutique de quartier : stock et ruptures",
    "Taxi ou transport : trajets et carburant",
    "Pêche en pirogue : marée et saison",
    "Maquis ou petit restaurant : recettes et péremption",
    "Atelier de couture : commandes et délais",
    "Cybercafé : postes, pannes et connexion",
]

EVENEMENTS = [
    "Grève ou pénurie d'un produit",
    "Saison des pluies : activité réduite",
    "Contrôle administratif avec amende possible",
    "Fête de quartier : pic de demande",
    "Panne d'équipement",
    "Client qui achète à crédit et tarde à payer",
]

CONTRAINTES = [
    "Les événements sont produits par un générateur (yield)",
    "Un décorateur journalise chaque action du joueur",
    "Une classe abstraite avec au moins 3 sous-classes",
    "Sauvegarde et reprise de partie complétées par une option en ligne de commande (argparse)",
    "Une fonction récursive utile au jeu (par exemple le calcul d'une dette échelonnée)",
    "Une classe de valeurs avec __add__, __lt__ et __str__ (par exemple une classe Montant)",
]
