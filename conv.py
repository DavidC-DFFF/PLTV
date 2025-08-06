import os
import re

# Dossier des chapitres
dossier = r'V:\18 ans Gatien\PLTV\capitoli'
pattern_fichier = re.compile(r'chapitre(\d{2})\.html')

# Fonction pour ne garder qu'un seul paragraphe <p>...</p>
def garder_un_seul_paragraphe(contenu):
    balises = list(re.finditer(r'<p>.*?</p>', contenu, flags=re.DOTALL))
    if not balises:
        return contenu
    premier = balises[0]
    debut, fin = premier.start(), premier.end()
    # Remplacer le premier paragraphe par <p>...</p> et supprimer tous les autres
    avant = contenu[:debut]
    apres = contenu[fin:]
    apres_nettoye = re.sub(r'<p>.*?</p>', '', apres, flags=re.DOTALL)
    return avant + '<p>...</p>\n\n' + apres_nettoye

# Parcourir les fichiers dans le dossier
for nom_fichier in os.listdir(dossier):
    match = pattern_fichier.match(nom_fichier)
    if match:
        numero = match.group(1)
        ancien_chemin = os.path.join(dossier, nom_fichier)
        nouveau_nom = f'capitolo{numero}.html'
        nouveau_chemin = os.path.join(dossier, nouveau_nom)

        with open(ancien_chemin, 'r', encoding='utf-8') as f:
            contenu = f.read()

        # 1. Modifier <html lang="fr"> → <html lang="it">
        contenu = re.sub(r'<html lang="fr"', '<html lang="it"', contenu)

        # 2. Modifier le <title>
        contenu = re.sub(
            r'<title>.*?Chapitre\s*\d{2}</title>',
            f'<title>Prestami la tua voce – Capitolo {numero}</title>',
            contenu
        )

        # 3. Corriger les liens chapitreXX dans la navigation
        contenu = re.sub(
            r'href="chapitre(\d{2})\.html"',
            lambda m: f'href="capitolo{m.group(1)}.html"',
            contenu
        )

        # 4. Remplacer les <p> par un seul <p>...</p>
        contenu = garder_un_seul_paragraphe(contenu)

        # 5. Écrire le nouveau fichier
        with open(nouveau_chemin, 'w', encoding='utf-8') as f:
            f.write(contenu)

        # Supprimer l’ancien fichier
        os.remove(ancien_chemin)

        print(f'{nom_fichier} → {nouveau_nom} : transformé')

print('✅ Tous les chapitres ont été traités avec succès.')
