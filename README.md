# Vérification automatique de la conformité des contrats de microcrédit

Projet de stage (2 mois) à Microcred SA, institution de microfinance tunisienne.

**Objectif** : vérifier automatiquement qu'un contrat de microcrédit respecte la réglementation de l'ACM (Autorité de Contrôle de la Microfinance), et justifier chaque anomalie par une citation précise de l'article de loi concerné.

**Données** : aucune donnée de l'entreprise n'est utilisée. Les contrats sont générés de façon synthétique, avec des défauts injectés et tracés. Les règles viennent uniquement de textes publics de l'ACM.

## Structure du dépôt

| Dossier | Contenu |
|---|---|
| `semaine1/` | Exercices Python et grille des obligations réglementaires |
| `semaine2/` | Extraction, nettoyage et découpage des textes de loi, base `base_articles.json` |
| `textes_loi/` | Arrêtés (2012, 2016, 2018, 2025) et notes ACM n°12 et n°39 |

## Utilisation (semaine 2)

```
python -m venv .venv
.venv\Scripts\activate
pip install pdfplumber python-docx
python semaine2/construire_base.py
```

Le programme lit les textes de `textes_loi/` et écrit `semaine2/base_articles.json` (un article par entrée : nom, texte, source).

## Avancement

- [x] Semaine 1 : bases de Python, lecture des textes, grille des obligations
- [x] Semaine 2 : base d'articles de loi interrogeable
- [ ] Semaines 3 à 8 : générateur de contrats, règles, classifieur, citation par RAG, mesure des résultats
