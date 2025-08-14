import cadquery as cq

# Dimensions générales
largeur = 120  # mm
hauteur = 80   # mm
profondeur = 35  # mm
epaisseur_paroi = 3  # mm

# Découpe écran TFT
ecran_largeur = 76
ecran_hauteur = 57
ecran_x = (largeur - ecran_largeur) / 2
ecran_y = hauteur - ecran_hauteur - 10

# Boutons
nb_boutons = 4
diametre_bouton = 8
espacement_boutons = 20
boutons_y = ecran_y - 20

# Capteurs sur face supérieure
diametre_capteur = 6
espacement_capteurs = 20

# Création du boîtier principal
boitier = cq.Workplane("XY").box(largeur, hauteur, profondeur)

# Creuser l'intérieur
boitier = boitier.faces(">Z").workplane().rect(largeur - 2 * epaisseur_paroi, hauteur - 2 * epaisseur_paroi).cutBlind(-profondeur + epaisseur_paroi)

# Découpe écran
boitier = boitier.faces(">Z").workplane(offset=-epaisseur_paroi).transformed(offset=(0, ecran_y - hauteur/2, 0)).rect(ecran_largeur, ecran_hauteur).cutBlind(-5)

# Boutons
start_x = -((nb_boutons - 1) * espacement_boutons) / 2
for i in range(nb_boutons):
    x = start_x + i * espacement_boutons
    boitier = boitier.faces(">Z").workplane(offset=-epaisseur_paroi).pushPoints([(x, boutons_y - hauteur/2)]).hole(diametre_bouton)

# Capteurs sur face supérieure
for i in range(4):
    x = -30 + i * espacement_capteurs
    boitier = boitier.faces(">Z").workplane(centerOption="CenterOfMass").pushPoints([(x, hauteur/2 - 5)]).hole(diametre_capteur)

# Trou capteur AFR à droite
boitier = boitier.faces(">Z").workplane(centerOption="CenterOfMass").pushPoints([(largeur/2 - 10, hauteur/2 - 5)]).hole(diametre_capteur)

# Trou USB-C en bas
boitier = boitier.faces("<Z").workplane(centerOption="CenterOfMass").center(0, -10).rect(12, 5).cutBlind(3)

# Export du modèle
cq.exporters.export(boitier, 'boitier_depressiometre.step')
cq.exporters.export(boitier, 'boitier_depressiometre.stl')
cq.exporters.export(boitier, 'boitier_depressiometre.3mf')
cq.exporters.export(boitier, 'boitier_depressiometre.obj')
