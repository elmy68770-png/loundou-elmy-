# calculs.py - Les calculs du cybercafe d'Elmy
# Tous les prix sont en FCFA, entiers, multiples de 5

def arrondi_5(montant):
    """Arrondit au multiple de 5 inferieur. Ex: 3352 -> 3350"""
    return (montant // 5) * 5

def remise(prix, pourcentage):
    """Calcule le prix apres remise, arrondi a 5 FCFA"""
    reduction = (prix * pourcentage) // 100
    return arrondi_5(prix - reduction)

def total(liste_prix):
    """Additionne une liste de prix et arrondit a 5 FCFA"""
    return arrondi_5(sum(liste_prix))