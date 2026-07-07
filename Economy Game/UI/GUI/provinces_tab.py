import customtkinter as ctk

class ProvinceTab:
    def __init__(self, parent, game_object):
        '''self.province_frames, self.provinces = [], []

        for i in range(len(game_object.provinces)):
            self.province_frames.append(ctk.CTkFrame(self.provinces_tab, border_width=5, corner_radius=3))

        self.province_frames = [ctk.CTkFrame(self.provinces_tab, border_width=5, corner_radius=3)]

        self.provinces = [ctk.CTkLabel() province for province in game_object.provinces]

        # Display each province and its statistics
        i = 0
        j = 0
        for province in game_object.provinces:
            self.province_frame = ctk.CTkFrame(self.provinces_tab, border_width=5, corner_radius=3)
            self.province_frame.grid(row=i, column=j, padx=4, pady=4)
            province_name = ctk.CTkLabel(self.province_frame, text=province.getName(), corner_radius=5, border_width=3)
            province_name.pack(padx=5, pady=5)
            self.province_stats = ctk.CTkLabel(self.province_frame, text=province.printStats())
            self.province_stats.pack(padx=10, pady=10)
            if j == 3:
                i += 1
                j = 0
            else:
                j += 1'''
        
        # Redo provinces menu