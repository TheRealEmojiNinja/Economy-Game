import customtkinter as ctk, Data.game_data as g

class SpinBoxWidget:
     
    def __init__(self, parent, instruction_text : str, spin_box_text : str, left_button_image, right_button_image, left_button_function, right_button_function, game_object : g.GameData):
         
        self.container_frame = ctk.CTkFrame(parent, corner_radius=10, width=250, height=250, fg_color='#292F3B')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure(0, weight=1)
        self.container_frame.grid(row=0, column=1, padx=7, pady=7)

        self.instruction_label = ctk.CTkLabel(self.container_frame, text=instruction_text, font=('Consolas', 20))
        self.instruction_label.grid(row=0, column=0)

        self.centering_frame_for_buttons = ctk.CTkFrame(self.container_frame, fg_color='transparent')
        self.centering_frame_for_buttons.grid(row=1, column=0, pady=15)

        self.left_button = ctk.CTkButton(self.centering_frame_for_buttons, image=left_button_image, text='', command=lambda:left_button_function(game_object), fg_color="#232633", hover_color='#3E455A', height=50, width=50)
        self.left_button.grid(row=0, column=0, padx=10)

        self.spin_box_label = ctk.CTkLabel(self.centering_frame_for_buttons, text=spin_box_text, font=('Bahnschrift Light SemiCondensed', 30, 'bold'), width=30, height=50)
        self.spin_box_label.grid(row=0, column=1, padx=5)

        self.right_button = ctk.CTkButton(self.centering_frame_for_buttons, image=right_button_image, text='', command=lambda:right_button_function(game_object), fg_color='#232633', hover_color='#3E455A', height=50, width=50)
        self.right_button.grid(row=0, column=2, padx=10)

    def refresh(self, new_spin_box_text):
        self.spin_box_label.configure(text=new_spin_box_text)

    def disableLeftButton(self):
        self.left_button.configure(state="disabled")

    def enableLeftButton(self):
        self.left_button.configure(state="normal")
    
    def disableRightButton(self):
        self.right_button.configure(state="disabled")
    
    def enableRightButton(self):
        self.right_button.configure(state="normal")









import customtkinter as ctk

class SelectorWidget:

    def __init__(self, parent, instruction_text : str, selector_values, function : function, game_object):
         
        self.container_frame = ctk.CTkFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure(0, weight=1)
        self.container_frame.grid(row=0, column=0, rowspan=20, padx=7, pady=7)

        self.centering_frame = ctk.CTkFrame(self.container_frame, fg_color='transparent')
        self.centering_frame.grid(row=0, column=0)

        self.instruction_label = ctk.CTkLabel(self.centering_frame, text=instruction_text, font=('Consolas', 20))
        self.instruction_label.grid(row=0, column=0, pady=7)

        self.selector = ctk.CTkOptionMenu(self.centering_frame, values=selector_values, font=('Bahnschrift Light SemiCondensed', 20, 'bold'))
        self.selector.configure(command=lambda choice: function(choice, game_object))
        self.selector.grid(row=1, column=0, pady=7)

    def setValue(self, value):
        self.selector.set(value)

