import os
import tkinter
import tkinter.messagebox
import customtkinter
import messagebox
import mysql.connector
from PIL import Image
from datetime import date, timedelta, datetime
import pandas as pd
from colorama import Fore, Style
import Appointment_Alignment_Scripts


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"
IMAGE_WIDTH = 621
IMAGE_HEIGHT = 125
IMAGE_PATH = 'images/clinical_app_align.png'


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.topwindow = customtkinter.CTkToplevel(None)
        self.topwindow.geometry("350x100+400+200")
        self.topwindow.title("Host IP Address")
        self.grid_columnconfigure(1, weight=1)
        self.topwindow.iconbitmap("images/cihp.ico")
        self.topwindow.resizable(False, False)

        self.break_label = customtkinter.CTkLabel(self.topwindow, text="Type in a host IP address:",
                                                  font=customtkinter.CTkFont(size=12),
                                                  text_color=("gray10", "#DCE4EE"))
        self.break_label.grid(row=0, column=0, padx=2, pady=(2, 0), sticky="w")

        self.ip_entry = customtkinter.CTkEntry(self.topwindow, placeholder_text="Enter IP address of host", width=200,
                                               height=20, font=customtkinter.CTkFont(size=15))
        self.ip_entry.grid(row=1, column=0, pady=0, padx=(2, 0), sticky="e")

        self.pepid_entry_button = customtkinter.CTkButton(self.topwindow, text="Connect to Host",
                                                          width=200, font=customtkinter.CTkFont(size=15),
                                                          command=self.ip_get_destroy_top)
        self.pepid_entry_button.grid(row=2, column=0, padx=2, pady=(2, 5), sticky="w")

        self.topwindow.lift()
        self.topwindow.focus_force()

        # self.ip_request = customtkinter.CTkInputDialog(text="Type in a host IP address:", title="Host IP Address")
        # print("Dialog:", self.ip_request.get_input())

        # p_request_value = self.ip_request.get_input()
        # print(ip_request_value)

        # host_ip = ip_request.get_input()

        try:
            mydb1 = mysql.connector.connect(
                host=self.ip_entry.get(),
                user="root",
                passwd="Admin123",
                database='openmrs'
            )

            my_cursor1 = mydb1.cursor()

            # my_cursor1.close()
            # mydb1.close()
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))

        # configure window
        self.title("Clinical Appointment Alignment")
        self.geometry(f"{1100}x{590}+400+450")
        self.iconbitmap("images/cihp.ico")
        self.resizable(False, False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18), weight=0)

        # create sidebar frame with widgets
        self.clinicdays_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.clinicdays_frame.grid(row=0, column=0, pady=9, rowspan=14, sticky="nsew")
        self.clinicdays_frame.grid_rowconfigure(17, weight=1)
        self.clinicdays_label = customtkinter.CTkLabel(self.clinicdays_frame, text="Select facility clinic days:",
                                                       font=customtkinter.CTkFont(size=15, weight="bold"))
        self.clinicdays_label.grid(row=0, column=0, padx=2, pady=(5, 5), sticky="w")

        self.checkboxmonday_var = customtkinter.StringVar(value="off")
        self.monday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Monday",
                                                         variable=self.checkboxmonday_var, onvalue="on", offvalue="off",
                                                         command=self.get_checked_days)
        self.monday_checkbox.grid(row=1, column=0, pady=(2, 0), padx=2, sticky="w")

        self.checkboxtuesday_var = customtkinter.StringVar(value="off")
        self.tuesday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Tuesday",
                                                          variable=self.checkboxtuesday_var, onvalue="on",
                                                          offvalue="off", command=self.get_checked_days)
        self.tuesday_checkbox.grid(row=2, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxwednesday_var = customtkinter.StringVar(value="off")
        self.wednesday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Wednesday",
                                                            variable=self.checkboxwednesday_var, onvalue="on",
                                                            offvalue="off", command=self.get_checked_days
                                                            )
        self.wednesday_checkbox.grid(row=3, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxthursday_var = customtkinter.StringVar(value="off")
        self.thursday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Thursday",
                                                           variable=self.checkboxthursday_var, onvalue="on",
                                                           offvalue="off", command=self.get_checked_days
                                                           )
        self.thursday_checkbox.grid(row=4, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxfriday_var = customtkinter.StringVar(value="off")
        self.friday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Friday",
                                                         variable=self.checkboxfriday_var, onvalue="on",
                                                         offvalue="off", command=self.get_checked_days
                                                         )
        self.friday_checkbox.grid(row=5, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxsaturday_var = customtkinter.StringVar(value="off")
        self.saturday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Saturday",
                                                           variable=self.checkboxsaturday_var, onvalue="on",
                                                           offvalue="off", command=self.get_checked_days
                                                           )
        self.saturday_checkbox.grid(row=6, column=0, pady=(0, 0), padx=2, sticky="w")

        self.checkboxsunday_var = customtkinter.StringVar(value="off")
        self.sunday_checkbox = customtkinter.CTkCheckBox(master=self.clinicdays_frame, text="Sunday",
                                                         variable=self.checkboxsunday_var, onvalue="on",
                                                         offvalue="off", command=self.get_checked_days
                                                         )
        self.sunday_checkbox.grid(row=7, column=0, pady=(0, 0), padx=2, sticky="w")

        self.break_label = customtkinter.CTkLabel(self.clinicdays_frame, text="_____________________________",
                                                  font=customtkinter.CTkFont(size=15, weight="bold"),
                                                  text_color=("gray10", "#DCE4EE"))
        self.break_label.grid(row=8, column=0, padx=2, pady=(2, 2), sticky="w")

        # Bind the combined function to the <Return> event
        # self.pepid_entry.bind("<Return>", self.combined_function)

        self.pepid_entry = customtkinter.CTkEntry(self.clinicdays_frame, placeholder_text="Enter PEPID", width=200,
                                                  height=40, font=customtkinter.CTkFont(size=20, weight="bold"))
        self.pepid_entry.grid(row=9, column=0, pady=(10, 0), padx=(2, 0), sticky="w")
        self.pepid_entry.bind("<Return>", self.current_client_details)

        self.pepid_entry_button = customtkinter.CTkButton(self.clinicdays_frame, text=f"Suggest Appointment Date",
                                                          width=200, font=customtkinter.CTkFont(size=15),
                                                          command=self.current_client_details)
        self.pepid_entry_button.grid(row=10, column=0, padx=2, pady=(2, 5), sticky="w")

        bleed_now_var = customtkinter.StringVar()

        def determinant(self):
            ip = self.ip_entry.get()
            try:
                mydb1 = mysql.connector.connect(
                    host=ip,
                    user="root",
                    passwd="Admin123",
                    database='openmrs'
                )
                my_cursor1 = mydb1.cursor()
                # my_cursor1.close()
                # mydb1.close()
            except Exception as e:
                messagebox.showinfo('Info', "ERROR: {}".format(e))
            pepid = self.pepid_entry.get()
            get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND `voided`=0;"
            run_set_patient_id = my_cursor1.execute(get_patient_id)
            result_patient_id1 = my_cursor1.fetchone()
            print(result_patient_id1)

            last_vl_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date)
            last_vl_date1_mysql_result = my_cursor1.fetchone()

            last_vl_result1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_result)
            last_vl_result1_mysql_result = my_cursor1.fetchone()

            last_sample_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_sample_date)
            last_sample_date1_mysql_result = my_cursor1.fetchone()

            last_refill_days = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_days)
            last_refill_days_mysql_result1 = my_cursor1.fetchone()

            # Calculate next appointment date
            last_pickup_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_date_raw)
            last_refill_date_raw_mysql_result = my_cursor1.fetchone()[0]
            print(f"Fetched data: {last_refill_date_raw_mysql_result},{last_refill_days_mysql_result1}")

            # Getting Drug refill date
            if last_refill_date_raw_mysql_result:  # Check if data is not None
                year, month, day = last_refill_date_raw_mysql_result.year, last_refill_date_raw_mysql_result.month, last_refill_date_raw_mysql_result.day  # Assuming date is the first element (index 0)
                last_pickup_date_convert = date(year, month, day)

            else:
                print("No data found.")
            next_appt = (last_pickup_date_convert) + timedelta(days=last_refill_days_mysql_result1)
            print(f"This is next appointment date {next_appt}")

            # Getting VL date
            last_vl_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date_raw)
            last_vl_date_raw_mysql_result = my_cursor1.fetchone()[0]
            next_vl_date_ = last_vl_date_raw_mysql_result + timedelta(days=365.25)
            print(f"Fectched VL due date is: {next_vl_date_}")

            current_date = date.today()
            print(f"This is today's date {current_date}")

            pill_balance_cal = next_appt - current_date
            print(pill_balance_cal)
            pill_balance_cal1 = pill_balance_cal.days
            print(pill_balance_cal1)

            bleed_due_days = current_date - last_vl_date_raw_mysql_result
            bleed_alert_days = bleed_due_days.days
            print(f"Bleeding alerto - {bleed_alert_days}")

            range_0_60 = range(0, 61)  # Meaning 0-60

        align_logo = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)),
                                            size=(IMAGE_WIDTH, IMAGE_HEIGHT))
        align_logo_label = customtkinter.CTkLabel(self, image=align_logo, text='')
        align_logo_label.grid(column=1, row=0, padx=(170, 0), pady=(0, 0))

    def current_client_details(self, event=None):
        ip = self.ip_entry.get()
        try:
            mydb1 = mysql.connector.connect(
                host=ip,
                user="root",
                passwd="Admin123",
                database='openmrs'
            )
            my_cursor1 = mydb1.cursor()
            # my_cursor1.close()
            # mydb1.close()
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))
        pepid = self.pepid_entry.get()

        pepid = self.pepid_entry.get()
        get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND `voided`=0;"
        run_set_patient_id = my_cursor1.execute(get_patient_id)
        result_patient_id1 = my_cursor1.fetchone()
        print(result_patient_id1)

        last_refill_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_date)
        last_refill_date_mysql_result = my_cursor1.fetchone()

        last_vl_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date)
        last_vl_date1_mysql_result = my_cursor1.fetchone()

        last_vl_result1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_result)
        last_vl_result1_mysql_result = my_cursor1.fetchone()

        last_sample_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_sample_date)
        last_sample_date1_mysql_result = my_cursor1.fetchone()
        print(last_sample_date1_mysql_result)

        if result_patient_id1 is None:
            messagebox.showerror("Client details error!!!",
                                 f"Client with the PEPID: {pepid} not found")

            self.client_name_label.grid_forget()
            self.last_pickup_label.grid_forget()
            self.last_pickup_duration.grid_forget()
            self.last_vl_date_label.grid_forget()
            self.last_vl_result_label.grid_forget()
            self.last_sample_label.grid_forget()
            self.bleeding_action1.grid_forget()
            self.appointment_sug_date.grid_forget()
            self.pill_balance_label.grid_forget()
            self.suggestionbox.grid_forget()
            self.eac_alert_yuletide_alert.grid_forget()
            self.suggestionbox_header.grid_forget()
            self.suggestionbox.grid_forget()
        else:

            get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND `voided`=0;"
            run_set_patient_id = my_cursor1.execute(get_patient_id)
            result_patient_id = my_cursor1.fetchone()[0]

            set_patient_id = f"SET @patient_id := '{result_patient_id}'"
            set_patient_id_mysql = my_cursor1.execute(set_patient_id)
            print(set_patient_id_mysql)

            client_name_fetch = my_cursor1.execute(Appointment_Alignment_Scripts.client_name)
            client_name_fetch_mysql_result = my_cursor1.fetchone()[0]

            client_age_fetch = my_cursor1.execute(Appointment_Alignment_Scripts.client_age)
            client_age_fetch_mysql_result = my_cursor1.fetchone()[0]

            last_vl_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date)
            last_vl_date_mysql_result = my_cursor1.fetchone()
            if last_vl_date_mysql_result is not None:
                last_vl_date_mysql_result1 = last_vl_date_mysql_result[0]
            else:
                last_vl_date_mysql_result1 = "No VL Date."

            last_vl_result = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_result)
            last_vl_result_mysql_result = my_cursor1.fetchone()
            if last_vl_result_mysql_result is not None:
                last_vl_result_mysql_result1 = last_vl_result_mysql_result[0]
            else:
                last_vl_result_mysql_result1 = "No VL Result."

            last_sample_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_sample_date)
            last_sample_date_mysql_result = my_cursor1.fetchone()
            if last_sample_date_mysql_result is not None:
                last_sample_date_mysql_result1 = last_sample_date_mysql_result[0]
            else:
                last_sample_date_mysql_result1 = "No Sample Date."

            last_refill_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_date)
            last_refill_date_mysql_result = my_cursor1.fetchone()
            if last_refill_date_mysql_result is not None:
                last_refill_date_mysql_result1 = last_refill_date_mysql_result[0]
            else:
                last_refill_date_mysql_result1 = "No Refill Date."

            last_refill_days = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_days)
            last_refill_days_mysql_result = my_cursor1.fetchone()
            if last_refill_days_mysql_result is not None:
                last_refill_days_mysql_result1 = last_refill_days_mysql_result[0]
            else:
                last_refill_days_mysql_result1 = "No Refill Qty."

            # Calculate next appointment date
            last_pickup_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_date_raw)
            last_refill_date_raw_mysql_result = my_cursor1.fetchone()[0]
            print(f"Fetched data: {last_refill_date_raw_mysql_result},{last_refill_days_mysql_result1}")
            # Getting Drug refill date
            if last_refill_date_raw_mysql_result:  # Check if data is not None
                year, month, day = last_refill_date_raw_mysql_result.year, last_refill_date_raw_mysql_result.month, last_refill_date_raw_mysql_result.day  # Assuming date is the first element (index 0)
                last_pickup_date_convert = date(year, month, day)
                print(last_pickup_date_convert)
            else:
                print("No data found.")
            next_appt = (last_pickup_date_convert) + timedelta(days=last_refill_days_mysql_result1)
            print(f"This is next appointment date {next_appt}")
            # Getting VL date
            last_vl_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date_raw)
            if last_vl_date_mysql_result is not None:
                last_vl_date_raw_mysql_result = my_cursor1.fetchone()[0]
            else:
                last_vl_date_raw_mysql_result = date(1900, 1, 1)

            next_vl_date_ = last_vl_date_raw_mysql_result + timedelta(days=365)
            print(f"Fectched VL due date is: {next_vl_date_}")
            current_date = date.today()
            print(f"This is today's date {current_date}")
            pill_balance_cal = next_appt - current_date
            print(pill_balance_cal)
            pill_balance_cal1 = pill_balance_cal.days
            print(f"Pill bal. is {pill_balance_cal1}")

            bleed_due_days = next_vl_date_ - current_date
            bleed_alert_days = int(bleed_due_days.days)
            print(f"Bleeding days interval - {bleed_alert_days}")
            print(type(bleed_alert_days))

            # range_0_60 = range(-10000, 61)  # Meaning 0-60

            self.client_name_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                            text=f"{client_name_fetch_mysql_result}      ",
                                                            font=customtkinter.CTkFont(size=14, weight="bold"))
            self.client_name_label.grid(row=11, column=0, padx=2, pady=(1, 1), sticky="w")

            self.last_pickup_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                            text=f"Last drug refill date:  {last_refill_date_mysql_result1}  .",
                                                            font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_pickup_label.grid(row=12, column=0, padx=2, pady=(2, 1), sticky="w")

            self.last_pickup_duration = customtkinter.CTkLabel(self.clinicdays_frame,
                                                               text=f"Last drug refill duration:  {last_refill_days_mysql_result1}",
                                                               font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_pickup_duration.grid(row=13, column=0, padx=2, pady=(1, 2), sticky="w")

            self.last_vl_date_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                             text=f"Last VL Date:  {last_vl_date_mysql_result1}'",
                                                             font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_vl_date_label.grid(row=14, column=0, padx=2, pady=(5, 0), sticky="w")

            self.last_vl_result_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                               text=f"Last VL Result:  {last_vl_result_mysql_result1}'",
                                                               font=customtkinter.CTkFont(size=13, slant="italic"))
            self.last_vl_result_label.grid(row=15, column=0, padx=2, pady=(0, 5), sticky="w")

            self.last_sample_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                            text=f"Last Sample date:  {last_sample_date_mysql_result1}'",
                                                            font=customtkinter.CTkFont(size=14, slant="italic"))
            self.last_sample_label.grid(row=16, column=0, padx=2, pady=(0, 5), sticky="w")

            self.pill_balance_label = customtkinter.CTkLabel(self.clinicdays_frame,
                                                             text=f"Pill Balance: {pill_balance_cal1} Pills",
                                                             font=customtkinter.CTkFont(size=14,
                                                                                        weight="bold"))
            self.pill_balance_label.grid(row=17, column=0, padx=2, pady=(2, 2), sticky="w")

            # self.suggested_appointment_date = customtkinter.CTkLabel(self.clinicdays_frame, text="00-00-0000",
            #                                                          font=customtkinter.CTkFont(size=18, weight="bold"))
            # self.suggested_appointment_date.grid(row=18, column=0, padx=2, pady=(2, 2), sticky="w")
            # self.align_logo_label.config(state="hidden")

            align_logo1 = customtkinter.CTkImage(light_image=Image.open(os.path.join(IMAGE_PATH)),
                                                 size=(IMAGE_WIDTH, IMAGE_HEIGHT))
            align_logo1_label = customtkinter.CTkLabel(self, image=align_logo1, text='')
            align_logo1_label.grid(column=1, row=0, columnspan=2, sticky="nsew")

            self.checkalert_frame = customtkinter.CTkFrame(self, height=70, width=860)
            self.checkalert_frame.grid(row=1, column=1, padx=(10, 10), pady=(2, 2), sticky="w")
            self.checkalert_frame.grid_propagate(False)

            def is_between_(check_date, start_date, end_date):
                print(start_date <= check_date <= end_date)

            year = current_date.year  # You can change this to any year you want
            year2 = current_date.year + 1  # You can change this to any year you want
            # print(f"asfgvsdfbsdfbsdfb ---{year}")

            q1_start_date = date(year, 10, 1)
            q1_end_date = date(year, 12, 31)

            q2_start_date = date(year, 1, 1)
            q2_end_date = date(year, 3, 31)

            q3_start_date = date(year, 4, 1)
            q3_end_date = date(year, 6, 30)

            q4_start_date = date(year, 7, 1)
            q4_end_date = date(year, 9, 30)

            yuletide_Start = date(year, 12, 15)
            yuletide_end = date(year2, 1, 15)

            easter_period_start = date(year, 3, 20)
            easter_period_end = date(year, 4, 24)

            workers_day = date(year, 5, 1)
            democracy_day = date(year, 5, 29)
            Independence_day = date(year, 10, 1)

            q1 = is_between_(next_vl_date_, q1_start_date, q1_end_date)
            q2 = is_between_(next_vl_date_, q2_start_date, q2_end_date)
            q3 = is_between_(next_vl_date_, q3_start_date, q3_end_date)
            q4 = is_between_(next_vl_date_, q4_start_date, q4_end_date)

            cur_date_q1 = is_between_(current_date, q1_start_date, q1_end_date)
            cur_date_q2 = is_between_(current_date, q2_start_date, q2_end_date)
            cur_date_q3 = is_between_(current_date, q3_start_date, q3_end_date)
            cur_date_q4 = is_between_(current_date, q4_start_date, q4_end_date)

            pills_of_90 = 90
            pills_of_120 = 120
            pills_of_150 = 150
            pills_of_180 = 180

            if isinstance(last_vl_result_mysql_result1, int):
                changed_last_vl_result_to_int = last_vl_result_mysql_result1
            elif isinstance(last_vl_result_mysql_result1, str):
                changed_last_vl_result_to_int = 0

            if int(client_age_fetch_mysql_result) < 19:
                ped_label = "3.    Pediatrics Client!!! Ensure all pediatrics related interventions are factored in."

            elif int(client_age_fetch_mysql_result) == 19:
                ped_label = "3.    Pediatrics/OTZ Client!!! Ensure all pediatrics related interventions are factored in."
            elif 19 < int(client_age_fetch_mysql_result) < 25:
                ped_label = "3.    OTZ Client!!! Ensure all OTZ related interventions are factored in."
            else:
                ped_label = ""

            if bleed_alert_days <= 60:
                bleeding_alert = "BLEED NOW"
            elif bleed_alert_days is None:
                bleeding_alert = "BLEED NOW"
            elif 60 < bleed_alert_days <= 90 and (
                    (q1 == True and cur_date_q1 == True) or (q2 == True and cur_date_q2 == True) or (
                    q3 == True and cur_date_q3 == True) or (q4 == True and cur_date_q4 == True)):
                bleeding_alert = "BLEED NOW"
            else:
                bleeding_alert = "Consider suggestion"

            if bleeding_alert == (-366 > pill_balance_cal1) and ("BLEED NOW" or bleeding_alert == "Consider suggestion"):
                new_next_appt = current_date + timedelta(pills_of_90)  # Force MMD3 for IIT for 1 year and above
            elif bleeding_alert == "Consider suggestion" and int(last_vl_result_mysql_result1) >= 1000:
                new_next_appt = current_date + timedelta(days=30)
            elif bleeding_alert == "BLEED NOW" and int(last_vl_result_mysql_result1) >= 1000:
                new_next_appt = current_date + timedelta(days=30)
            elif bleeding_alert == "BLEED NOW":
                new_next_appt = current_date + timedelta(days=pills_of_180)
            elif bleeding_alert == "Consider suggestion" and bleed_alert_days <= 90:
                new_next_appt = current_date + timedelta(days=pills_of_90)
            elif bleeding_alert == "Consider suggestion" and 90 < bleed_alert_days <= 100:
                new_next_appt = current_date + timedelta(days=100)
            elif bleeding_alert == "Consider suggestion" and 100 < bleed_alert_days <= 110:
                new_next_appt = current_date + timedelta(days=110)
            elif bleeding_alert == "Consider suggestion" and 110 < bleed_alert_days <= 115:
                new_next_appt = current_date + timedelta(days=115)
            elif bleeding_alert == "Consider suggestion" and 115 < bleed_alert_days <= 120:
                new_next_appt = current_date + timedelta(days=pills_of_120)
            elif bleeding_alert == "Consider suggestion" and 120 < bleed_alert_days <= 125:
                new_next_appt = current_date + timedelta(days=125)
            elif bleeding_alert == "Consider suggestion" and 125 < bleed_alert_days <= 130:
                new_next_appt = current_date + timedelta(days=130)
            elif bleeding_alert == "Consider suggestion" and 130 < bleed_alert_days <= 135:
                new_next_appt = current_date + timedelta(days=135)
            elif bleeding_alert == "Consider suggestion" and 135 < bleed_alert_days <= 140:
                new_next_appt = current_date + timedelta(days=140)
            elif bleeding_alert == "Consider suggestion" and 140 < bleed_alert_days <= 145:
                new_next_appt = current_date + timedelta(days=145)
            elif bleeding_alert == "Consider suggestion" and 145 < bleed_alert_days <= 150:
                new_next_appt = current_date + timedelta(days=pills_of_150)
            elif bleeding_alert == "Consider suggestion" and 150 < bleed_alert_days <= 155:
                new_next_appt = current_date + timedelta(days=155)
            elif bleeding_alert == "Consider suggestion" and 155 < bleed_alert_days <= 160:
                new_next_appt = current_date + timedelta(days=160)
            elif bleeding_alert == "Consider suggestion" and 160 < bleed_alert_days <= 165:
                new_next_appt = current_date + timedelta(days=165)
            elif bleeding_alert == "Consider suggestion" and 165 < bleed_alert_days <= 170:
                new_next_appt = current_date + timedelta(days=170)
            elif bleeding_alert == "Consider suggestion" and 170 < bleed_alert_days <= 175:
                new_next_appt = current_date + timedelta(days=175)
            elif bleeding_alert == "Consider suggestion" and 175 < bleed_alert_days <= 180:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            elif bleeding_alert == "Consider suggestion" and bleed_alert_days > 180:
                new_next_appt = current_date + timedelta(days=pills_of_180)

                '''           elif 60 < bleed_alert_days <= 90:
                new_next_appt = current_date + timedelta(days=pills_of_90)
            elif 90 < bleed_alert_days <= 120:
                new_next_appt = current_date + timedelta(days=pills_of_120)
            elif 120 < bleed_alert_days <= 150:
                new_next_appt = current_date + timedelta(days=pills_of_150)
            elif 120 < bleed_alert_days <= 180:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            elif 180 < bleed_alert_days:
                new_next_appt = current_date + timedelta(days=pills_of_180)
            if bleed_alert_days <= 60:
                total_pills_dispense = 60
            elif 60 < bleed_alert_days <= 90:
                total_pills_dispense = 90
            elif 90 < bleed_alert_days <= 120:
                total_pills_dispense = 120
            elif 120 < bleed_alert_days <= 150:
                total_pills_dispense = 120
            elif 120 < bleed_alert_days <= 180:
                total_pills_dispense = 180
            elif 180 < bleed_alert_days:
                total_pills_dispense = 180
'''
            total_pills_dispense1 = new_next_appt - current_date
            total_pills_dispense = int(total_pills_dispense1.days)
            # Define the desired format string
            date_format_string = "%d-%m-%Y"

            new_next_appt1 = new_next_appt.strftime(date_format_string)

            # Pill balance alternative in KEY NOTE
            if 1 > pill_balance_cal1:
                pill_balance_cal1_alt = 0
            else:
                pill_balance_cal1_alt = pill_balance_cal1

            # Convert date to 'Saturday, 2nd November 2024'
            def format_date_detailed(new_next_appt):
                """Formats a datetime object to include day of the week, ordinal suffix, and full month name."""
                # Get day of the week (0=Monday)
                day_of_week = new_next_appt.strftime("%A")  # Full day name (Monday-Sunday)
                day_number = new_next_appt.day

                # Define suffixes for dates (1st, 2nd, 3rd, etc.)
                suffixes = ["st", "nd", "rd", "th"]

                # Handle special cases for 11, 12, and 13
                if 11 <= day_number <= 13:
                    suffix = "th"
                else:
                    suffix = suffixes[day_number % 5 - 1]

                # Get full month name and formatted date
                month_name = new_next_appt.strftime("%B")  # Full month name (January-December)
                new_next_appt2 = f"{day_of_week} {month_name} {day_number}, {new_next_appt.year}"

                return new_next_appt2

            new_next_appt3 = format_date_detailed(new_next_appt)

            print(new_next_appt3)

            print(type(bleed_alert_days))

            # Combining selected clinic days
            combination = [self.checkboxmonday_var.get(), self.checkboxtuesday_var.get(),
                           self.checkboxwednesday_var.get(), self.checkboxthursday_var.get(),
                           self.checkboxfriday_var.get(), self.checkboxsaturday_var.get(),
                           self.checkboxsunday_var.get()]

            # Days of the week
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            # Identify checked days
            checked_days = [day for day, state in zip(days_of_week, combination) if state == "on"]

            # Print the checked days
            print("Checked days:", checked_days)
            day_of_week = new_next_appt.strftime("%A")
            print(day_of_week)

            '''if day_of_week in checked_days:
                new_next_appt
                print(new_next_appt)
            else:
                new_next_appt - timedelta(days=1)'''

            # Define the initial date
            initial_date = new_next_appt  # Example initial date

            # Define the list of days of the week to check for
            days_to_check = checked_days

            # Define the initial day of the week for the initial date
            initial_day_of_week = initial_date.strftime('%A')

            # Initialize the result variable to store the final date
            result_date = initial_date

            # Loop until the resulting date falls on one of the specified days
            while result_date.strftime('%A') not in days_to_check:
                # Deduct one day from the current result date
                result_date -= timedelta(days=1)

            # Print the final date
            print("Resulting Date:", result_date)
            clinic_days_based_date = result_date.strftime(date_format_string)

            def format_clinic_days_based_nxt_appt(result_date):
                """Formats a datetime object to include day of the week, ordinal suffix, and full month name."""
                # Get day of the week (0=Monday)
                day_of_week = result_date.strftime("%A")  # Full day name (Monday-Sunday)
                day_number = result_date.day

                # Define suffixes for dates (1st, 2nd, 3rd, etc.)
                suffixes = ["st", "nd", "rd", "th"]

                # Handle special cases for 11, 12, and 13
                if 11 <= day_number <= 13:
                    suffix = "th"
                else:
                    suffix = suffixes[day_number % 5 - 1]

                # Get full month name and formatted date
                month_name = result_date.strftime("%B")  # Full month name (January-December)
                result_date2 = f"{day_of_week} {month_name} {day_number}, {new_next_appt.year}"

                return result_date2

            result_date3 = format_clinic_days_based_nxt_appt(result_date)

            self.bleeding_action = customtkinter.CTkLabel(master=self.checkalert_frame, text="Bleeding action:",
                                                          font=customtkinter.CTkFont(size=14),
                                                          text_color="blue")
            self.bleeding_action.grid(row=0, column=1, padx=2, pady=(2, 1), sticky="w")

            self.bleeding_action1 = customtkinter.CTkLabel(master=self.checkalert_frame, text=f"{bleeding_alert}",
                                                           font=customtkinter.CTkFont(size=20, weight="bold"),
                                                           text_color="red")
            self.bleeding_action1.grid(row=1, column=1, padx=2, pady=(2, 1), sticky="w")

            self.appointment_sug = customtkinter.CTkLabel(master=self.checkalert_frame,
                                                          text="Suggested Appointment Date:",
                                                          font=customtkinter.CTkFont(size=14, weight="bold"))
            self.appointment_sug.grid(row=0, column=2, padx=(450, 0), pady=(2, 1), sticky="e")

            self.appointment_sug_date = customtkinter.CTkLabel(master=self.checkalert_frame,
                                                               text=f"{clinic_days_based_date} ({result_date3})",
                                                               font=customtkinter.CTkFont(size=20, weight="bold"))
            self.appointment_sug_date.grid(row=1, column=2, padx=(150, 0), pady=(2, 1), sticky="e")

            # create textbox
            total_pills_dispense__ = total_pills_dispense1
            total_pills_dispense__1 = total_pills_dispense__.total_seconds()

            # Convert total seconds to integer
            total_pills_dispense__2 = int(total_pills_dispense__1)
            total_pills_dispense__3 = total_pills_dispense__2 / 86400
            pill_balance_cal1__ = (pill_balance_cal1)

            dispense_quantity = total_pills_dispense - pill_balance_cal1_alt

            if last_vl_result_mysql_result1 is not None:
                try:
                    # Attempt conversion to integer
                    last_vl_result_int = int(last_vl_result_mysql_result1)
                    if last_vl_result_int >= 1000 and pill_balance_cal1 < 0:
                        dispense_quantity = 30
                except ValueError:
                    # Handle the case where conversion fails (e.g., print message)
                    print("Invalid value encountered for last_vl_result_mysql_result1")
            elif last_vl_result_mysql_result1 is not None:
                try:
                    # Attempt conversion to integer
                    last_vl_result_int = int(last_vl_result_mysql_result1)
                    if last_vl_result_int >= 1000 and 0 <= pill_balance_cal1 <= 20:
                        dispense_quantity = 30 - pill_balance_cal1
                except ValueError:
                    # Handle the case where conversion fails (e.g., print message)
                    print("Invalid value encountered for last_vl_result_mysql_result1")
            elif last_vl_result_mysql_result1 is not None:
                try:
                    # Attempt conversion to integer
                    last_vl_result_int = int(last_vl_result_mysql_result1)
                    if last_vl_result_int >= 1000 and pill_balance_cal1 > 20:
                        dispense_quantity = 0
                except ValueError:
                    # Handle the case where conversion fails (e.g., print message)
                    print("Invalid value encountered for last_vl_result_mysql_result1")
            elif pill_balance_cal1 > 0:
                dispense_quantity = total_pills_dispense - pill_balance_cal1_alt
            else:
                dispense_quantity = total_pills_dispense - pill_balance_cal1_alt

            print(type(total_pills_dispense1))
            print(type(pill_balance_cal1))
            print(total_pills_dispense1)
            print(pill_balance_cal1__)
            # print(dispense_quantity)

            print(type(last_vl_result_mysql_result1))

            if last_vl_result_mysql_result1 == "No VL Result.":
                eac_alert_text = ""
            elif int(last_vl_result_mysql_result1) >= 1000:
                eac_alert_text = "EAC Client"
            else:
                eac_alert_text = ""

            if is_between_(result_date, yuletide_Start, yuletide_end):
                yuletide_alert_text = "YULETIDE PERIOD APPOINTMENT"
            elif is_between_(result_date, easter_period_start, easter_period_end):
                yuletide_alert_text = "Possible Easter Period Flag"
            elif result_date == workers_day:
                yuletide_alert_text = "Workers' Day Flag"
            elif result_date == democracy_day:
                yuletide_alert_text = "Democracy Day Flag"
            elif result_date == democracy_day:
                yuletide_alert_text = "Independence Day Flag"
            else:
                yuletide_alert_text = ""

            if int(client_age_fetch_mysql_result) < 19:
                client_age_text = "Pediatrics Client"
            elif int(client_age_fetch_mysql_result) == 19:
                client_age_text = "Pediatrics/OTZ Client"
            elif 19 < int(client_age_fetch_mysql_result) < 25:
                client_age_text = "OTZ Client"
            else:
                client_age_text = ""

            if -366 > pill_balance_cal1:
                force_mmd3_for_iit_1_yr_above = "Note: MMD3 is recommended for IIT client(s) for a year and above"
            else:
                force_mmd3_for_iit_1_yr_above = ""

            self.eac_alert_yuletide_alert = customtkinter.CTkLabel(self,
                                                                   text=f"{eac_alert_text} - {yuletide_alert_text} - {client_age_text}",
                                                                   width=250,
                                                                   font=customtkinter.CTkFont(size=20, weight="bold"),
                                                                   text_color="red", anchor="w")
            self.eac_alert_yuletide_alert.grid(row=3, column=1, padx=10, pady=(2, 1), sticky="w")

            # self.yuletide_alert = customtkinter.CTkLabel(self,
            #                                             text=f"{yuletide_alert_text}",
            #                                             width=250,
            #                                             font=customtkinter.CTkFont(size=20, weight="bold"),
            #                                             text_color="red")
            # self.yuletide_alert.grid(row=4, column=1, padx=(0, 10), pady=(1, 1), sticky="w")

            self.suggestionbox_header = customtkinter.CTkLabel(self,
                                                               text="KEY NOTES (Appointment suggestion considerations)",
                                                               width=250,
                                                               font=customtkinter.CTkFont(size=15, weight="bold"))
            self.suggestionbox_header.grid(row=4, column=1, padx=(0, 10), pady=(1, 1), sticky="sw")

            Total_pills = dispense_quantity + pill_balance_cal1_alt
            suggestionbo_formatted_text = f"1.   Dispense {dispense_quantity} pill(s) - ({pill_balance_cal1_alt} pill(s) still with client from previous refill. {Total_pills} in total).\n2.   The aligned next appointment date is {new_next_appt1} ({new_next_appt3}) the suggested date is based on\n       the clinic days specified.\n{ped_label}\n\n\n\n{force_mmd3_for_iit_1_yr_above} "

            self.suggestionbox = customtkinter.CTkLabel(self, text=suggestionbo_formatted_text, width=250,
                                                        justify="left",
                                                        font=customtkinter.CTkFont(size=15))
            self.suggestionbox.grid(row=5, column=1, padx=(10, 10), pady=(1, 1), columnspan=2, sticky="nw")

            # suggestionbo_formatted_text = f"3.   The aligned next appointment date is {new_next_appt1} ({new_next_appt3}) the suggested date is based on\n the clinic days specified."

            # suggestionbox_formatted_text = f"<span>{suggestionbo_formatted_text.replace(pill_balance_cal1, f'<b>{pill_balance_cal1}</b>')}</span>"
            # self.suggestionbox.insert("0.0",
            #                        "APPOINTMENT SUGGESTION\n\n" + f"1.   Discount the client's {pill_balance_cal1} left over pills from the {total_pills_dispense} days dispense as suggested.")

            ip = self.ip_entry.get()
            try:
                # Connection to create line-list db
                mydb2 = mysql.connector.connect(
                    host=ip,
                    user="root",
                    passwd="Admin123"
                )

                my_cursor2 = mydb2.cursor()

                # Create db
                my_cursor2.execute("CREATE DATABASE IF NOT EXISTS appt_alignment_log")
                my_cursor2.execute("CREATE TABLE IF NOT EXISTS appt_alignment_log.`appt_alignment_log_tab` (\
                `State` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `SurgeCommand` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `LGA` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Datim_code` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Facility_name` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Pepid_Datim_code` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Patient_Id` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Pepid` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Client_Bio` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Last_Pickup_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Duration_Last_Pickup` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Pill_Balance` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Last_VL_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Last_VL_Result` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Bleeding_Alert` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Suggested_Next_Appt_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Suggested_Next_Appt_Day` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Actual_Suggested_Next_Appt_Date` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Actual_Suggested_Next_Appt_Day` VARCHAR(255) CHARACTER SET utf8 DEFAULT NULL,\
                `Key_Note` LONGTEXT CHARACTER SET utf8 DEFAULT NULL,\
                `Search_Timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

            except Exception as e:
                messagebox.showinfo('Info', "ERROR: {}".format(e))

            insert_searched_client = f"INSERT INTO `appt_alignment_log`.`appt_alignment_log_tab` (`State`, " \
                                     f"`SurgeCommand`, `LGA`, `Datim_code`, `Facility_name`, `Pepid_Datim_code`, " \
                                     f"`Patient_Id`, `Pepid`, `Client_Bio`, `Last_Pickup_Date`, " \
                                     f"`Duration_Last_Pickup`, `Pill_Balance`, `Last_VL_Date`, " \
                                     f"`Last_VL_Result`, `Bleeding_Alert`, `Suggested_Next_Appt_Date`, " \
                                     f"`Suggested_Next_Appt_Day`, `Actual_Suggested_Next_Appt_Date`, " \
                                     f"`Actual_Suggested_Next_Appt_Day`, `Key_Note`) " \
                                     f"VALUES ((SELECT State FROM `openmrs`.CIHP_ListOfFacility WHERE Datim_Code = (" \
                                     f"SELECT `property_value` FROM `openmrs`.`global_property` WHERE `property`= " \
                                     f"'facility_datim_code')LIMIT 1), (SELECT SurgeCommand FROM " \
                                     f"`openmrs`.CIHP_ListOfFacility WHERE Datim_Code = (SELECT `property_value` FROM " \
                                     f"`openmrs`.`global_property` WHERE `property`= 'facility_datim_code') LIMIT 1), " \
                                     f"(SELECT LGA FROM `openmrs`.CIHP_ListOfFacility WHERE Datim_Code = (SELECT " \
                                     f"`property_value` FROM `openmrs`.`global_property` WHERE `property`= " \
                                     f"'facility_datim_code')LIMIT 1), (SELECT `property_value` FROM " \
                                     f"`openmrs`.`global_property` WHERE `property`= 'facility_datim_code' LIMIT 1), " \
                                     f"(SELECT `property_value` FROM `openmrs`.`global_property` WHERE `property`= " \
                                     f"'Facility_Name' LIMIT 1), CONCAT('{pepid}','_',(SELECT `property_value` FROM " \
                                     f"`openmrs`.`global_property` WHERE `property`= 'facility_datim_code' LIMIT 1)), " \
                                     f"'{result_patient_id}', '{pepid}', '{client_name_fetch_mysql_result}', '{last_refill_date_mysql_result1}', " \
                                     f"'{last_refill_days_mysql_result1}', '{pill_balance_cal1}', '{last_vl_date_mysql_result1}', '{last_vl_result_mysql_result1}', '{bleeding_alert}', '{clinic_days_based_date}', '{result_date3}', " \
                                     f"'{new_next_appt1}', '{new_next_appt3}', '{suggestionbo_formatted_text}') "
            my_cursor2.execute(insert_searched_client)
            mydb2.commit()
            my_cursor2.close()
            mydb2.close()



    def combined_function(self):
        self.current_client_details()
        self.determinant()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def ip_get_destroy_top(self):
        ip_get = self.ip_entry.get()
        print(ip_get)
        self.topwindow.withdraw()

    def get_checked_days(self):
        if self.checkboxmonday_var.get() == "on" or self.checkboxtuesday_var.get() == "on" or self.checkboxwednesday_var.get() == "on" or self.checkboxthursday_var.get() == "on" or self.checkboxfriday_var.get() == "on" \
                or self.checkboxsaturday_var.get() == "on" or self.checkboxsunday_var.get() == "on":
            print([self.checkboxmonday_var.get(), self.checkboxtuesday_var.get(), self.checkboxwednesday_var.get(),
                   self.checkboxthursday_var.get(), self.checkboxfriday_var.get(), self.checkboxsaturday_var.get(),
                   self.checkboxsunday_var.get()])
            return ([self.checkboxmonday_var.get(), self.checkboxtuesday_var.get(), self.checkboxwednesday_var.get(),
                     self.checkboxthursday_var.get(), self.checkboxfriday_var.get(), self.checkboxsaturday_var.get(),
                     self.checkboxsunday_var.get()])


'''
    def main_determinant(self):
        ip = self.ip_entry.get()
        try:
            mydb1 = mysql.connector.connect(
                host=ip,
                user="root",
                passwd="Admin123",
                database='openmrs'
            )
            my_cursor1 = mydb1.cursor()
            # my_cursor1.close()
            # mydb1.close()
        except Exception as e:
            messagebox.showinfo('Info', "ERROR: {}".format(e))
        pepid = self.pepid_entry.get()
        get_patient_id = f"SELECT `patient_id` FROM `patient_identifier` WHERE `identifier` = '{pepid}' AND `voided`=0;"
        run_set_patient_id = my_cursor1.execute(get_patient_id)
        result_patient_id1 = my_cursor1.fetchone()
        print(result_patient_id1)

        last_vl_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date)
        last_vl_date1_mysql_result = my_cursor1.fetchone()

        last_vl_result1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_result)
        last_vl_result1_mysql_result = my_cursor1.fetchone()

        last_sample_date1 = my_cursor1.execute(Appointment_Alignment_Scripts.last_sample_date)
        last_sample_date1_mysql_result = my_cursor1.fetchone()

        last_refill_days = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_days)
        last_refill_days_mysql_result1 = my_cursor1.fetchone()

        # Calculate next appointment date
        last_pickup_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_refill_date_raw)
        last_refill_date_raw_mysql_result = my_cursor1.fetchone()[0]
        print(f"Fetched data: {last_refill_date_raw_mysql_result},{last_refill_days_mysql_result1}")

        # Getting Drug refill date
        if last_refill_date_raw_mysql_result:  # Check if data is not None
            year, month, day = last_refill_date_raw_mysql_result.year, last_refill_date_raw_mysql_result.month, last_refill_date_raw_mysql_result.day  # Assuming date is the first element (index 0)
            last_pickup_date_convert = date(year, month, day)

        else:
            print("No data found.")
        next_appt = (last_pickup_date_convert) + timedelta(days=last_refill_days_mysql_result1)
        print(f"This is next appointment date {next_appt}")

        # Getting VL date
        last_vl_date = my_cursor1.execute(Appointment_Alignment_Scripts.last_vl_date_raw)
        last_vl_date_raw_mysql_result = my_cursor1.fetchone()[0]
        next_vl_date_ = last_vl_date_raw_mysql_result + timedelta(days=365.25)
        print(f"Fectched VL due date is: {next_vl_date_}")

        current_date = date.today()
        print(f"This is today's date {current_date}")

        pill_balance_cal = next_appt - current_date
        print(pill_balance_cal)
        pill_balance_cal1 = pill_balance_cal.days
        print(pill_balance_cal1)

        bleed_due_days = current_date - last_vl_date_raw_mysql_result
        bleed_alert_days = bleed_due_days.days
        print(f"Bleeding alerto - {bleed_alert_days}")

        range_0_60 = range(0, 61)  # Meaning 0-60

        return next_appt, next_vl_date_, current_date, pill_balance_cal1, bleed_alert_days

    def next_appointment_date(self):
        next_appt, next_vl_date_, current_date, pill_balance_cal1, bleed_alert_days = self.main_determinant()
        print(f"sdsdfsdfsdf {next_appt}")
        print(next_vl_date_)
        print(current_date)
        print(pill_balance_cal1) '''

if __name__ == "__main__":
    app = App()
    app.mainloop()
