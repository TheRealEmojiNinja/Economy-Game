import customtkinter as ctk, Systems.resource_system as r, Systems.Events.event_system as event, Systems.development_systems as d, Data.game_data as g, UI.GUI.scrollable_widget as scrollable_widget

class DashBoardTab:
    def __init__(self, parent, game_object):

        self.game_rules_container = ctk.CTkFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.game_rules_container.grid_propagate(False)
        self.game_rules_container.grid_columnconfigure(0, weight=1)
        self.game_rules_container.grid_rowconfigure(0, weight=1)
        self.game_rules_container.grid(row=0, column=0, padx=7, pady=7)

        self.game_rules_centering_frame = ctk.CTkFrame(self.game_rules_container, fg_color='transparent')
        self.game_rules_centering_frame.grid(row=0, column=0)

        self.game_rules_title = ctk.CTkLabel(self.game_rules_centering_frame, text="LEADER'S GUIDE\nON RUNNING THE\nECONOMY\n", font=('Bahnschrift Light SemiCondensed', 25, 'bold'))
        self.game_rules_title.grid(row=0, column=0, pady=5)

        self.game_rules_info = ctk.CTkLabel(self.game_rules_centering_frame, text="▪ Each province has a\nunique number of buildings.\n▪ Factories generate money,\ncaves allow resource gathering,\nand infrastructure reduces\nconstruction time.\n▪ Construct more buildings\nwith resources.", font=('Consolas', 15))
        self.game_rules_info.grid(row=1, column=0, pady=5)


        self.event_history_widget = scrollable_widget.ScrollableWidget(parent, "EVENT HISTORY", event.getEventHistory(game_object), 0, 1)

        '''self.event_history_container = ctk.CTkScrollableFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.event_history_container.grid_columnconfigure(0, weight=1)
        self.event_history_container.grid(row=0, column=1, padx=7, pady=7)


        self.construction_stats = ctk.CTkScrollableFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.construction_stats.grid(row=0, column=2, rowspan=20, padx=7, pady=7)
        self.construction_stats.columnconfigure(0, weight=1)

        self.construction_title = ctk.CTkLabel(self.construction_stats, text="BUILDINGS IN\nCONSTRUCTION", font=('Bahnschrift Light SemiCondensed', 25, 'bold'))
        self.construction_title.grid(row=0, column=0, pady=5)

        self.construction_label = ctk.CTkLabel(self.construction_stats, text=d.returnBuildingsInConstruction(game_object), font=('Consolas', 18))
        self.construction_label.grid(row=1, column=0, pady=8)'''

    def refreshValues(self, game_object : g.GameData):
        self.event_history_widget.refresh(event.getEventHistory(game_object))
