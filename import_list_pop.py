import customtkinter
import os

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")


def reopen_merge():
    os.system('merge_linelist.py')


# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=reopen_merge)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
