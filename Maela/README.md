# Copier des fichiers entre l'ordinateur et une clé USB avec Python

## Description du projet
Ce projet propose deux scripts Python pour automatiser la copie de fichiers entre votre ordinateur et une clé USB détectée automatiquement.  
Il utilise Python 3, la bibliothèque `psutil` pour détecter les périphériques amovibles, et `shutil` pour effectuer les copies.

## Fichiers du projet

- **copie.py** :
  - Script principal pour copier un fichier de votre ordinateur vers une clé USB détectée.
  - Modifiez la variable `source_file` dans ce fichier pour indiquer le chemin du fichier à copier.
  - Le fichier sera copié dans un dossier `copies_pc` à la racine de la clé USB.

- **copie2.py** :
  - Script pour copier automatiquement tout le contenu d'une clé USB nouvellement insérée vers un dossier local `usb_copies` sur l'ordinateur.
  - À chaque détection d'une nouvelle clé USB, son contenu est copié dans un sous-dossier horodaté.

- **Pipfile** et **Pipfile.lock** :
  - Fichiers générés par Pipenv pour gérer les dépendances Python du projet (ici, `psutil`).
  - Ils assurent que l'environnement virtuel contient les bonnes versions des bibliothèques nécessaires.

- **mon_fichier.txt** :
  - Exemple de fichier à copier avec `copie.py`.

## Prérequis
- Python 3.13 ou supérieur
- Pipenv installé (`pip install pipenv`)

## Installation et utilisation

1. **Cloner ou copier ce dossier sur votre ordinateur.**
2. **Ouvrir un terminal dans le dossier du projet.**
3. **Installer les dépendances avec Pipenv :**
   ```powershell
   pipenv install
   ```

### Utilisation de `copie.py` (PC → USB)

1. **Modifier le chemin du fichier source dans `copie.py` :**
   - Remplacez la valeur de `source_file` par le chemin complet de votre fichier à copier.
2. **Brancher votre clé USB.**
3. **Lancer le script avec Pipenv :**
   ```powershell
   pipenv run python copie.py
   ```
   Le script détectera automatiquement la clé USB et copiera le fichier dans le dossier `copies_pc` à la racine de la clé.

### Utilisation de `copie2.py` (USB → PC)

1. **Lancer le script avec Pipenv :**
   ```powershell
   pipenv run python copie2.py
   ```
2. **Insérer une clé USB.**
   - Le script attend la détection d'une nouvelle clé USB et copie automatiquement tout son contenu dans un dossier `usb_copies/usb_copy_<nom>_<timestamp>` sur votre ordinateur.

## Remarques
- Les scripts sont prévus pour fonctionner sous Windows et Linux, mais la détection automatique de la clé USB dépend du système d'exploitation.
- Si vous rencontrez des problèmes de détection, vérifiez que votre clé USB est bien montée et reconnue par le système.
