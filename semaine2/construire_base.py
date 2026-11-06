import json
from pathlib import Path

from extraire import extraire
from nettoyer import nettoyer
from decouper import decouper_articles

base = []
for fichier in sorted(Path("textes_loi").glob("*.pdf")):
    texte = nettoyer(extraire(fichier))
    if texte.strip() == "":
        print(f"{fichier.name:28} ignoré (scan sans texte)")
        continue
    articles = decouper_articles(texte)
    for a in articles:
        a["source"] = fichier.name        # on note de quel texte vient l'article
        base.append(a)
    print(f"{fichier.name:28} {len(articles)} morceaux")

with open("semaine2/base_articles.json", "w", encoding="utf-8") as f:
    json.dump(base, f, ensure_ascii=False, indent=2)

print(f"{len(base)} articles enregistrés dans semaine2/base_articles.json")