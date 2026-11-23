# === CYBERCAFE D'ELMY ===
# Fichier a moi : elmy_cybercafe.py
# Tirage : des 6, 6, 2
# Activite : Cybercafe postes, pannes et connexion
# Evenement : Client qui achete a credit et tarde a payer
# Contrainte : Un decorateur journalise chaque action

# --- 1. MES 10 CLIENTS ---
# Chaque client a un nom, un argent, et une dette
clients = [
    {"nom": "Maman Aicha", "argent": 1000, "dette": 0},
    {"nom": "Kevin", "argent": 2000, "dette": 0},
    {"nom": "Papa Jean", "argent": 500, "dette": 0},
    {"nom": "Sarah", "argent": 1500, "dette": 0},
    {"nom": "Petit Yann", "argent": 200, "dette": 0},
    {"nom": "Tatie Rose", "argent": 1200, "dette": 0},
    {"nom": "Moussa", "argent": 1800, "dette": 0},
    {"nom": "Lea", "argent": 900, "dette": 0},
    {"nom": "Oncle Paul", "argent": 1000, "dette": 0},
    {"nom": "Chloe", "argent": 800, "dette": 0},
]

# Pour retrouver un client par son nom
def trouver_client(nom):
    for c in clients:
        if c["nom"] == nom:
            return c
    return None

# --- 2. LE JOURNALISTE ---
# C'est le decorateur impose par le tirage
# Il raconte chaque action comme un journaliste
def journaliste(fonction):
    def nouvelle_fonction(nom_client, *args):
        print("[Journaliste] :", fonction.__name__, "pour", nom_client)
        resultat = fonction(nom_client, *args)
        print("[Journaliste] : termine pour", nom_client)
        return resultat
    return nouvelle_fonction

# --- 3. LES 4 ACTIONS ---
@journaliste
def choisir_poste(nom_client):
    client = trouver_client(nom_client)
    print(nom_client, ": choisit un poste. 1 poste en panne, il reste 4 postes.")
    return 4

@journaliste
def gerer_connexion(nom_client):
    print(nom_client, ": connexion lente, on redemarre le routeur.")
    return 10

@journaliste
def vendre_credit(nom_client, montant):
    client = trouver_client(nom_client)
    print(nom_client, ": achete a credit", montant, ". Il promet de payer demain.")
    client["dette"] = client["dette"] + montant
    return montant

@journaliste
def relancer_client(nom_client):
    client = trouver_client(nom_client)
    if client["dette"] == 0:
        print(nom_client, ": n'a pas de dette, rien a relancer.")
        return 0
    print(nom_client, ": on le relance, il doit encore", client["dette"])
    # Il paie la moitie, il tarde pour le reste
    paye = client["dette"] // 2
    client["dette"] = client["dette"] - paye
    client["argent"] = client["argent"] - paye
    print(nom_client, ": paie", paye, ", il reste a payer", client["dette"])
    return paye

# --- 4. 30 JOURS, CHAQUE JOUR SA SITUATION ---
# On garde les 7 situations, et on les fait tourner sur 30 jours
# Jour 1 = Lundi, Jour 8 = Lundi, etc. C'est comme un vrai mois.

situations = [
    "Ouverture, tout marche",
    "1 poste en panne",
    "Connexion tres lente",
    "Papa Jean achete a credit",
    "On relance Papa Jean",
    "Beaucoup de monde, plus de poste libre",
    "Bilan de la semaine"
]

print("=== BIENVENUE AU CYBERCAFE D'ELMY ===")
print("Des tires : 6, 6, 2")
print("6 = bonne journee, 6 = beaucoup de clients, 2 = la panne qui gache tout")
print("")

total_gagne = 0

