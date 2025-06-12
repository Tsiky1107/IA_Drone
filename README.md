# IA_Drone – Détection de Marquages et de Feuilles de Plantes Mortes

## Description

IA_Drone est un projet de vision par ordinateur permettant la détection automatique de marquages au sol et de feuilles mortes sur des plantes. Ce système utilise Python pour le traitement d’image (avec YOLOv8 et OpenCV) et communique avec une carte Arduino via le port série afin d’exécuter des actions ou stocker des informations pertinentes.

L’objectif est d’automatiser l'analyse des images capturées par une caméra et de transmettre les détections à l’Arduino pour prise de décision.

## Fonctionnalités

- Détection des marquages et feuilles mortes à l'aide d'un modèle YOLOv8 personnalisé.
- Interface graphique (Tkinter) pour la configuration et l'affichage des résultats en temps réel.
- Communication série avec une carte Arduino pour transmettre les détections.
- Traitement vidéo en direct avec OpenCV.
- Possibilité d'entraînement d'un modèle YOLOv8 personnalisé.

## Dépendances

Assurez-vous d'installer les bibliothèques suivantes avant d'exécuter le projet :

```bash
pip install ultralytics opencv-python pyserial tk
