## Prerequis
Nous avons utilisé pour cette application LE langage de programmation **Python 3.9** sous **Pycharme**
les bibliothèque utilisées sont **Tkinter**, **Pandas**, **Matplotlib**

 ## 1) les fonctions de l'Application
 les fonctions utilisées dans cette application sont:
 1. **load_csv()**: Pour charger et afficher le fichier.csv dans une DataFrame 
 2. **show_data(dataframe)**: Pour afficher le DataFrame sur une composante Tree.
 3. **apply_filters()**: Appliquer les filtres sur les titres, l'Autheur, l'Année et la venue.
 4. **save_to_csv()**: Afin de sauvegarder les résultats filtrés dans un fichier.csv.
 5. **preprocessing()**: Le prétratement des données concernant les noms d'auteurs, ou de l'Avenue.
 6. **standardize_author(name)**: Standardisation des noms par la première lettre de prénom suivi de nom.
 7. **standardize_venue(venue)**: Standarisation des venue par des abreviation commune.
 8. **visualize_Number_Year()**: Pour dessiner **line chart** montrant le nombre de publication par année.
 9. **most_active_authors()**: Pour dessiner en Horizontal **bar chart** montrant les 10 top auteurs actifs.


## 2) L'Interface de l'Application 
![L'Interface génerale de l'Application](Interface_Globale.png "L'Interface génerale de l'Application")

## 3) Le chargement de fichier  
Nous utilison l'instruction **_df = pd.read_csv(file_path)_** pour charger le fichier a partir d'un chmenin 
![le chargement de fichier CSV](load_succes.png "le chargement de fichier CSV")

## 3.1) Affichage de fichier  
Le fichier chrgé est affiché sur un composant **Treeview** , le resultats sur l'image
![Affichage de fichier](Tree_Globale.png)

## 4) Pré-traiement de données:
Consiste a remplacer les nome de l'auteur par la premieère Lettre de Prénom et aprés suivi par le Nom de l'autheur, concernant les venue en impliménte un dictionnaire des abreviation come suit:

la venue    | le formulair
--------- | -------------
'VLDB'  | VLD
'VLDB 2022'| VLDB
'VLDB Conference'| VLDB
'ICML Conference' |ICML
'SIGMOD Record' |SIGMOD
'SIGMOD Conference'|SIGMOD
'ACM Trans. Database Syst.'|ACM Trans

Et après en remplace les différentes variantes de mêmes noms par un seul formulaire suivant
le dictionnaire comme illustré dans le tableau ci-dessus.

![le Pré-traitement](preprocessing.png)

## 5) Appliquer des  filtres
Nous pouvons faire des recherche par nom , titre, année et venue , et pour cela nous utilisant ces instructions (exemple sur titre):  
```python
*_filtered = df.copy()_*  
*_filtered = filtered[filtered['title'].astype(str).str.contains(title, case=False, na=False)]_*
```
![la recherche par titre](partitle.png)   
### 5.1 ) Exemple de recherche par l'année 2003  
![la recherche par Année](year_2003.png)  

### 5.2 ) Exemple de recherch par (l'année 2002 et venue=VLDP)  aprés un prétraitement
![la recherche par Année et Venue](year%202002%20%2C%20VLDP.png)  


## 6) Sauvegarder les resultats filtrés
 Nous pouvons sauvegarder le resultats de filtrage dans un fichier.csv Grace à  l'instruction:    
 ```python
  **_filtered. to_csv('filtered_results.csv', index=False)_**
  ```
 ![Sauvegarde dans fichier CSV](Save_CVS.png "Sauvegarde dans fichier CSV")
 
## 7) Analyse et  Visualisation 
Nous montrons le reultats concerne le nombre de publication par année par un graphique linéair **(line chart)**  
```python
pubs_per_year = df.groupby('year').size()
plt.plot(pubs_per_year.index, pubs_per_year.values, marker='o')
```
![number par année](number_by_years.png)  


et Nous montrons le reultats concerne les autheurs les plus actif (exemple top 10) par un graphique à barres  **(bar chart)**
```python
 authors = [a.strip() for sublist in df['authors'].str.split(',') for a in sublist]
 counter = Counter(authors)
 top_authors = counter.most_common(10)
 plt.barh([a[0] for a in reversed(top_authors)], [a[1] for a in reversed(top_authors)])

![number par année](topMost_active.png)  
