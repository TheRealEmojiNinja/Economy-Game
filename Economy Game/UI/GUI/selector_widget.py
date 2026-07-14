import customtkinter as ctk

class SelectorWidget:

    def __init__(self, parent, instruction_text : str, selector_values, function : function, game_object):
         
        self.container_frame = ctk.CTkFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure(0, weight=1)
        self.container_frame.grid(row=0, column=0, padx=7, pady=7)

        self.centering_frame = ctk.CTkFrame(self.container_frame, fg_color='transparent')
        self.centering_frame.grid(row=0, column=0)

        self.instruction_label = ctk.CTkLabel(self.centering_frame, text=instruction_text, font=('Consolas', 20))
        self.instruction_label.grid(row=0, column=0, pady=7)

        self.selector = ctk.CTkOptionMenu(self.centering_frame, values=selector_values, font=('Bahnschrift Light SemiCondensed', 20, 'bold'))
        self.selector.configure(command=lambda choice: function(choice, game_object))
        self.selector.grid(row=1, column=0, pady=7)

    def setValue(self, value):
        self.selector.set(value)
