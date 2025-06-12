IA_drone - Détection de Marquage et Feuilles de Plantes Mortes

📌 Description

Ce projet implémente un modèle de vision par ordinateur pour détecter des marquages et des feuilles de plantes mortes. Il utilise Python pour le traitement d'image et la communication avec une carte Arduino via le port série.

L'objectif est d'automatiser l'analyse d'images capturées par une caméra et d'envoyer des informations pertinentes à l'Arduino pour une éventuelle action ou stockage des données.

🛠️ Fonctionnalités

Détection des marquages et feuilles mortes à l'aide d'un modèle d'IA (YOLO).

Interface graphique (Tkinter) pour configurer et afficher les résultats.

Communication série avec l'Arduino pour transmettre les détections.

Traitement d'images en temps réel avec OpenCV.

Possibilité d'entraîner un modèle personnalisé.


📦 Dépendances

Assurez-vous d'installer les bibliothèques suivantes avant d'exécuter le projet :

pip install ultralytics opencv-python pyserial tkinter

🚀 Installation et Exécution

1. Clonez le dépôt :

git clone https://github.com/IA_drone
cd IA_drone


2. Connectez l'Arduino à votre PC via USB et notez le port série (ex: COM3 sous Windows ou /dev/ttyUSB0 sous Linux).


3. Lancez le programme principal :

python _Interface drone/main.py


4. Utilisation :

L'interface affichera la capture vidéo en direct.

Lorsque le modèle détecte une feuille morte ou un marquage, l'information est envoyée à l'Arduino via le port série.

L'Arduino peut ensuite déclencher une action en fonction des données reçues.




📂 Structure du Projet

/projet_detection
│── _Interface drone/                  # Interface principale
│   │── main.py                 # Programme principal
│   └── App/                    # Gestion de l'application
│       │── app.py            # Fichier de configuration et chargement du modèle YOLO
│── python_to_c++/                     # Code Arduino
│   │── arduino_code.ino         # Script Arduino
│── train/                        # Entraînement du modèle
│   │── train.py                 # Script d'entraînement YOLO
│   │── yolov8n.pt               # Modèle YOLO entraîné
│   └── datasets/                # Données d'entraînement
│── README.md                    # Documentation du projet

🔧 Configuration de l'Arduino

Un script Arduino doit être chargé sur la carte pour recevoir et traiter les données du port série. Exemple minimal en Arduino C++ :

void setup() {
    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        String data = Serial.readStringUntil('\n');
        Serial.println("Reçu: " + data);
    }
}

📌 Entraînement du Modèle

Si vous souhaitez entraîner un modèle personnalisé, placez vos images et annotations dans le dossier train/datasets/ ou décompresser le datasets.rar, puis exécutez :

python train/train.py

Le modèle entraîné sera sauvegardé sous runs/detect/model drone agri v** ou personnalisé la paramètres name et pourra être utilisé dans l'application.

📌 Améliorations Futures

Optimisation du modèle pour de meilleures performances.

Ajout d'une base de données pour stocker les résultats.

Intégration d'alertes visuelles ou sonores via l'Arduino.


👥 Collaborateurs

Nous accueillons toutes les contributions ! Voici les personnes ayant contribué à ce projet :

_ RAZANAKOLONA Joanna Tsiafoy

_ FIFALIANASOA Aina Nomenjanahary

- RAKOTONDRANAIVO Tsiory Mihajanirina

- FANOMEZANTSOA Aina Fitiavana

_ANDRIANTOVOSOA Aina Harentsoa

_RASEHENONJATOVO Ndranto Maël

_RAVALISON Tsiky Andriantia


Si vous souhaitez contribuer, n'hésitez pas à faire un pull request ou à nous contacter.

📜 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier.

✉️ Contact

Pour toute question ou amélioration, contactez-nous :

_ fanmetsoaina2@gmail.com

_ tsikyandriantia@gmail.com

_ tsiorymihajanirina@gmail.com

