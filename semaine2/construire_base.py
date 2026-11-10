import json
from pathlib import Path

from extraire import extraire
from nettoyer import nettoyer
from decouper import decouper_articles
TITRES = {
    "arrete_2012_01_18.pdf": "18 janvier 2012, relatif à la fixation",
    "arrete_2016_08_24.pdf": "Arrêté du ministre des finances du 24 août 2016",
    "arrete_2018_04_13.pdf": "Arrêté du ministre des finances du 13 avril 2018",
    "arrete_2025_12_26.pdf": "26 décembre 2025, fixant un plafond",
}
COUPURES = {"arrete_2025_12_26.pdf": " Prénom et nom Grade"} 

base = []
for fichier in sorted(Path("textes_loi").glob("*.pdf")):
    texte = nettoyer(extraire(fichier))
    if texte.strip() == "":
        print(f"{fichier.name:28} ignoré (scan sans texte)")
        continue
    articles = decouper_articles(texte, TITRES.get(fichier.name))
    if len(articles) <= 1:
        print(f"ATTENTION : titre introuvable dans {fichier.name}")
    coupure = COUPURES.get(fichier.name)
    for a in articles:
        a["source"] = fichier.name
        if coupure:
            a["texte"] = a["texte"].split(coupure)[0].strip()       # on note de quel texte vient l'article
        base.append(a)
    print(f"{fichier.name:28} {len(articles)} morceaux")

with open("semaine2/base_articles.json", "w", encoding="utf-8") as f:
    json.dump(base, f, ensure_ascii=False, indent=2)

print(f"{len(base)} articles enregistrés dans semaine2/base_articles.json")