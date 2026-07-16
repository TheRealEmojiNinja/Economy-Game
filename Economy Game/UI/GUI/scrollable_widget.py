import customtkinter as ctk

class ScrollableWidget:

    def __init__(self, parent, title_text : str, information_text : str, row : int, column : int):

        self.scrollable_container = ctk.CTkScrollableFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.scrollable_container.grid_columnconfigure(0, weight=1)
        self.scrollable_container.grid(row=row, column=column, rowspan=20, padx=7, pady=7)

        self.title_label = ctk.CTkLabel(self.scrollable_container, text=title_text, font=('Bahnschrift Light SemiCondensed', 25, 'bold'))
        self.title_label.grid(row=0, column=0, pady=5)

        self.information_label = ctk.CTkLabel(self.scrollable_container, text=information_text, font=('Consolas', 18), wraplength=250)
        self.information_label.grid(row=1, column=0, pady=8)

    def refresh(self, new_information_text : str):
        self.information_label.configure(text=new_information_text)
