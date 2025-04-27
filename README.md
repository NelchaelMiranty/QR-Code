# QRCode Tools

QRCode Tools est une application graphique développée en Python, permettant de générer, scanner et enregistrer des codes QR. Cette application offre une interface utilisateur intuitive et moderne utilisant la bibliothèque CustomTkinter.

## Fonctionnalités

- **Génération de Code QR** : Crée des codes QR à partir de textes ou de liens.
- **Scanner un Code QR** : Permet de scanner un code QR à partir d'une image.
- **Sauvegarde de Code QR** : Sauvegarde les QR Codes générés dans un fichier image.
- **Interface utilisateur moderne** : Conçu avec CustomTkinter et une apparence en mode sombre.

## Prérequis

Avant d'exécuter ce programme, vous devez installer les bibliothèques suivantes :

- [qrcode](https://pypi.org/project/qrcode/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [Pillow](https://pypi.org/project/Pillow/)
- [OpenCV](https://pypi.org/project/opencv-python/)
- [NumPy](https://pypi.org/project/numpy/)

Tu peux installer ces dépendances avec `pip` en utilisant la commande suivante :

```bash
pip install qrcode[pil] customtkinter pillow opencv-python numpy
