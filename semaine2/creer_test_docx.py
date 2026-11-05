from docx import Document

doc = Document()                                  # un document Word vide
doc.add_heading("CONTRAT DE MICROCRÉDIT", level=1)   # un titre
doc.add_paragraph("Emprunteur : Amel Ben Salah")     # un paragraphe
doc.add_paragraph("Montant : 5 000 DT")
doc.add_paragraph("TEG : 26,2 %")
doc.save("semaine2/test_contrat.docx")            # on l'enregistre

print("Fichier créé : semaine2/test_contrat.docx")