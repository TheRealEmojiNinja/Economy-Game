import customtkinter as ctk

class StatisticWidget:

    title_font = ('Bahnschrift Light SemiCondensed', 35, 'bold')
    text_font = ('Consolas', 20)

    def __init__(self, parent, title_text : str, statistics_text : str, row : int, col : int):
        
        self.container_frame = ctk.CTkFrame(parent, border_width=5, corner_radius=20, width=250, height=250)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        #self.container_frame.grid_rowconfigure((0,1), weight=1)
        self.container_frame.grid(row=row, column=col, padx=7, pady=7)

        self.title = ctk.CTkLabel(self.container_frame, text=title_text, font=StatisticWidget.title_font)
        self.title.grid(row=0, column=0, pady=10)

        self.stats = ctk.CTkLabel(self.container_frame, text=statistics_text, font=StatisticWidget.text_font)
        self.stats.grid(row=1, column=0)

    def refresh(self, new_statistics_text : str):
        self.stats.configure(text=new_statistics_text)



