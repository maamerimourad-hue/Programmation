import pandas as pd
import tkinter as tk
import functions
import matplotlib.pyplot as plt
from tkinter import filedialog, messagebox, ttk
import matplotlib.pyplot as plt
from collections import Counter

# Global variable to store dataset
df = None
filtered=None
def load_csv():
    global df
    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select CSV File",
        filetypes=[("CSV files", "*.csv")]
    )

    if not file_path:
        return  # user cancelled

    try:
        df = pd.read_csv(file_path)
        messagebox.showinfo("Success", f"CSV file loaded successfully!\nRows: {len(df)}")
        # Optionally, display first few rows in the Treeview
        show_data(df)
    except Exception as e:
        messagebox.showerror("Error", f"Could not load file:\n{e}")

#afficher le DataFrame  df sur le Tree
def show_data(dataframe):
    # Clear previous rows
    for row in tree.get_children():
        tree.delete(row)

    tree["columns"] = list(dataframe.columns)
    tree["show"] = "headings"

    for col in dataframe.columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    # Insérer les premières lignes
    for _, row in dataframe.head(50).iterrows():  # affiche 50 lignes max
        tree.insert("", "end", values=list(row))


#plot de nombre de publication par Year
def visualize_Number_Year():
 global df
 pubs_per_year = df.groupby('year').size()
 plt.plot(pubs_per_year.index, pubs_per_year.values, marker='o')
 plt.title("Number of Publications per Year")
 plt.xlabel("year")
 plt.ylabel("count")
 plt.show()

# ---- pour visualiser les autheurs les plus active (10 par exemple)
def most_active_authors():
 authors = [a.strip() for sublist in df['authors'].str.split(',') for a in sublist]
 counter = Counter(authors)
 top_authors = counter.most_common(10)

 plt.barh([a[0] for a in reversed(top_authors)], [a[1] for a in reversed(top_authors)])
 plt.title("Top 10 Most Active Authors")
 plt.xlabel("Number of Publications")
 plt.show()

# appliquer des filtres sur nom, titre, venue , ou année de  DataFrame
# utilisant une variable globale filtred qui prend les resultas  afin
# qu'on puisse les sauvegaeder en fichier csv
def apply_filters():
    global df
    global filtered

    if df is None:
        messagebox.showwarning("Attention", "Chargez d'abord un fichier CSV.")
        return

    # Récupération des valeurs de recherche
    title = entry_title.get().strip()
    author = entry_author.get().strip()
    year = entry_year.get().strip()
    venue = entry_venue.get().strip()

    filtered = df.copy()

    # Appliquer les filtres seulement si champ non vide
    if title:
        filtered = filtered[filtered['title'].astype(str).str.contains(title, case=False, na=False)]
    if author:
        filtered = filtered[filtered['authors'].astype(str).str.contains(author, case=False, na=False)]
    if year:
        filtered = filtered[filtered['year'].astype(str).str.contains(year, case=False, na=False)]
    if venue:
        filtered = filtered[filtered['venue'].astype(str).str.contains(venue, case=False, na=False)]

    show_data(filtered)

# sauvegaeder le resultats filtré dans un file CSV.
def save_to_csv():
    global filtered
    filtered. to_csv('filtered_results.csv', index=False)

## appel de fonctions standardize_author(nom) et standardize_venue(venu) a partir de
## fichier fonctions (import functions)
def preprocessing():
    global df
    df['authors'] = df['authors'].apply(lambda x: ', '.join(functions.standardize_author(a) for a in x.split(',')))
    df['venue'] = df['venue'].apply(lambda x: functions.standardize_venue(x))
    show_data(df)
root = tk.Tk()
root.title("Explorateur de Publications Scientifiques")
root.geometry("1000x650")



# === Boutons ===
btn_load = tk.Button(root, text="📂 Charger un fichier CSV", command=load_csv, font=("Arial", 12))
btn_load.pack(pady=10)

# === Cadre de filtres ===
frame_filters = tk.Frame(root)
frame_filters.pack(pady=5)

tk.Label(frame_filters, text="Title:").grid(row=0, column=0, padx=5)
entry_title = tk.Entry(frame_filters, width=20)
entry_title.grid(row=0, column=1, padx=5)
## les labels
tk.Label(frame_filters, text="Author:").grid(row=0, column=2, padx=5)
entry_author = tk.Entry(frame_filters, width=20)
entry_author.grid(row=0, column=3, padx=5)

tk.Label(frame_filters, text="Year:").grid(row=1, column=0, padx=5)
entry_year = tk.Entry(frame_filters, width=20)
entry_year.grid(row=1, column=1, padx=5)

tk.Label(frame_filters, text="Venue:").grid(row=1, column=2, padx=5)
entry_venue = tk.Entry(frame_filters, width=20)
entry_venue.grid(row=1, column=3, padx=5)

## === positionnement des boutons ===

btn_Visualize = tk.Button(root, text="number_by_Year", command=visualize_Number_Year, font=("Arial", 12))
btn_Visualize.pack(side=tk.LEFT)
btn_Visualize1 = tk.Button(root, text="most_authors", command=most_active_authors, font=("Arial", 12))
btn_Visualize1.pack(side=tk.LEFT)
btn_preprocess = tk.Button(frame_filters, text="Preprocessing", command=preprocessing)
btn_preprocess.grid(row=3, column=1, columnspan=1, pady=5)
btn_filter = tk.Button(frame_filters, text="🔍 Appliquer les filtres", command=apply_filters)
btn_filter.grid(row=2, column=2, columnspan=1, pady=5)
btn_save = tk.Button(frame_filters, text="Suvegarder Resultats en CSV", command=save_to_csv)
btn_save.grid(row=3, column=3, columnspan=1, pady=5)

# === Table de données ===
frame_table = tk.Frame(root)
frame_table.pack(fill="both", expand=True)

scroll_y = tk.Scrollbar(frame_table, orient="vertical")
scroll_y.pack(side="right", fill="y")
scroll_x = tk.Scrollbar(frame_table, orient="horizontal")
scroll_x.pack(side="bottom", fill="x")

## l'objet treeview de l'affichage
tree = ttk.Treeview(
    frame_table,
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

scroll_y.config(command=tree.yview)
scroll_x.config(command=tree.xview)

scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
tree.pack(fill="both", expand=True)


root.mainloop()

