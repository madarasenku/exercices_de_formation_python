from pathlib import Path

chemin = Path("/home/madara/Bureau/formation_python")

d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}


for cle , valeur in d.items() :
    for element in valeur:
        chemin_final = chemin / cle / element
        chemin_final.mkdir(exist_ok=True , parents=True)