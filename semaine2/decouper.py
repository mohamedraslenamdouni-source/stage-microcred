import re

def decouper_articles(texte):
    """Découpe un texte de loi propre en une liste d'articles."""
    articles = []
    actuel = {"article": "Préambule", "texte": ""}

    for ligne in texte.split("\n"):
        debut = re.match(r"(Article premier|Art\. \d+)", ligne)   # la ligne commence-t-elle un article ?
        if debut:
            articles.append(actuel)                               # on range l'article précédent
            actuel = {"article": debut.group(1), "texte": ligne}  # et on en commence un nouveau
        else:
            actuel["texte"] += " " + ligne                        # sinon, la ligne continue l'article en cours
        if "sera publié au Journal Officiel" in ligne:
            break                                                 # fin de l'arrêté : on s'arrête là

    articles.append(actuel)                                       # on range le tout dernier article
    return articles

if __name__ == "__main__":
    from extraire import extraire
    from nettoyer import nettoyer
    texte = nettoyer(extraire("textes_loi/arrete_2016_08_24.pdf"))
    articles = decouper_articles(texte)
    print(f"{len(articles)} morceaux trouvés")
    for a in articles:
        print(f"{a['article']:16} {a['texte'][:70]}")