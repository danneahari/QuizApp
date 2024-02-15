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
canvas = tk.Canvas(ruta, bg="#eff0f3", width=363, height=786)
canvas.place(x=-2,y=-2)

# Rita in bakgrundsbild
background_img = tk.PhotoImage(file=Assets + "/quizbackground.png")
canvas.create_image(181,393,image=background_img)

# Rita in poängsymbol
logga_img = Image.open(Assets + "/points.png")
logga_img = logga_img.resize((30,30), Image.ANTIALIAS)
logga_img = ImageTk.PhotoImage(logga_img)
canvas.create_image(300,60,image=logga_img)

# Skriv ut Ämne
skriv_namn_text=customtkinter.CTkLabel(ruta, text="Ämne", font=('Century Gothic', 14, "bold"), bg_color="#eff0f3", text_color="#383838",justify="center")
skriv_namn_text.place(x=160, y=70)

# Skriv ut Poäng
skriv_namn_text=customtkinter.CTkLabel(ruta, text="100", font=('Century Gothic', 14, "bold"), bg_color="#eff0f3", text_color="#1a1f71",justify="center")
skriv_namn_text.place(x=320, y=35)

# Skriv ut fråga
skriv_namn_text=customtkinter.CTkLabel(ruta, text="Detta är en testfrågadfgdgadfgadfgaasdfasdf", font=('Century Gothic', 14, "bold"), bg_color="#FFFFFF", text_color="#383838",justify="center")
skriv_namn_text.place(x=30, y=150)

#Skapa en progressbar med CtkProgressBar samt progresstext

progressbar = customtkinter.CTkProgressBar(ruta, orientation="horizontal", progress_color="#31CD63", width=270,fg_color='#FFFFFF',mode="determinate", height=10)
progressbar.place(x=35,y=95)
progressText=customtkinter.CTkLabel(ruta, text="1/5", font=('Century Gothic', 12, "bold"), bg_color="#eff0f3", text_color="#383838",justify="center")
progressText.place(x=310, y=85)
progressbar.set(0.1)

# Knapparnas funktion
def button_function():
    print("Start")

#Skapa backa knapp
backa_img = tk.PhotoImage(file=Assets + "/backa.png")
button = tk.Button(ruta, bd=0, image = backa_img)
button.place(x=10,y=40) 

#Skapa svar1 knapp
button = customtkinter.CTkButton(ruta, command=button_function, text="Svar 1", text_color="#383838", font=('Century Gothic', 18, "bold"), fg_color='#FFFFFF', width=300, height=55, corner_radius=20, hover_color="#ffdb93", bg_color="#eff0f3")
button.place(x=31,y=440)
#Skapa svar2 knapp
button = customtkinter.CTkButton(ruta, command=button_function, text="Svar 2", text_color="#383838", font=('Century Gothic', 18, "bold"), fg_color='#FFFFFF', width=300, height=55, corner_radius=20, hover_color="#ffdb93", bg_color="#eff0f3")
button.place(x=31,y=510)
#Skapa svar3 knapp
button = customtkinter.CTkButton(ruta, command=button_function, text="Svar 3", text_color="#383838", font=('Century Gothic', 18, "bold"), fg_color='#FFFFFF', width=300, height=55, corner_radius=20, hover_color="#ffdb93", bg_color="#eff0f3")
button.place(x=31,y=580)
#Skapa svar4 knapp
button = customtkinter.CTkButton(ruta, command=button_function, text="Svar 4", text_color="#383838", font=('Century Gothic', 18, "bold"), fg_color='#FFFFFF', width=300, height=55, corner_radius=20, hover_color="#ffdb93", bg_color="#eff0f3")
button.place(x=31,y=650)

ruta.mainloop()

