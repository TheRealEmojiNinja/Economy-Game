import customtkinter as ctk, Systems.resource_system as r, Systems.economy_system as e, Systems.development_systems as d, Data.game_data as g

class InformationTab:
    def __init__(self, parent, game_object):

        self.instructions_frame = ctk.CTkFrame(parent, border_width=5, corner_radius=20, width=400, height=550)
        self.instructions_frame.grid_propagate(False)
        self.instructions_frame.grid(row=0, column=1, rowspan=2)

        self.instruction_title = ctk.CTkLabel(self.instructions_frame, text="DASHBOARD", font=('Bahnschrift Light SemiCondensed', 35, 'bold'))
        self.instructions_label = ctk.CTkLabel(self.instructions_frame, text="Factories generate money.\nMines generate resources.\nInfrastructure reduces\nconstruction time.\nKeep a minimum\namount of currency\nto prepare for\nrandom disasters.", font=('Consolas', 20))
        self.instructions_frame.grid_columnconfigure(0, weight=1)
        self.instruction_title.grid(row=0, column=0, pady=10)
        self.instructions_label.grid(row=1, column=0, pady=10)

    def refreshValues(self, game_object : g.GameData):
        pass
