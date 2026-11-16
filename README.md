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