# On joue 30 jours
for numero_jour in range(1, 31):
    # Pour retrouver la situation du jour
    # Ex : jour 1 -> situation 0, jour 8 -> situation 0 aussi
    position = (numero_jour - 1) % 7
    situation = situations[position]

    print("======================================")
    print("JOUR", numero_jour, "-", situation)
    print("======================================")

    # Dimanche = bilan, on ne fait pas jouer les clients
    if position == 6:
        print("On ferme les postes, on compte.")
        print("")
        continue

    # Chaque jour, on prend 3 clients differents
    # On tourne dans la liste des clients
    clients_du_jour = []
    for i in range(3):
        indice = (numero_jour + i) % 10
        clients_du_jour.append(clients[indice]["nom"])

    for nom in clients_du_jour:
        print("")
        print("--- Client :", nom, "---")
        choisir_poste(nom)
        gerer_connexion(nom)

        # Si c'est le jour du credit et que c'est Papa Jean
        if situation == "Papa Jean achete a credit" and nom == "Papa Jean":
            vendre_credit(nom, 500)

        # Si c'est le jour de la relance et que c'est Papa Jean
        if situation == "On relance Papa Jean" and nom == "Papa Jean":
            gagne = relancer_client(nom)
            total_gagne = total_gagne + gagne

        if situation == "Beaucoup de monde, plus de poste libre":
            print("Trop de monde, on fait attendre", nom, "5 minutes.")

    print("")
# Chaque jour : nom du jour, situation, et les clients qui viennent ce jour-la
semaine = [
    {"jour": "Lundi", "situation": "Ouverture, tout marche", "clients": ["Chloe la nouvelle", "Sarah l'etudiante", "Oncle Paul", "Papa Jean"]},
    {"jour": "Mardi", "situation": "1 poste en panne", "clients": ["Kevin le gamer", "Oncle Paul", "Moussa le footballeur"]},
    {"jour": "Mercredi", "situation": "Connexion tres lente", "clients": ["Maman Aicha", "Lea la discrete", "Tatie Rose"]},
    {"jour": "Jeudi", "situation": "Papa Jean achete a credit", "clients": ["Papa Jean", "Tatie Rose", "Petit Yann"]},
    {"jour": "Vendredi", "situation": "On relance Papa Jean", "clients": ["Papa Jean", "Sarah l'etudiante", "Chloe la nouvelle"]},
    {"jour": "Samedi", "situation": "Beaucoup de monde, plus de poste libre", "clients": ["Kevin le gamer", "Moussa le footballeur", "Petit Yann", "Maman Aicha", "Oncle Paul"]},
    {"jour": "Dimanche", "situation": "Bilan de la semaine", "clients": []},
]

print("=== BIENVENUE AU CYBERCAFE D'ELMY ===")
print("Des tires : 6, 6, 2")
print("6 = bonne journee, 6 = beaucoup de clients, 2 = la panne qui gache tout")
print("")

total_gagne = 0

for jour_info in semaine:
    print("======================================")
    print(jour_info["jour"], "-", jour_info["situation"])
    print("======================================")

    # Dimanche = bilan, pas d'action
    if jour_info["jour"] == "Dimanche":
        print("On ferme les postes, on compte.")
        continue

    for nom in jour_info["clients"]:
        print("")
        print("--- Client :", nom, "---")
        choisir_poste(nom)
        gerer_connexion(nom)

        # Jeudi : Papa Jean prend a credit, les autres paient normalement
        if jour_info["jour"] == "Jeudi" and nom == "Papa Jean":
            vendre_credit(nom, 500)
        # Vendredi : on relance Papa Jean
        if jour_info["jour"] == "Vendredi" and nom == "Papa Jean":
            gagne = relancer_client(nom)
            total_gagne = total_gagne + gagne

        # Samedi : trop de monde, on doit choisir
        if jour_info["jour"] == "Samedi":
            print("Samedi : trop de monde, on fait attendre", nom, "5 minutes.")

    print("")

# --- 5. BILAN FINAL ---
print("=== BILAN FINAL DU DIMANCHE ===")
for c in clients:
    print(c["nom"], "- argent :", c["argent"], "- dette restante :", c["dette"])
    if c["dette"] > 0:
        print("  ->", c["nom"], "doit encore payer, on le relancera lundi.")

print("")
print("Total recupere grace aux relances :", total_gagne)
print("Semaine terminee. Merci d'etre venu au cybercafe d'Elmy !")