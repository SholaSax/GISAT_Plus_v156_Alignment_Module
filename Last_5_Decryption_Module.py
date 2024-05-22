import msoffcrypto
import pathlib
from tkinter import Tk, filedialog, messagebox, ttk
import os
import shutil
import customtkinter as ck

hts = ck.CTk()
hts.geometry("300*300")
hts.title("GISAT Plus Last 5 Pharm. Decrypt")

frame_1 = ck.CTkFrame(master=hts)
frame_1.pack(pady=(20, 10), padx=20, fill="both", expand=True)


def run_all():
    path_ = filedialog.askdirectory()
    pattern = "CIHP_Last*.xlsx"

    # files = [file for file in os.listdir(path) if fnmatch.fnmatch(file, pattern)]

    url = pathlib.Path(path_)
    excel_files = list(url.glob(pattern))

    def unlock_hts(filename, passwd, output_folder):
        temp = open(filename, 'rb')
        excel = msoffcrypto.OfficeFile(temp)
        excel.load_key(passwd)
        out_path = pathlib.Path(output_folder)
        if not out_path.exists():
            out_path.mkdir()

        with open(str(out_path / filename.name), 'wb') as f:
            excel.decrypt(f)
        temp.close()

    # Define the path to the existing folder
    existing_folder_path = f"{path_}/Decrypted File(s)"

    # Check if the existing folder exists
    if os.path.exists(existing_folder_path):
        # Delete the existing folder and its contents
        shutil.rmtree(existing_folder_path)

    # Create the new folder
    os.makedirs(existing_folder_path)
    for i in excel_files:
        unlock_hts(i, 'datasecurityisheremovingforwardL5P', existing_folder_path)


hts_unlock_button = ck.CTkButton(master=frame_1, command=run_all,
                                 text="Decrypt Last 5 Pharmacy",
                                 width=280, font=("Century Gothic", 18, "bold"))
hts_unlock_button.pack(pady=(1, 4), padx=10)

hts.mainloop()
