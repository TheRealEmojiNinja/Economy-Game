import customtkinter as ctk

import CTkToolTip as ctktooltip

class InfoWidget:

    def __init__(self, parent, info_text : str, row : int, col : int, height : int=50, width : int=200, fg_color='#343B4A', font = ('Consolas', 20), image=None, tooltip_text : str=None):
          
        self.container_frame = ctk.CTkFrame(parent, corner_radius=10, height=height, width=width, fg_color=fg_color)
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure(0, weight=1)
        self.container_frame.grid(row=row, column=col, padx=5, pady=5)

        if image != None:
            self.centering_frame = ctk.CTkFrame(self.container_frame, fg_color='transparent')
            self.centering_frame.grid(row=0, column=0)
            self.image_label = ctk.CTkLabel(self.centering_frame, image=image, text='')
            self.image_label.grid(row=0, column=0)
            self.info_label = ctk.CTkLabel(self.centering_frame, text=info_text, font=font)
            self.info_label.grid(row=0, column=1)
        else:
            self.info_label = ctk.CTkLabel(self.container_frame, text=info_text, font=font)
            self.info_label.grid(row=0, column=0)

        if tooltip_text != None:
            self.frame_tool_tip = ctktooltip.CTkToolTip(self.container_frame, message=tooltip_text, delay=0)
            self.centering_frame_tool_tip = ctktooltip.CTkToolTip(self.centering_frame, message=tooltip_text, delay=0)
            self.image_tool_tip = ctktooltip.CTkToolTip(self.image_label, message=tooltip_text, delay=0)
            self.text_tool_tip = ctktooltip.CTkToolTip(self.info_label, message=tooltip_text, delay=0)

    def refresh(self, new_info_text : str):
        self.info_label.configure(text=new_info_text)

