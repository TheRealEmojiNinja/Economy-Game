import customtkinter as ctk

class InfoWidget:

    text_font = ('Consolas', 20)

    def __init__(self, parent, info_text : str, row : int, col : int):
        
        self.container_frame = ctk.CTkFrame(parent, corner_radius=10, height=50, width=200, fg_color='#343B4A')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure(0, weight=1)
        self.container_frame.grid(row=row, column=col, padx=5, pady=5)

        self.info_label = ctk.CTkLabel(self.container_frame, text=info_text, font=InfoWidget.text_font)
        self.info_label.grid(row=0, column=0)

    def refresh(self, new_info_text : str):
        self.info_label.configure(text=new_info_text)

