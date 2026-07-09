import customtkinter as ctk, Systems.resource_system as r, Systems.economy_system as e, Systems.development_systems as d, Data.game_data as g, UI.GUI.statistic_widget as widget

class InformationTab:
    def __init__(self, parent, game_object):

        self.resource_stats = widget.StatisticWidget(parent, 
                                                     "RESOURCES", 
                                                     f"{r.getCoalQuantity(game_object)} coal\n{r.getIronQuantity(game_object)} iron\n{r.getStoneQuantity(game_object)} stone",
                                                     0,
                                                     0)
        
        self.economy_stats = widget.StatisticWidget(parent,
                                                    "ECONOMY",
                                                    f"{e.getCurrencyAmount(game_object)} currency\n{e.getDebtAmount(game_object)} in debt",
                                                    1,
                                                    0)
        
        self.building_stats = widget.StatisticWidget(parent,
                                                     "TOTAL\nBUILDINGS",
                                                     f"{e.getTotalFactories(game_object)} total factories\n{e.getTotalMines(game_object)} total mines",
                                                     2,
                                                     0)

        # Main progress button to progress through the days
        #self.progress_button = ctk.CTkButton(parent, text="PROGRESS TO \nNEXT DAY", command=lambda:self.refreshValues(game_object), font=('Tahoma', 20, 'bold'), width=400, height=250, border_width=5, corner_radius=20)
        #self.progress_button.grid(row=2, column=1,padx=7, pady=7)

        self.construction_stats = ctk.CTkScrollableFrame(parent, border_width=5, corner_radius=20, width=250, height=500)
        self.construction_stats.grid(row=0, column=2, rowspan=2, padx=7, pady=7)
        self.construction_stats.columnconfigure(0, weight=1)

        self.construction_title = ctk.CTkLabel(self.construction_stats, text="BUILDINGS IN\nCONSTRUCTION", font=('Bahnschrift Light SemiCondensed', 25, 'bold'))
        self.construction_title.grid(row=0, column=0, pady=5)

        self.construction_label = ctk.CTkLabel(self.construction_stats, text=d.returnBuildingsInConstruction(game_object), font=('Consolas', 18))
        self.construction_label.grid(row=1, column=0, pady=8)

        self.instructions_frame = ctk.CTkFrame(parent, border_width=5, corner_radius=20, width=400, height=550)
        self.instructions_frame.grid_propagate(False)
        self.instructions_frame.grid(row=0, column=1, rowspan=2)

        self.instruction_title = ctk.CTkLabel(self.instructions_frame, text="DASHBOARD", font=('Bahnschrift Light SemiCondensed', 35, 'bold'))
        self.instructions_label = ctk.CTkLabel(self.instructions_frame, text="Factories generate money.\nMines generate resources.\nInfrastructure reduces\nconstruction time.\nKeep a minimum\namount of currency\nto prepare for\nrandom disasters.", font=('Consolas', 20))
        self.instructions_frame.grid_columnconfigure(0, weight=1)
        self.instruction_title.grid(row=0, column=0, pady=10)
        self.instructions_label.grid(row=1, column=0, pady=10)

    def refreshValues(self, game_object : g.GameData):
        self.resource_stats.refresh(f"{r.getCoalQuantity(game_object)} coal\n{r.getIronQuantity(game_object)} iron\n{r.getStoneQuantity(game_object)} stone")
        self.economy_stats.refresh(f"{e.getCurrencyAmount(game_object)} currency\n{e.getDebtAmount(game_object)} in debt")
        self.building_stats.refresh(f"{e.getTotalFactories(game_object)} total factories\n{e.getTotalMines(game_object)} total mines")
        self.construction_label.configure(text=d.returnBuildingsInConstruction(game_object))

        # Implement start/stop button that will automatically progress the game through the days instead of having to click the button every time
