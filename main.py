from tkinter import *
import tkinter as tk
import customtkinter
import time
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

        self.frame = customtkinter.CTkFrame(self.root)

        self.sample = customtkinter.CTkLabel(self.frame, text= random.choice(self.texts),font=customtkinter.CTkFont(size=20))
        self.sample.grid(row=0 , column=0, columnspan = 500, padx=10,pady=20)

        self.entry  = customtkinter.CTkEntry(self.frame, width=500, height=50,font=customtkinter.CTkFont(size=24))
        self.entry.grid(row=1 , column=0, columnspan =500, padx=10,pady=20)
        self.entry.bind("<KeyPress>", self.start)
        
        self.speed = customtkinter.CTkLabel(self.frame, text="Speed: \n 0.00 CPS \n 0.00 CPM",font=customtkinter.CTkFont(size=12))
        self.speed.grid(row=2 , column=0, columnspan = 20, padx=10,pady=20)

        self.reset = customtkinter.CTkButton(self.frame, text= "Reset" , command= self.reset1)
        self.reset.grid(row=3 , column=0, columnspan = 5, padx=10,pady=20)
        
        self.frame.pack(expand=True)

        self.counter = 0
        self.started = False

        self.root.mainloop()

   def start(self, event):
        if not self.started:
             if not event.keycode in [16,17,18]:
                  self.started = True
                  t = threading.Thread(target=self.time_thread)
                  t.start()
        if not self.sample.cget('text').startswith(self.entry.get()):
             self.entry.configure(fg="red") 
        else:
             self.entry.configure(fg="black")
        if self.entry.get() == self.sample.cget('text')[:-1]:
             self.started = False
             self.entry.configure(fg="blue")
   
   def time_thread(self):
        while self.started:
             time.sleep(0.1)
             self.counter += 0.1
             cps = len(self.entry.get()) / self.counter
             cpm = cps * 60
             self.speed.configure(text= f"Speed: \n{cps:.2f} CPS\n{cpm:.2f} CPM")

   def reset1(self):
        pass

SpeedType()
