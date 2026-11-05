from pathlib import Path
from extraire import extraire_texte     # on récupère la fonction de l'autre fichier

for fichier in sorted(Path("textes_loi").glob("*.pdf")):
    texte = extraire_texte(fichier)
    print(f"{fichier.name:28} {len(texte):6} caractères")