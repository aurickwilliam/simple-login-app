import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import ctypes

try:
    from ctypes import windll, byref, sizeof, c_int
except Exception:
    print("Cannot Import ctypes")

appid = 'loniantech.loginapp.1' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

# Colors
black_text = "#383838"
white_text = "#F6F6F6"
background_color = "#D4E09B"
title_bar = 0x009BE0D4
entry_color = "#F6F6F6"
button_color = "#F19C79"
button_hover_color = "#A44A3F"

# Accounts
list_users = [["aurickwilliam", "aigoo"],
              ["vincenzo", "shibaloma"]]

class App(ctk.CTk):
    def __init__(self, title: str, size: tuple, appearance: str):
        super().__init__(fg_color=background_color)

        # Centering the window, i guess??
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        win_x = int((screen_width - size[0]) / 2)
        win_y = int((screen_height - size[1]) / 2)

        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}+{win_x}+{win_y}")
        self.minsize(size[0], size[1])
        ctk.set_appearance_mode(appearance)

        # Icon
        icon = tk.PhotoImage(file="lock_icon.png")
        self.wm_iconbitmap()
        self.iconphoto(True, icon)

        self.change_title_bar(title_bar)

        # Variables
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()
        self.username_entry = None
        self.password_entry = None

        title = self.title_frame(self, "Log-in")
        title.place(relx=0, rely=0, relwidth=1, relheight=0.2)

        main = self.main_frame(self)
        main.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        self.mainloop()

    def title_frame(self, parent, title_text):
        frame = ctk.CTkFrame(master=parent, fg_color="transparent")

        title_label = ctk.CTkLabel(master=frame,
                                   text=title_text,
                                   font=("Segoe UI", 30, "bold"),
                                   text_color=black_text)
        title_label.pack(expand=True)

        return frame

    def main_frame(self, parent):
        frame = ctk.CTkFrame(master=parent, fg_color="transparent")

        username_label = ctk.CTkLabel(master=frame,
                                      text="Email/Username:",
                                      font=("Segoe UI", 15, "bold"),
                                      text_color=black_text,
                                      anchor="sw")

        self.username_entry = ctk.CTkEntry(master=frame,
                                           height=40,
                                           font=("Segoe UI", 15),
                                           textvariable=self.username,
                                           fg_color=entry_color,
                                           text_color=black_text,
                                           border_width=0)

        password_label = ctk.CTkLabel(master=frame,
                                      text="Password:",
                                      font=("Segoe UI", 15, "bold"),
                                      text_color=black_text,
                                      anchor="sw")

        self.password_entry = ctk.CTkEntry(master=frame,
                                           height=40,
                                           show="\u2022",  # Bullet Character
                                           font=("Segoe UI", 15),
                                           textvariable=self.password,
                                           fg_color=entry_color,
                                           text_color=black_text,
                                           border_width=0)

        submit_btn = ctk.CTkButton(master=frame,
                                   text="Submit",
                                   fg_color=button_color,
                                   hover_color=button_hover_color,
                                   height=40,
                                   font=("Segoe UI", 15, "bold"),
                                   command=self.validate_input)

        # Layout
        username_label.pack(fill="x", padx=20)
        self.username_entry.pack(fill="x", padx=20, pady=(5, 10))

        password_label.pack(fill="x", padx=20)
        self.password_entry.pack(fill="x", padx=20, pady=(5, 10))

        submit_btn.pack(fill="x", padx=20, pady=(20, 20))

        return frame

    def validate_input(self):
        username = self.username.get()
        password = self.password.get()
        is_validated = False

        print(username)
        print(password)

        if username == "" or password == "":
            messagebox.showerror("No Input", "Please complete the form")
            return

        for user, userpass in list_users:
            if user == username and userpass == password:
                is_validated = True

        if is_validated:
            messagebox.showinfo("Account", "Access Granted!")
        else:
            messagebox.showwarning("Account", "Access Denied!")

        self.username.set(value="")
        self.password.set(value="")
        self.username_entry.focus()

    def change_title_bar(self, bg_color):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            windll.dwmapi.DwmSetWindowAttribute(HWND,
                                                35,
                                                byref(c_int(bg_color)),
                                                sizeof(c_int))
        except Exception:
            print("Cannot Change Title Bar Background Color")


if __name__ == '__main__':
    App("Login App", (400, 350), "light")
