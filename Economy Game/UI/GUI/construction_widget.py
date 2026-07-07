import customtkinter as ctk


class ConstructionWidget:

    button_font = ('Bahnschrift Light SemiCondensed', 35, 'bold')
    text_font = ('Consolas', 20)

    def __init__(self, parent, queue_text : str, requirements : str, row : int, col : int, function):

        self.container_frame = ctk.CTkFrame(parent, border_width=5, corner_radius=20, width=250, height=500)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid(row=row, column=col, padx=7, pady=7)

        self.requirements = ctk.CTkLabel(parent, text=requirements, font=ConstructionWidget.text_font)
        self.requirements.grid(row=0, column=0)

        self.add_to_queue_button = ctk.CTkButton(parent, text=queue_text, command=lambda:function, font=ConstructionWidget.button_font)
        self.add_to_queue_button.grid(row=1, column=0, pady=15)

