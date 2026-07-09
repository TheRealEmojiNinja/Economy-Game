import customtkinter as ctk, Data.game_data as g, UI.GUI.info_widget as widget

class ProvinceTab:
    def __init__(self, parent, game_object : g.GameData):
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

        self.province_selector_frame = ctk.CTkFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.province_selector_frame.grid_propagate(False)
        self.province_selector_frame.grid_columnconfigure(0, weight=1)
        self.province_selector_frame.grid_rowconfigure(0, weight=1)
        self.province_selector_frame.grid(row=0, column=0, padx=7, pady=7)

        self.province_selector_centering_frame = ctk.CTkFrame(self.province_selector_frame, fg_color='transparent')
        self.province_selector_centering_frame.grid(row=0, column=0)

        self.province_names = [province.getName().upper() for province in game_object.provinces]

        self.province_selector_instruction_label = ctk.CTkLabel(self.province_selector_centering_frame, text="Select a province from\nthe dropdown menu\nto view its\ninformation.", font=('Consolas', 20))
        self.province_selector_instruction_label.grid(row=0, column=0, pady=7)

        self.province_selector = ctk.CTkOptionMenu(self.province_selector_centering_frame, values=self.province_names, font=('Bahnschrift Light SemiCondensed', 20, 'bold'))
        self.province_selector.configure(command=lambda choice: self.changeProvince(choice, game_object))
        self.province_selector.set(self.province_names[0])
        self.selected_province = game_object.provinces[0]
        self.province_selector.grid(row=1, column=0, pady=7)

        self.province_container = ctk.CTkFrame(parent, corner_radius=10, width=600, height=500, fg_color='#292F3B')
        self.province_container.grid_propagate(False)
        self.province_container.grid_columnconfigure(0, weight=1)
        self.province_container.grid(row=0, column=1, padx=7, pady=7)

        self.title_container = ctk.CTkFrame(self.province_container, fg_color='#313847', width=600, height=50)
        self.title_container.grid_propagate(False)
        self.title_container.grid_rowconfigure(0, weight=1)
        self.title_container.grid_columnconfigure(0, weight=1)
        self.title_container.grid(row=0, column=0, padx=7, pady=7)

        self.province_title = ctk.CTkLabel(self.title_container, text=self.selected_province.getName().upper(), font=('Bahnschrift Light SemiCondensed', 35, 'bold'))
        self.province_title.grid(row=0, column=0, padx=7, pady=7)

        self.stats_container = ctk.CTkFrame(self.province_container, fg_color='#313847', width=600, height=420)
        self.stats_container.grid_propagate(False)
        self.stats_container.grid(row=1, column=0, padx=7, pady=7)

        self.factory_info = widget.InfoWidget(self.stats_container, 
                                           f"Factories: {self.selected_province.getFactories()}\nOutage Status: {'No Outage' if not self.selected_province.getOutageStatus() else 'Ongoing Outage'}\nDays until Outage\nis Resolved: {'No Outage' if self.selected_province.getOutageTime() == -1 else self.selected_province.getOutageTime()}", 
                                           0, 0,
                                           100, 300,
                                           fg_color='#272C38',
                                           font=('Consolas', 15))

        #self.province_stats = ctk.CTkLabel(self.province_container, text=self.selected_province.printStats())
        #self.province_stats.grid(row=0, column=0)

    def changeProvince(self, choice : str, game_object : g.GameData):
        index = self.province_names.index(choice)
        self.selected_province = game_object.provinces[index]
        self.updateProvinceView()
    
    def updateProvinceView(self):
        self.factory_info.refresh(f"Factories: {self.selected_province.getFactories()}\nOutage Status: {'No Outage' if not self.selected_province.getOutageStatus() else 'Ongoing Outage'}\nDays until Outage\nis Resolved: {'No Outage' if self.selected_province.getOutageTime() == -1 else self.selected_province.getOutageTime()}")


