# 📄 OCR Pipeline – PDF vers DOCX (Arabe Supporté)

Application Web permettant de convertir des fichiers **PDF scannés** en fichiers **Word (.docx)** en utilisant **Tesseract OCR**, **Flask**, **Celery** et **Redis**.

Le projet supporte l’extraction de texte arabe et génère automatiquement un document Word propre.

---

## 🚀 Fonctionnalités

- 📥 Upload de fichiers PDF
- 🔍 Extraction OCR (Tesseract)
- 🌍 Support langue arabe
- 📄 Génération automatique de fichier DOCX
- ⚙️ Traitement asynchrone avec Celery
- 🔄 Gestion de file d’attente via Redis

---

## 🏗️ Architecture

Flask (Web App)  
⬇  
Celery (Task Queue)  
⬇  
Redis (Broker & Backend)  
⬇  
Tesseract OCR  
⬇  
python-docx (Génération Word)

---

## 🛠️ Technologies utilisées

- Python 3.10+
- Flask
- Celery
- Redis
- Tesseract OCR
- pdf2image
- pytesseract
- python-docx
- Pillow

---

## 📂 Structure du projet

```
ocr_pipeline/
│
├── app/
│   ├── app.py
│   ├── tasks.py
│   ├── ocr_utils.py
│   ├── config.py
│   ├── templates/
│   ├── uploads/
│   └── results/
│
├── venv/
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/TON-USERNAME/ocr-pipeline.git
cd ocr-pipeline
```

### 2️⃣ Créer un environnement virtuel

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

Si requirements.txt n’existe pas :

```bash
pip install flask celery redis pdf2image pytesseract python-docx pillow
```

### 4️⃣ Installer Tesseract OCR

Télécharger et installer Tesseract :  
https://github.com/tesseract-ocr/tesseract

Puis vérifier :

```bash
tesseract --version
```

Dans config.py, vérifier le chemin :

```
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 5️⃣ Installer et lancer Redis (Windows)

Télécharger Redis pour Windows.

Puis lancer :

```bash
redis-server
```

Vérifier :

```bash
redis-cli ping
```

Réponse attendue :

```
PONG
```

---

## ▶️ Lancer l’application

### 1️⃣ Lancer Celery (IMPORTANT sous Windows)

```bash
cd app
celery -A tasks.celery worker --loglevel=info --pool=solo
```

### 2️⃣ Lancer Flask

Dans un autre terminal :

```bash
cd app
python app.py
```

### 3️⃣ Ouvrir dans le navigateur

```
http://localhost:5000
```

---

## 🔄 Workflow

Upload d’un PDF

Création d’une tâche Celery

Conversion PDF → Images

OCR via Tesseract

Nettoyage du texte

Génération DOCX

Téléchargement du fichier

---

## ⚠️ Notes importantes

Sous Windows, utiliser --pool=solo pour Celery

Redis doit être lancé avant Celery

Les fichiers générés sont stockés dans /results

---

## 📌 Exemple de sortie

```
Task succeeded in 52s: {'docx': 'output.docx'}
```

---

## 📈 Améliorations possibles

Barre de progression

Interface plus moderne (Bootstrap)

Déploiement cloud (Render / Railway)

Support multi-langue

Amélioration qualité OCR

---

## 👨‍💻 Auteur

Projet réalisé par ISMAIL  
Projet personnel – OCR Pipeline avec traitement asynchrone

---

## 📄 Licence

Projet open-source à but éducatif.

---

Si tu veux, je peux aussi :

- ✅ te générer le `requirements.txt`
- ✅ t’écrire le `.gitignore`
- ✅ t’écrire un README plus professionnel pour recruteurs
- ✅ optimiser la description pour LinkedIn
- ✅ t’aider à faire un commit propre avec messages professionnels

Dis-moi ce que tu veux faire ensuite.

