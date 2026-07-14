import customtkinter as ctk, Data.game_data as g, UI.GUI.info_widget as info_widget, UI.GUI.selector_widget as selector_widget

class ProvinceTab:
    def __init__(self, parent, game_object : g.GameData):

        self.province_names = [province.getName().upper() for province in game_object.provinces]
        self.province_selector = selector_widget.SelectorWidget(parent, "Select a province from\nthe dropdown menu\nto view its\ninformation.", self.province_names, self.changeProvince, game_object)
        self.selected_province = game_object.provinces[0]
        self.province_selector.setValue(self.province_names[0])

        self.province_container = ctk.CTkFrame(parent, corner_radius=10, width=600, height=500, fg_color='#292F3B')
        self.province_container.grid_propagate(False)
        self.province_container.grid_columnconfigure(0, weight=1)
        self.province_container.grid(row=0, column=1, padx=14, pady=14)

        self.title_container = ctk.CTkFrame(self.province_container, fg_color="#2D3341", width=600, height=50)
        self.title_container.grid_propagate(False)
        self.title_container.grid_rowconfigure(0, weight=1)
        self.title_container.grid_columnconfigure(0, weight=1)
        self.title_container.grid(row=0, column=0, padx=7, pady=7)

        self.province_title = ctk.CTkLabel(self.title_container, text=self.selected_province.getName().upper(), font=('Bahnschrift Light SemiCondensed', 35, 'bold'))
        self.province_title.grid(row=0, column=0, padx=7, pady=7)

        self.stats_container = ctk.CTkFrame(self.province_container, fg_color='#2D3341', width=600, height=420)
        self.stats_container.grid_propagate(False)
        self.stats_container.grid_columnconfigure(0, weight=1)
        self.stats_container.grid_rowconfigure(0, weight=1)
        self.stats_container.grid(row=1, column=0, padx=7, pady=7)

        self.stats_centering_frame = ctk.CTkFrame(self.stats_container, fg_color='transparent')
        self.stats_centering_frame.grid(row=0, column=0)

        self.factory_info = info_widget.InfoWidget(self.stats_centering_frame, 
                                           f"Factories: {self.selected_province.getFactories()}\nOutage Status: {'No Outage' if not self.selected_province.getOutageStatus() else 'Ongoing Outage'}\nDays until Outage\nis Resolved: {'No Outage' if self.selected_province.getOutageTime() == -1 else self.selected_province.getOutageTime()}", 
                                           0, 0,
                                           100, 250,
                                           fg_color='#272C38',
                                           font=('Consolas', 15))
        
        self.terrain_info = info_widget.InfoWidget(self.stats_centering_frame,
                                            f"Terrain Type: {self.selected_province.getTerrainType()}\nMax Factory Limit: {self.selected_province.getMaxFactories()}\nMax Mine Limit: {self.selected_province.getMaxMines()}\nMax Infrastructure Limit: {self.selected_province.getMaxInfrastructureLevel()}",
                                            1, 0,
                                            100, 250,
                                            fg_color='#272C38',
                                            font=('Consolas', 15))
        
        self.mine_info = info_widget.InfoWidget(self.stats_centering_frame,
                                            f"Mines: {self.selected_province.getMines()}\nKnown Resource\nDeposits: {self.selected_province.getAvailableResources()}",
                                            0, 1,
                                            100, 250,
                                            fg_color='#272C38',
                                            font=('Consolas', 15))
        
        self.infrastructure_info = info_widget.InfoWidget(self.stats_centering_frame,
                                            f"Infrastructure Level: {self.selected_province.getInfrastructureLevel()}\nConstruction\nTime In Days: {self.selected_province.getConstructionSpeed()}",
                                            1, 1,
                                            100, 250,
                                            fg_color='#272C38',
                                            font=('Consolas', 15))

    def changeProvince(self, choice : str, game_object : g.GameData):
        index = self.province_names.index(choice)
        self.selected_province = game_object.provinces[index]
        self.updateProvinceView()
    
    def updateProvinceView(self):
        self.province_title.configure(text=self.selected_province.getName().upper())
        self.factory_info.refresh(f"Factories: {self.selected_province.getFactories()}\nOutage Status: {'No Outage' if not self.selected_province.getOutageStatus() else 'Ongoing Outage'}\nDays until Outage\nis Resolved: {'No Outage' if self.selected_province.getOutageTime() == -1 else self.selected_province.getOutageTime()}")
        self.terrain_info.refresh(f"Terrain Type: {self.selected_province.getTerrainType()}\nMax Factory Limit: {self.selected_province.getMaxFactories()}\nMax Mine Limit: {self.selected_province.getMaxMines()}\nMax Infrastructure Limit: {self.selected_province.getMaxInfrastructureLevel()}")
        self.mine_info.refresh(f"Mines: {self.selected_province.getMines()}\nKnown Resource\nDeposits: {self.selected_province.getAvailableResources()}")
        self.infrastructure_info.refresh(f"Infrastructure Level: {self.selected_province.getInfrastructureLevel()}\nConstruction\nTime In Days: {self.selected_province.getConstructionSpeed()}")


