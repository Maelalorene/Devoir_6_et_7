#!/usr/bin/env python3
#Script python pour copier un fichier de l'ordinateur vers une clé USB
import psutil
import shutil
import os

# Chemin complet du fichier source à copier (à modifier selon ton fichier)
source_file = r"./mon_fichier.txt"

# Fonction pour trouver la lettre du lecteur USB (lecteur amovible)
def find_usb_drive():
    partitions = psutil.disk_partitions()
    for p in partitions:
        print(f'{p}\n')
        if 'removable' in p.opts:
            return p.device  # Exemple : 'E:\\'
    return None

def copy_file_to_usb():
    usb_drive = find_usb_drive()
    if usb_drive is None:
        print("Aucune clé USB détectée.")
        return
    
    # Construire le chemin de destination : copie dans la racine de la clé USB
    destination_file = os.path.join(f'{usb_drive}/copies_pc', os.path.basename(source_file))
    
    try:
        shutil.copy2(source_file, destination_file)
        print(f"Fichier copié avec succès vers {destination_file}")
    except Exception as e:
        print(f"Erreur lors de la copie : {e}")

if __name__ == "__main__":
    copy_file_to_usb()