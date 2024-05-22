import os
import sys
import threading
from tkinter import *
import customtkinter as ck
from PIL import ImageTk, Image
import subprocess
#import Appointment_Alignment
#import GISAT_Plus_v1_5_6

ck.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ck.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = ck.CTk()
app.geometry("510x170+800+400")
app.title("GISAT Plus v1.5.6")
app.iconbitmap("images/cihp.ico")
app.resizable(False, False)

frame_1 = ck.CTkFrame(master=app, width=1900)
frame_1.grid(row=0, column=0, padx=20, pady=20, columnspan=2, sticky="nsew")

gplus = ImageTk.PhotoImage(file="images/gisat_plus.png")

gplus_ = Label(master=frame_1, image=gplus, bd=0)  # , background="#333333")
gplus_.grid(row=0, column=0, padx=(20, 20), pady=(50, 20), rowspan=2, sticky="nsew")


def suggest_appointment_date():
    os.system('python GISAT_Plus_v1_5_6.py')
    #sys.exit(0)

def suggest_appointment_date1():
    os.system('python Appointment_Alignment.py')
    #sys.exit(0)
# Create threads for each function
thread1 = threading.Thread(target=suggest_appointment_date)
thread2 = threading.Thread(target=suggest_appointment_date1)




pepid_entry_button = ck.CTkButton(frame_1, text="GISAT Plus v1.5.6", width=290, height=40,
                                  font=ck.CTkFont(size=20, weight="bold"), command=thread1.start)
pepid_entry_button.grid(row=0, column=1, padx=2, pady=(2, 5), sticky="w")

pepid_entry_button = ck.CTkButton(frame_1, text="Clinic Appointment Alignment", width=290, height=40,
                                  font=ck.CTkFont(size=19, weight="bold"), command=thread2.start)
pepid_entry_button.grid(row=1, column=1, padx=2, pady=(2, 5), sticky="w")

# Call the function to run the other script

app.mainloop()
