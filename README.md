## Prerequis
nous avons utilisé pour cette application langage Python sous Pycharme
les bibliothèque utilisées sont **Tkinter**, **Pandas**, **Matplotlib**

 ## les fonctions de l'Application
 les fonctions utilisées dans cette application sont:
 1. **load_csv()**: Pour charger et afficher le fichier.csv dans une DataFrame 
 2. **show_data(dataframe)**: Pour afficher le DataFrame sur une composante Tree
 3. **apply_filters()**: Appliquer les filtres sur les titres, l'Autheur, l'Année et la venue
 4. **save_to_csv()**: Afin de sauvegarder les résultats filtrés dans un fichier.csv
 5. **preprocessing()**: Le prétratement des données concernant les noms d'auteurs, ou l'Avenue.

## L'Interface de l'Application 
![L'Interface génerale de l'Application](Interface_globale.png)

## Le chargement de fichier
Nous utilison l'instruction **_df = pd.read_csv(file_path)_** pour charger le fichier a partir d'un chmenin 
![le chargement de fichier CSV](load_succes.png)

## l'Affichage de fichier
Le fichier chrgé est affiché sur un composant Tree , le resultats sur l'image
![Affichage de fichier](tree_globale.png)

## pré-traiement de données:
consiste a par des Lettre
