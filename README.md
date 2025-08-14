[README (1).md](https://github.com/user-attachments/files/21774273/README.1.md)
# Dépressiomètre ESP32

Ce projet open-source permet de mesurer et visualiser la pression d'admission d'un moteur thermique à l'aide d'un microcontrôleur ESP32 et d'un écran TFT.

## 📦 Matériel utilisé

Voici la liste du matériel nécessaire à la réalisation du projet :

| Numéro | Référence | Catégorie | Description | Quantité | Lien |
|--------|-----------|-----------|-------------|----------|------|
| A1 | ESP32-S3 | Microcontrôleur | Carte de développement Wi-Fi/Bluetooth | 1 | https://www.amazon.com/Espressif-ESP32-S3-DevKitC-1U-N8-Development-Board/dp/B0BX2MSCRT |
| A2 | ILI9488 TFT | Affichage | Écran TFT 3.5" SPI 480x320 | 1 | https://www.amazon.com/3-5inch-display-interface-ili9488-electronic/dp/B08C7NPQZR |
| A3 | XGZP6818A | Capteur de pression | Capteur absolu 0–700kPa analogique | 4 | https://www.digikey.com/en/products/detail/cfsensor/XGZP6818A00700KPA33/25807294 |
| A4 | MTX-L Plus | Capteur AFR | Capteur AFR Bosch LSU 4.9 analogique | 1 | https://www.innovatemotorsports.com/mtx-l-plus-digital-wideband-air-fuel-ratio-gauge-kit-3-ft.html |
| A5 | SD Module SPI | Stockage | Module carte SD externe SPI | 1 | https://www.amazon.com/Micro-Module-Arduino-ESP32-ESP8266/dp/B0D8HR7XCK |
| A6 | Bouton Ø8mm | Interface utilisateur | Bouton momentané à montage panneau | 4 | https://www.amazon.com/outstanding-Button-Switch-Momentary-DS-101/dp/B07ZV3PB26 |
| A7 | USB-C Panel Mount | Connectique | Connecteur USB-C à montage panneau | 1 | https://www.amazon.com/QIANRENON-Straight-Connector-Mounting-Extension/dp/B0CQ4VD2N2 |
| A8 | Insert M2.5 | Fixation | Insert fileté pour plastique | 4 | https://www.amazon.com/M2-5-Brass-Knurled-Insert-Threaded/dp/B07ZKZKJZJ |
| A9 | Connecteur AFR | Connectique | Prise pour capteur AFR analogique | 1 | https://www.amazon.com/Innovate-Motorsports-3844-Replacement-Sensor/dp/B00B4VZKZK |


## 🛠️ Fonctionnalités

- Acquisition de données de pression via capteurs analogiques
- Affichage en temps réel sur écran TFT
- Enregistrement des données sur carte SD
- Interface utilisateur avec boutons physiques
- Connectivité USB-C pour alimentation et communication

## 📐 Fichiers 3D

Les fichiers du boîtier sont disponibles aux formats :
- STL
- STEP
- OBJ
- 3MF
- DXF
- SLDPRT
- IPT

## ⚙️ Instructions de montage

1. Imprimer le boîtier en 3D
2. Insérer les composants selon le plan d’implantation
3. Connecter les capteurs et l’écran à l’ESP32
4. Charger le firmware sur l’ESP32
5. Tester l’affichage et la mesure

## 🔌 Schéma de câblage

Le schéma de câblage est disponible dans le dossier `docs/`.

## 🔗 Liens utiles

- [Documentation ESP32](https://docs.espressif.com/)
- [Librairie TFT ILI9488](https://github.com/Bodmer/TFT_eSPI)
- [CadQuery pour modélisation paramétrique](https://cadquery.readthedocs.io/)
