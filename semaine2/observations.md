# Observations - semaine 2 (extraction des textes)

## Problèmes rencontrés
- Pages du Journal Officiel en deux colonnes : les lignes se mélangeaient. Solution : `page.crop` en deux moitiés.
- Titre « décrets et arrêtés » coupé par le crop : traité dans `est_entete`.
- En-têtes et pieds de page (Page, N°, Journal Officiel, Tunisienne —) à supprimer.
- Une page du Journal Officiel contient plusieurs textes : le découpage s'ancre sur le titre de l'arrêté (`TITRES`).
- Tableau de la Santé collé à l'Art. 5 de 2025 : coupé avec `COUPURES`.
- Les notes ACM 12 et 39 sont des scans (aucun texte lisible) : transcrites à la main en `.txt`.
- Word : `doc.paragraphs` ne lit pas les tableaux.
- Fautes de lecture possibles : « l0.000 », « 2011- 117 » (corrigées par regex).

## Points de vigilance pour la suite
- L'arrêté 2018 remplace l'article premier de 2012 : les plafonds valides sont 10 000 / 40 000 DT (pas 5 000 / 20 000).
- « Article premier » existe dans plusieurs fichiers : c'est le champ `source` qui les distingue.
- Les notes n'ont pas d'articles : découpées par « Section I, II... ».
- Les 9 catégories de TEG viennent de la note 12, section III.
- L'IRA est plafonnée au plus faible de 2 % du capital restant dû et des intérêts de la prochaine échéance (note 39, section III).
