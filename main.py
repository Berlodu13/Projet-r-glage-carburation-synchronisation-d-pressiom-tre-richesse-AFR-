
from machine import Pin, ADC, SPI, UART
import sdcard
import os
import time
import ili9488
import bluetooth
import network

# === Initialisation des capteurs de pression ===
capteurs = [ADC(Pin(i)) for i in (32, 33, 34, 35)]
for capteur in capteurs:
    capteur.atten(ADC.ATTN_11DB)  # Plage 0-3.6V

# === Initialisation du capteur AFR ===
uart_afr = UART(1, baudrate=9600, tx=Pin(17), rx=Pin(16))

# === Initialisation de l'écran TFT ILI9488 ===
spi = SPI(2, baudrate=40000000, polarity=0, phase=0, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
tft = ili9488.ILI9488(spi, cs=Pin(5), dc=Pin(2), rst=Pin(4))
tft.fill(ili9488.BLACK)
tft.text("Depressiometre ESP32", 10, 10, ili9488.WHITE)

# === Initialisation des boutons ===
boutons = [Pin(i, Pin.IN, Pin.PULL_UP) for i in (12, 13, 14, 15)]

# === Initialisation de la carte SD ===
sd_spi = SPI(1, baudrate=10000000, polarity=0, phase=0, sck=Pin(40), mosi=Pin(41), miso=Pin(39))
sd = sdcard.SDCard(sd_spi, Pin(38))
os.mount(sd, "/sd")

# === Initialisation Bluetooth/Wi-Fi ===
bt = bluetooth.BLE()
bt.active(True)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

# === Fonction de lecture des capteurs ===
def lire_pressions():
    return [capteur.read() for capteur in capteurs]

def lire_afr():
    if uart_afr.any():
        return uart_afr.readline().decode().strip()
    return "N/A"

# === Fonction d'enregistrement sur SD ===
def enregistrer_donnees(pressions, afr):
    try:
        with open("/sd/donnees.csv", "a") as f:
            ligne = "{},{},{},{},{}
".format(*pressions, afr)
            f.write(ligne)
    except Exception as e:
        print("Erreur SD:", e)

# === Fonction d'affichage ===
def afficher_donnees(pressions, afr):
    tft.fill_rect(0, 30, 320, 200, ili9488.BLACK)
    for i, p in enumerate(pressions):
        tft.text("Capteur {}: {}".format(i+1, p), 10, 40 + i*20, ili9488.GREEN)
    tft.text("AFR: {}".format(afr), 10, 140, ili9488.YELLOW)

# === Fonction d'autocalibration ===
def autocalibration():
    tft.text("Calibration en cours...", 10, 180, ili9488.CYAN)
    time.sleep(2)
    tft.text("Calibration terminee", 10, 200, ili9488.CYAN)

# === Boucle principale ===
def boucle_principale():
    tft.text("Appuyez sur un bouton", 10, 160, ili9488.WHITE)
    while True:
        pressions = lire_pressions()
        afr = lire_afr()
        afficher_donnees(pressions, afr)
        enregistrer_donnees(pressions, afr)

        # Gestion des boutons
        if not boutons[0].value():
            autocalibration()
        elif not boutons[1].value():
            tft.text("Mode Bluetooth", 10, 220, ili9488.MAGENTA)
        elif not boutons[2].value():
            tft.text("Mode Wi-Fi", 10, 240, ili9488.MAGENTA)
        elif not boutons[3].value():
            tft.text("Sauvegarde manuelle", 10, 260, ili9488.MAGENTA)
            enregistrer_donnees(pressions, afr)

        time.sleep(1)

# === Démarrage ===
boucle_principale()
