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
background_img = tk.PhotoImage(file=Assets + "/leaderboardbackground.png")
canvas.create_image(181,393,image=background_img)

# Rita in krona
logga_img = tk.PhotoImage(file=Assets + "/krona.png")
canvas.create_image(181,100,image=logga_img)

# Skriv ut text "Grattis <namn>!"
skriv_namn_text=customtkinter.CTkLabel(ruta, text="Grattis <namn>!", font=('Century Gothic', 24, "bold"), bg_color="#366990")
skriv_namn_text.place(x=90, y=130)
# Skriv ut text "Din poäng: "
skriv_namn_text=customtkinter.CTkLabel(ruta, text="Din poäng: 100 pts", text_color="#383838", font=('Century Gothic', 20, "bold"), bg_color="#eff0f3")
skriv_namn_text.place(x=90, y=400)


# Knappens funktion
def button_function():
    print("Start")

#Skapa knappen
button = customtkinter.CTkButton(ruta, command=button_function, text="Börja om", text_color="#f2f2f2", font=('Century Gothic', 20, "bold"), fg_color='#32638b', width=300, height=55, corner_radius=20, hover_color="#f9d455", bg_color="#eff0f3")
button.place(x=31,y=600)

ruta.mainloop()