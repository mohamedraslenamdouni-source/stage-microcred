import re

def decouper_articles(texte, titre=None):
    """Découpe un texte de loi propre en articles.
    titre : une phrase du titre de l'arrêté ; tout ce qui est avant est ignoré."""
    articles = []
    actuel = {"article": "Préambule", "texte": ""}
    commence = titre is None                     # sans titre, on commence tout de suite

    for ligne in texte.split("\n"):
        if not commence:                         # on cherche encore le titre
            if titre in ligne:
                commence = True
                actuel["texte"] = ligne
            continue

        debut = re.match(r"(Article premier(?: \(nouveau\)| bis)?|Art\. \d+)", ligne)
        if debut:
            articles.append(actuel)
            actuel = {"article": debut.group(1), "texte": ligne}
        else:
            actuel["texte"] += " " + ligne
        if "sera publié au journal officiel" in ligne.lower():   # .lower() : majuscules ou minuscules
            break

    articles.append(actuel)
    return articles

if __name__ == "__main__":
    from extraire import extraire
    from nettoyer import nettoyer
    texte = nettoyer(extraire("textes_loi/arrete_2016_08_24.pdf"))
    articles = decouper_articles(texte)
    print(f"{len(articles)} morceaux trouvés")
    for a in articles:
        print(f"{a['article']:16} {a['texte'][:70]}")