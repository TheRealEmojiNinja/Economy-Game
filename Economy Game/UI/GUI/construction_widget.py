import customtkinter as ctk


class ConstructionWidget:

    button_font = ('Bahnschrift Light SemiCondensed', 25, 'bold')
    text_font = ('Consolas', 20)

    def __init__(self, parent, queue_text : str, requirements : str, row : int, col : int, function):

        self.container_frame = ctk.CTkFrame(parent, border_width=5, corner_radius=20, width=250, height=200)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid(row=row, column=col, padx=7, pady=7)

        #self.requirements = ctk.CTkLabel(self.container_frame, text=requirements, font=ConstructionWidget.text_font)
        #self.requirements.grid(row=0, column=0, pady=15)

        self.add_to_queue_button = ctk.CTkButton(self.container_frame, text=queue_text, command=lambda:function, font=ConstructionWidget.button_font, border_width=5, corner_radius=20, width=200, height=150)
        self.add_to_queue_button.grid(row=1, column=0, pady=15)

