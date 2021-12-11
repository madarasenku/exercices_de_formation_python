"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""
from pprint import pprint
from pathlib import Path

chemin = (Path(__file__)).parent
chemin_fichier = chemin/"prenoms.txt"
chemin_fichier.touch()
chemin_fichier.write_text("""Charlotte, Raphaël,  Jade, Justin, Zoe Jeanne, Elsa
Mathis, Sara, David. Chloe, Ludovic, Nicolas, Léo, Mathieu, Charles, Apolline, Noemie, Heloïse, Anaïs, Philippe, Antoine, Lina, Laura
Pauline, Simon
Maxime, Victoire, Noah,
Emilie, Gabrielle, Louise, Nathan, Logan, Margaux, Clemence, Inès, Tommy, Isaac, Malik, Yasmine, Lena, Juliette, Eva, Elisa, Lisa, Salome, Ambre, Emma, Marie, Maya, Dylan, Mathilde, Noa, Christopher, Anna, Alexis, Elise, Guillaume, Adam, Alexandre, Victor, Sarah, Lou, Lucas, Lola, Victoria, Capucine, Jonathan, Clara, Camille, Lea, Félix, Gabriel, Cédric, Josephine, Alex, Sofia, Benjamin, Loïc, Thomas, Elliot, Romane, Agathe, Alix, Manon, Vincent, Alice, Samuel, Hugo, Diane, Julien, Jacob, Margot, Nina, Valentine, Rose, Jérémy, Julie, Anthony, Julia, Tristan
 Olivier, Louis, Adèle, Michaël, Lucie, """)
chemin_ouvert = chemin_fichier.read_text()
contenu = chemin_ouvert.splitlines()

prenoms =[]
for line in contenu:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]
chemin_fichier.write_text("\n".join(sorted(prenoms_final)))
    

