from pathlib import Path

import pdfplumber
from docx import Document


def extraire_texte(chemin):
    """Ouvre un PDF en deux colonnes et renvoie son texte dans le bon ordre."""
    texte_complet = ""
    with pdfplumber.open(chemin) as pdf:
        for page in pdf.pages:
            milieu = page.width / 2
            gauche = page.crop((0, 0, milieu, page.height))          # moitié gauche
            droite = page.crop((milieu, 0, page.width, page.height)) # moitié droite
            for colonne in (gauche, droite):
                texte = colonne.extract_text()
                if texte:
                    texte_complet += texte + "\n"
    return texte_complet


def extraire_texte_docx(chemin):
    """Ouvre un fichier Word et renvoie tout son texte."""
    doc = Document(chemin)
    lignes = []
    for paragraphe in doc.paragraphs:
        lignes.append(paragraphe.text)
    return "\n".join(lignes)


def extraire(chemin):
    """Lit un PDF ou un Word : choisit la bonne fonction selon l'extension."""
    extension = Path(chemin).suffix.lower()
    if extension == ".pdf":
        return extraire_texte(chemin)
    elif extension == ".docx":
        return extraire_texte_docx(chemin)
    elif extension == ".txt":
        return Path(chemin).read_text(encoding="utf-8")
    else:
        raise ValueError(f"Format non géré : {extension}")


if __name__ == "__main__":
    print(extraire("semaine2/test_contrat.docx"))
    print(extraire("textes_loi/arrete_2016_08_24.pdf")[:300])