[README.md](https://github.com/user-attachments/files/21774198/README.md)
# Dépressiomètre ESP32

Ce projet open-source vise à concevoir un **dépressiomètre numérique** basé sur un microcontrôleur **ESP32-S3**, permettant de mesurer et d'afficher les pressions dépressives dans un système automobile ou industriel.

## 🚀 Fonctionnalités

- Affichage des pressions sur écran TFT 3.5" ILI9488
- Lecture de 4 capteurs de pression analogiques XGZP6818A
- Intégration d’un capteur AFR MTX-L Plus
- Sauvegarde des données sur carte SD
- Interface utilisateur avec 4 boutons
- Connectivité USB-C pour alimentation et communication
- Boîtier imprimable en 3D avec inserts filetés

## 🧰 Matériel utilisé

Voici la liste du matériel nécessaire à la réalisation du projet :

- A1
- A2
- A3
- A4
- A5
- A6
- A7
- A8
- A9

## 🧱 Fichiers 3D

Le boîtier du dépressiomètre est modélisé en 3D et disponible aux formats suivants :

- STL
- STEP
- OBJ
- 3MF
- DXF
- SLDPRT
- IPT

👉 Les fichiers sont téléchargeables via les liens fournis dans le dépôt ou dans la section [Releases](https://github.com/ton-repo/releases).

## 🛠️ Instructions de montage

1. Imprimer le boîtier en 3D (épaisseur des parois : 3 mm)
2. Fixer l’écran TFT sur la face avant (découpe : 76 x 57 mm)
3. Insérer les 4 boutons Ø8 mm sous l’écran
4. Monter les capteurs de pression sur la face supérieure (Ø6 mm)
5. Intégrer le capteur AFR à droite
6. Fixer la carte ESP32-S3 à l’intérieur
7. Connecter la carte SD et le port USB-C
8. Fermer le boîtier avec les vis M2.5 dans les inserts filetés

## 📐 Schéma de câblage

Le câblage complet est disponible dans le fichier PDF `Plans_Boitier_Depressiometre_ESP32_Cotes_Complets (1).pdf` avec les dimensions et emplacements des composants.

## 📎 Liens utiles

- [Documentation ESP32-S3](https://www.espressif.com/en/products/socs/esp32-s3)
- [Datasheet XGZP6818A](https://www.sensorsportal.com)
- [TFT ILI9488 Library](https://github.com/Bodmer/TFT_eSPI)
- [CadQuery pour modélisation paramétrique](https://cadquery.readthedocs.io)

---

© Projet développé par Laurent. Contributions bienvenues !
