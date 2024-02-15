import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

# Skapa ett tk-fönster "ruta" 
ruta = customtkinter.CTk()
ruta.geometry("363x786")
ruta.title("QuizApp")

# Ladda in assets
oliverAssets = "C:/Users/olive/Documents/Oliver skola/Python/Quizzapp/assets/" # Olivers mapp för assets
danielAssets = "?" #Daniels mapp för assets

Assets = oliverAssets #Ändra denna beroende på person

# Skapa ett canvas i 'ruta'
canvas = tk.Canvas(ruta, bg="#366990", width=363, height=786)
canvas.place(x=-2,y=-2)

# Rita in bakgrundsbild
background_img = tk.PhotoImage(file=Assets + "/background.png")
canvas.create_image(181,393,image=background_img)

# Rita in logga
logga_img = tk.PhotoImage(file=Assets + "/testlogga.png")
canvas.create_image(181,200,image=logga_img)

# Skriv ut text "Ditt namn: "
skriv_namn_text=customtkinter.CTkLabel(ruta, text="Ditt namn:", font=('Century Gothic', 14, "bold"), bg_color="#366990")
skriv_namn_text.place(x=35, y=410)

# Skapa en entryruta
text_namn = customtkinter.CTkEntry(ruta, placeholder_text="Daniel..", fg_color='#32638b', width=300, height=55, corner_radius=20, bg_color="#366990", border_color="#e9e9e9")
text_namn.place(relx=0.5, rely=0.6, anchor="center")

# Knappens funktion
def button_function():
    print("Start")

#Skapa knappen
button = customtkinter.CTkButton(ruta, command=button_function, text="Välj Ämne", text_color="#f2f2f2", font=('Century Gothic', 20, "bold"), fg_color='#F8C660', width=300, height=55, corner_radius=20, hover_color="#ffdb93", bg_color="#32638b")
button.place(x=31,y=600)

ruta.mainloop()