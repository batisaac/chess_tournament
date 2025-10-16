# Gestionnaire de Tournois d'Échecs

Programme simple pour gérer des tournois d'échecs, structuré selon le modèle MVC (`src/models/`, `src/views/`, `src/controllers/`).

## Prérequis
- Python 3.10+ recommandé
- Windows (testé) ou équivalent

## Installation (Windows / pip)
1. Cloner ce dépôt ou copier le dossier.
2. Créer un environnement virtuel:
   ```powershell
   python -m venv venv
   ```
3. Activer l'environnement:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
4. Installer les dépendances:
   ```powershell
   pip install -r requirements.txt
   ```

## Exécution de l'application
Lancer le programme principal:
```powershell
python main.py
```

## Linting et rapport Flake8 (PEP 8)
Le projet est configuré avec `.flake8` pour:
- une longueur de ligne maximale de 119 (`max-line-length = 119`)
- la génération d'un rapport HTML via `flake8-html` dans le dossier `flake8_rapport/`

Générer un rapport HTML à tout moment:
```powershell
python -m flake8 --max-line-length=119 --format=html --htmldir=flake8_rapport
```

Le rapport sera créé dans `flake8_rapport/index.html`. L'objectif est qu'il n'affiche **aucune erreur**.

## Structure du projet
```
chess_tournament/
├─ main.py
├─ requirements.txt
├─ .flake8
├─ src/
│  ├─ models/
│  ├─ views/
│  ├─ controllers/
│  └─ database/
└─ flake8_rapport/   (généré par flake8-html)