import customtkinter as ctk

try:
    from ctypes import windll, byref, sizeof, c_int
except Exception:
    print("Cannot Import ctypes")

# Colors
black_text = "#383838"
white_text = "#F6F6F6"
background_color = "#D4E09B"
title_bar = 0x009BE0D4
entry_color = "#F6F6F6"
button_color = "#F19C79"
button_hover_color = "#A44A3F"


class App(ctk.CTk):
    def __init__(self, title: str, size: tuple, appearance: str):
        super().__init__(fg_color=background_color)

        self.title(title)
        self.geometry(f"{size[0]}x{size[1]}")
        self.minsize(size[0], size[1])
        ctk.set_appearance_mode(appearance)

        self.change_title_bar(title_bar)

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
        frame = ctk.CTkFrame(master=parent)

        username_label = ctk.CTkLabel(master=frame,
                                      text="Email/Username:",
                                      font=("Segoe UI", 15),
                                      text_color=black_text,
                                      fg_color="red")

        username_entry = ctk.CTkEntry(master=frame)

        username_label.pack(expand=True, fill="x")
        username_entry.pack(expand=True, fill="x")

        return frame

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
    print("Hello World")
    App("Login App", (400, 350), "light")
