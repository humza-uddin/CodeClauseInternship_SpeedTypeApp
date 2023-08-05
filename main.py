import tkinter as tk
import customtkinter
import threading
import random

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class SpeedType:
 
   def __init__(self):
        
        self.root = customtkinter.CTk()
        self.root.title('Speed Typing Test App')
        self.root.geometry("1000x500")

        self.texts = open("text.txt", "r").read().split("\n")

        self.sample = customtkinter.CTkLabel(self.root, text= random.choice(self.texts))
        self.sample.grid(row=0 , column=0, column_span = 800)
        
        button_1 = customtkinter.CTkButton(master= self.root, width= 50, height= 50, corner_radius= 8, border_width= 2)
        button_1.grid(row = 1, column=0)
        button_2 = customtkinter.CTkButton(master= self.root, width= 50, height= 50, corner_radius= 8, border_width= 2)
        button_2.grid(row = 2, column=0)
        button_3 = customtkinter.CTkButton(master= self.root, width= 50, height= 50, corner_radius= 8, border_width= 2)
        button_3.grid(row = 3, column=0)


        button_1 = customtkinter.CTkButton(master= self.root, width= 50, height= 50, corner_radius= 8, border_width= 2)
        button_1.grid(row = 1, column=1)
        button_2 = customtkinter.CTkButton(master= self.root, width= 50, height= 50, corner_radius= 8, border_width= 2)
        button_2.grid(row = 2, column=1)
        button_3 = customtkinter.CTkButton(master= self.root, width= 50, height= 50, corner_radius= 8, border_width= 2)
        button_3.grid(row = 3, column=1)

        self.root.mainloop()

SpeedType()