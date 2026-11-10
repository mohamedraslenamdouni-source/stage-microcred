import re

def est_entete(ligne):
    """Vrai si la ligne est un en-tête ou un pied de page du Journal Officiel."""
    return (ligne.startswith("Page ")
            or ligne.startswith("N° ")
            or "Journal Officiel de la République Tunisienne" in ligne
            or ligne.startswith("décrets")
            or ligne.startswith("t arrêtés")
            or ligne.startswith("et arrêtés")
            or ligne.startswith("Tunisienne —")
            or "Tunisienne —" in ligne
              )
              

def nettoyer(texte):
    # 1. Garder les lignes utiles
    lignes = []
    for ligne in texte.split("\n"):
        ligne = ligne.strip()                  # enlève les espaces au début et à la fin
        if ligne == "" or est_entete(ligne):
            continue                           # on saute cette ligne
        lignes.append(ligne)

    # 2. Recoller les phrases coupées
    paragraphes = []
    for ligne in lignes:
        if paragraphes and paragraphes[-1].endswith("-") :
            paragraphes[-1] += ligne           # mot coupé : on recolle sans espace
        elif (paragraphes
              and not paragraphes[-1].endswith((".", ":", ";"))
              and not ligne.startswith(("-", "Art", "Vu", "Arrêt"))):
            paragraphes[-1] += " " + ligne     # même phrase : on recolle avec un espace
        else:
            paragraphes.append(ligne)          # nouvelle phrase ou nouvel article
    texte = "\n".join(paragraphes)

    # 3. Corriger les erreurs de conversion
    texte = re.sub(r"\bl(?=\d)", "1", texte)   # un « l » collé à un chiffre devient « 1 »
    texte = re.sub(r" {2,}", " ", texte)       # plusieurs espaces deviennent un seul
    texte = re.sub(r"(\d)- (\d)", r"\1-\2", texte)   # « 2011- 117 » devient « 2011-117 »
    return texte

if __name__ == "__main__":
    from extraire import extraire_texte
    brut = extraire_texte("textes_loi/arrete_2016_08_24.pdf")
    propre = nettoyer(brut)
    print(propre[:1500])