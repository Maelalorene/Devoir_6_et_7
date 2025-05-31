#!/usr/bin/env python3
#script python qui copie le contenu d'une clé USB vers l'ordinateur
import psutil
import shutil
import os
import time

# Répertoire de destination (à adapter si besoin)
DESTINATION_FOLDER = r"usb_copies"

# Crée le dossier de destination s'il n'existe pas
if not os.path.exists(DESTINATION_FOLDER):
    os.makedirs(DESTINATION_FOLDER)

# Fonction pour copier les fichiers
def copy_usb_contents(drive_letter):
    source_path = drive_letter + ":\\"
    usb_name = os.path.basename(os.path.normpath(source_path))
    dest_path = os.path.join(DESTINATION_FOLDER, f"usb_copy_{usb_name}_{int(time.time())}")
    try:
        shutil.copytree(source_path, dest_path)
        print(f"Contenu de {source_path} copié vers {dest_path}")
    except Exception as e:
        print(f"Erreur lors de la copie : {e}")

# Liste des lecteurs connus (initiale)
known_drives = set(part.device for part in psutil.disk_partitions())

print("En attente d'une clé USB...")

while True:
    time.sleep(2)
    current_drives = set(part.device for part in psutil.disk_partitions())
    new_drives = current_drives - known_drives

    for drive in new_drives:
        try:
            if 'removable' in psutil.disk_usage(drive)._fields:  # pas très fiable, on préfère une vérification simple :
                print(f"Nouvelle clé détectée : {drive}")
                copy_usb_contents(drive.strip("\\"))
                known_drives = current_drives
        except Exception as e:
            print(f"Erreur de détection : {e}")
            continue