import qrcode
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
import os
import sys

def resou(relaive_path):
    if getattr(sys, 'frozen', False):
        base_path=sys._MEIPASS
    else:
        base_path=os.path.abspath(".")
    return os.path.join(base_path, relaive_path)

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue") 

Test = ctk.CTk()
Test.title("QRCode Tools")
Test.geometry("800x500")
Test.resizable(False, False)

# Supprimer ou commenter cette ligne si tu ne veux pas de logo
# icon=resou("logo.ico")
# Test.iconbitmap(resou("logo.ico"))

# Fonction pour générer un QR Code
def generate_qr():
    data = entrez.get()
    if not data:
        messagebox.showerror("Erreur", "Entrez un texte ou un lien !")
        return
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qr_code.png")
    display_qr(img)

# Fonction pour afficher le QR Code
def display_qr(img):
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.configure(image=img_tk)
    qr_label.image = img_tk

# Fonction pour sauvegarder le QR Code
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        img = Image.open("qr_code de QrTools.png")
        img.save(file_path)
        messagebox.showinfo("Succès", f"QR Code enregistré sous {file_path}")

# Fonction pour ouvrir une image QR Code
def open_qr_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
    if file_path:
        scan_qr_code(file_path)

# Fonction pour scanner un QR Code
def scan_qr_code(image_path):
    img = Image.open(image_path).convert("RGB")
    img_np = np.array(img)

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img_np)
    
    if bbox is not None:
        bbox = bbox.astype(int)  # Convertir en entiers pour éviter l'erreur
        for i in range(len(bbox[0])):  
            point1 = tuple(bbox[0][i])  
            point2 = tuple(bbox[0][(i + 1) % len(bbox[0])])  
            cv2.line(img_np, point1, point2, (0, 255, 0), 2)

        # Affichage de l'image avec le cadre (optionnel)
        display_qr(Image.fromarray(img_np))

    if data:
        result_text.configure(state="normal")
        result_text.delete(0, "end")
        result_text.insert(0, data)
        result_text.configure(state="readonly")
    else:
        messagebox.showerror("Erreur", "Aucun QR Code détecté.")
    

# Label d'entrée
ctk.CTkLabel(Test, text="Generateur de Code QR", font=("Showcard Gothic", 20)).pack(pady=10)

# Champ de texte
entrez = ctk.CTkEntry(Test, font=("Arial", 14), width=300, placeholder_text="Entrez un texte ou un lien")
entrez.pack(pady=5)

# Création des boutons arrondis
def create_button(text, command, y):
    btn = ctk.CTkButton(Test, text=text, command=command, width=200, height=50, corner_radius=30, font=("Rockwell", 15))
    btn.place(x=40, y=y)

create_button("Générer QR Code", generate_qr, 150)
create_button("Enregistrer QR Code", save_qr, 220)
create_button("Scanner QR Code", open_qr_image,290)

# Affichage du QR Code généré
qr_frame = ctk.CTkFrame(Test, width=200, height=200, fg_color="white", corner_radius=10)
qr_frame.place(x=500, y=150)
qr_label = ctk.CTkLabel(qr_frame, text="")
qr_label.place(relx=0.5, rely=0.5, anchor="center")

# Champ pour afficher le texte du QR Code scanné
result_text = ctk.CTkEntry(Test, font=("Arial", 14), width=300, state="readonly")
result_text.place(x=450, y=360)

# Bouton pour quitter
quit_button = ctk.CTkButton(Test, text="Quitter", command=Test.quit, fg_color="red", hover_color="darkred", corner_radius=30, font=("Copperplate Gothic Bold", 16))
quit_button.place(x=350, y=450)


Test.mainloop()

