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

# Startknappens funktion
def buttonStart_function():
    print("Start")

# Amne1 knappens funktion
def buttonAmne1_function():
    print("Start")

# Amne2 knappens funktion
def buttonAmne2_function():
    print("Start")

# Amne3 knappens funktion
def buttonAmne3_function():
    print("Start")

# Amne4 knappens funktion
def buttonAmne4_function():
    print("Start")


#Skapa knapp för ämne 1
buttonAmne1 = customtkinter.CTkButton(ruta, command=buttonAmne1_function, text="Ämne 1", text_color="#383838", font=('Century Gothic', 20, "bold"), fg_color='#f0f0f0', width=120, height=80, corner_radius=20, hover_color="#ffdb93", bg_color="#32638b")
buttonAmne1.place(x=45,y=350)

#Skapa knapp för ämne 2
buttonAmne2 = customtkinter.CTkButton(ruta, command=buttonAmne2_function, text="Ämne 2", text_color="#383838", font=('Century Gothic', 20, "bold"), fg_color='#f0f0f0', width=120, height=80, corner_radius=20, hover_color="#ffdb93", bg_color="#32638b")
buttonAmne2.place(x=192,y=350)

#Skapa knapp för ämne 3
buttonAmne3 = customtkinter.CTkButton(ruta, command=buttonAmne3_function, text="Ämne 3", text_color="#383838", font=('Century Gothic', 20, "bold"), fg_color='#f0f0f0', width=120, height=80, corner_radius=20, hover_color="#ffdb93", bg_color="#32638b")
buttonAmne3.place(x=45,y=450)

#Skapa knapp för ämne 4
buttonAmne4 = customtkinter.CTkButton(ruta, command=buttonAmne4_function, text="Ämne 4", text_color="#383838", font=('Century Gothic', 20, "bold"), fg_color='#f0f0f0', width=120, height=80, corner_radius=20, hover_color="#ffdb93", bg_color="#32638b")
buttonAmne4.place(x=192,y=450)

#Skapa startknappen
buttonStart = customtkinter.CTkButton(ruta, command=buttonStart_function, text="Start", text_color="#f2f2f2", font=('Century Gothic', 20, "bold"), fg_color='#F8C660', width=300, height=55, corner_radius=20, hover_color="#ffdb93", bg_color="#32638b")
buttonStart.place(x=31,y=600)




ruta.mainloop()