# Mon Quartier en 30 jours

Projet individuel – Programmation avancée en Python, Licence 2 Informatique.

Ce dépôt est **le vôtre** : vous seul et l'enseignant y avez accès.

## Lundi : mise en route

1. Créez un compte sur github.com et indiquez votre adresse à l'enseignant.
2. Installez Git (git-scm.com). Sous Windows, gardez les options par défaut.
3. Acceptez l'invitation reçue : votre dépôt privé apparaît dans votre compte.
4. Dans un terminal, indiquez qui vous êtes (une seule fois par ordinateur) :

       git config --global user.name "Prénom Nom"
       git config --global user.email "votre.adresse@exemple.com"

5. Clonez votre dépôt (l'adresse est sur la page du dépôt, bouton « Code ») :

       git clone ADRESSE_DE_VOTRE_DEPOT
       cd NOM_DU_DEPOT

6. Ajoutez votre nom et votre matricule en haut de `JOURNAL.md`, puis :

       git add JOURNAL.md
       git commit -m "Ajoute mon nom au journal"
       git push

   À votre premier `git push`, une fenêtre de connexion à GitHub s'ouvre : connectez-vous.

## Mardi : le tirage au dé

L'enseignant annonce un mot secret. Lancez, une seule fois :

    python de_projet.py

Puis enregistrez :

    git add .
    git commit -m "Tirage au dé"
    git push

Ne modifiez ni `tirage.json` ni la section « Mon tirage au dé » de `JOURNAL.md` :
l'enseignant peut vérifier votre tirage, et toute modification serait visible dans l'historique.

## Ensuite

Poussez votre travail régulièrement (au moins à chaque idée terminée).
Votre historique Git fait partie de votre note.

# Cybercafé d'Elmy - Comment j'ai fait
**Fichier principal :** `elmy_cybercafe.py`
**Tirage :** dés 6, 6, 2

## 1. Mon tirage 6, 6, 2
J'ai tiré les dés, j'ai eu 6, 6, 2.
- Mon activité : un cybercafé avec des postes
- Mon évènement : un client qui achète à crédit
- Ma contrainte : il faut un décorateur dans mon code

## 2. Mon fichier
J'ai créé mon fichier : `elmy_cybercafe.py`

## 3. La liste de mes clients
J'ai créé une liste avec 10 clients, avec leur nom et leur argent.
Exemple : Kévin, Maeva, Papa Jean...
C'est comme le carnet du cybercafé.

## 4. Mes petites fonctions
Chaque fonction fait UN seul travail :
- `choisir_poste()` : le client choisit un poste
- `gerer_connexion()` : on allume la connexion
- `vendre_credit()` : quand Papa Jean achète à crédit, on note sa dette
- `relancer_client()` : quand on le relance, il paie un peu

## 5. Le décorateur
J'ai fait un décorateur qui écrit dans le journal chaque fois qu'un client arrive.
C'est ma contrainte.

## 6. 30 jours de test
Au début, j'ai testé sur 7 jours. Après, j'ai fait tourner sur 30 jours.
Je n'ai pas réécrit 30 fois la même chose.
J'ai fait une boucle `for numero_jour in range(1, 31)` et j'ai fait tourner mes 7 situations avec `% 7`.
Chaque jour, on prend 3 clients différents.

## 7. Le bilan final
À la fin, on compte combien Papa Jean doit encore et combien on a gagné dans le mois.