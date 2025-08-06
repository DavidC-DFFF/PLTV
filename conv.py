import re

# Chemin vers navbar.html en version française
chemin_navbar = r'V:\18 ans Gatien\PLTV\navbar.html'

# Dictionnaire de traduction des titres
TRADUCTIONS = {
    "Préambule": "Preludio",
    "Quand tout bougeait": "Quando tutto si muoveva",
    "L’univers devient trop petit": "L’universo diventa troppo piccolo",
    "Le passage": "Il passaggio",
    "L’autre monde": "L’altro mondo",
    "La petite maidon": "La piccola casa",
    "Comme un souvenir d’avant": "Come un ricordo di prima",
    "Vers l’infini et à mon rythme": "Verso l’infinito e al mio ritmo",
    "Un monde encore plus merveilleux": "Un mondo ancora più meraviglioso",
    "Des murs plus hauts, mais les mêmes bras autour": "Muri più alti, ma le stesse braccia intorno",
    "Un nouveau refrain dans l’air": "Un nuovo ritornello nell’aria",
    "Un géant dans ses yeux": "Un gigante nei suoi occhi",
    "Et mon monde eût deux soleils": "E il mio mondo ebbe due soli",
    "Nonnu": "Nonnu",
    "La deuxième sortie": "La seconda uscita",
    "Le bâtonnet qui dansait": "Il bastoncino che danzava",
    "De l’autre côté de l’eau": "Dall’altra parte dell’acqua",
    "Des grains de sable sur les joues": "Granelli di sabbia sulle guance",
    "La terre qui me reconnaît": "La terra che mi riconosce",
    "Depuis la porte de la classe": "Dalla porta della classe",
    "Quand les cloches ont sonné": "Quando le campane hanno suonato",
    "Mon année invisible": "Il mio anno invisibile",
    "Il est mon lien": "È il mio legame",
    "Le prince des têtus": "Il principe dei testardi",
    "Quand le barrage commencer à céder": "Quando la diga inizia a cedere",
    "Une autre main sur le guidon": "Un’altra mano sul manubrio",
    "« Papa, regarde ! »": "« Papà, guarda! »",
    "La classe aux trois dames": "La classe con tre maestre",
    "L’école de l’autre côté": "La scuola dall’altra parte",
    "La mer, le sable et l’arbre aux pommes": "Il mare, la sabbia e l’albero delle mele",
    "Deux cent quarante kilomètres d’amour": "Duecentoquaranta chilometri d’amore",
    "Le spectacle": "Lo spettacolo",
    "Une maison à faire pousser": "Una casa da far crescere",
    "Un dressing pour deux": "Un armadio per due",
    "Une école pour chacun, une maison pour tous": "Una scuola per ciascuno, una casa per tutti",
    "Quatre cœurs qui battent pour moi": "Quattro cuori che battono per me",
    "Un aquarium pour chambre, un bateau dans le cœur": "Un acquario per stanza, una nave nel cuore",
    "Mon monde à bord": "Il mio mondo a bordo",
    "Back to Magic": "Ritorno alla Magia",
    "L’orage dans mes rêves": "La tempesta nei miei sogni",
    "Elle avait déjà la clé": "Aveva già la chiave",
    "Trois voyages, mille textures": "Tre viaggi, mille texture",
    "Le monstre dans ses poumons": "Il mostro nei suoi polmoni",
    "La graine de chaos": "Il seme del caos",
    "Refermer la boucle": "Chiudere il cerchio",
    "L’école de grands": "La scuola dei grandi",
    "Le monde en pause": "Il mondo in pausa",
    "Le sentier des cousins": "Il sentiero dei cugini",
    "Pédaler en confiance": "Pedalare con fiducia",
    "Nous ne sommes pas si différents": "Non siamo poi così diversi",
    "Le monde qui ne dort jamais": "Il mondo che non dorme mai",
    "Les petits singes": "Le scimmiette",
    "River camp": "Campo sul fiume",
    "Des corps différents, un même cœur": "Corpi diversi, un solo cuore",
    "Fondre goutte à goutte": "Sciogliersi goccia a goccia",
    "Trop vieux, trop jeune": "Troppo vecchio, troppo giovane",
    "Une forêt pour ma revanche": "Una foresta per la mia rivincita",
    "Là où j’ai brûlé, là où j’ai brillé": "Dove ho bruciato, dove ho brillato",
    "Épilogue : Les mots qu’il m’a donnés": "Epilogo: Le parole che mi ha dato",
}

# Charger navbar
with open(chemin_navbar, 'r', encoding='utf-8') as f:
    contenu = f.read()

# Transformer les chapitres
def remplacer_chapitre(match):
    numero = match.group(1)
    titre_fr = match.group(2).strip()
    titre_it = TRADUCTIONS.get(titre_fr, titre_fr)
    return f'<option value="capitol{numero}.html">{numero}. {titre_it}</option>'

contenu_modifié = re.sub(
    r'<option value="chapitre(\d{2})\.html">\d+\.\s(.*?)</option>',
    remplacer_chapitre,
    contenu
)

# Écrire dans un nouveau fichier
chemin_sortie = chemin_navbar.replace('navbar.html', 'navbar-it.html')
with open(chemin_sortie, 'w', encoding='utf-8') as f:
    f.write(contenu_modifié)

print("✅ navbar-it.html généré avec chapitres traduits et renommés.")
