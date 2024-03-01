import tkinter as tk
import customtkinter
from PIL import Image, ImageTk

### Funktioner som ritar sidor ####

def startSida():
    # Skapa globala variabler så att bilderna fortsätter finnas när funktionen kört klart
    global background_img, logga_img

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
        valjÄmneSida()

    #Skapa knappen
    button = customtkinter.CTkButton(ruta, command=button_function, text="Välj Ämne", text_color="#f2f2f2", font=('Century Gothic', 20, "bold"), fg_color='#F8C660', width=300, height=55, corner_radius=20, hover_color="#ffdb93", bg_color="#32638b")
    button.place(x=31,y=600)

def valjÄmneSida():
    # Skapa globala variabler så att bilderna fortsätter finnas när funktionen kört klart
    global background_img, logga_img

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
        frågeSida()

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

def frågeSida():
    # Skapa globala variabler så att bilderna fortsätter finnas när funktionen kört klart
    global background_img, logga_img

    # Skapa ett canvas i 'ruta'
    canvas = tk.Canvas(ruta, bg="#eff0f3", width=363, height=786)
    canvas.place(x=-2,y=-2)

    # Rita in bakgrundsbild
    background_img = tk.PhotoImage(file=Assets + "/quizbackground.png")
    canvas.create_image(181,393,image=background_img)

    # Rita in poängsymbol
    logga_img = Image.open(Assets + "/points.png")
    logga_img = logga_img.resize((30,30))
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
        resultatSida()

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

def resultatSida():
    # Skapa globala variabler så att bilderna fortsätter finnas när funktionen kört klart
    global background_img, logga_img

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
        startSida()

    #Skapa knappen
    button = customtkinter.CTkButton(ruta, command=button_function, text="Börja om", text_color="#f2f2f2", font=('Century Gothic', 20, "bold"), fg_color='#32638b', width=300, height=55, corner_radius=20, hover_color="#f9d455", bg_color="#eff0f3")
    button.place(x=31,y=600)

### Setup ### 

# Skapa ett tk-fönster "ruta" 
ruta = customtkinter.CTk()
ruta.geometry("363x786")
ruta.title("QuizApp") 

# Ladda in assets
Assets = "C:/Users/olive/Documents/Oliver skola/Python/Quizzapp/assets/"

# Ser till att startsidan ritas när programmet startas
startUp=True
if (startUp==True):
    startUp=False
    startSida()

### Main loop ###

ruta.mainloop()
