import Systems.time_system as t, Systems.economy_system as e, Systems.resource_system as r, Systems.time_system as t, Systems.development_systems as d, Data.game_data as g

import UI.GUI.information_tab as info, UI.GUI.provinces_tab as prov, UI.GUI.construction_tab as const, UI.GUI.info_widget as widget

import customtkinter as ctk
import random
import time

class EconomyGameInterface:
    def __init__ (self, root : ctk.CTk, game_object : g.GameData):

        self.progressing = False

        # Set title of game window
        self.title = ctk.CTkLabel(root, text="Economy Game")

        root.grid_propagate(False)
        root.grid_columnconfigure(0, weight=1)

        # Create game tab manager and 4 tabs to manage different aspects of the game
        self.tabs = ctk.CTkTabview(root, height=650, width=1480, fg_color='#2f3542')
        self.tabs._segmented_button.configure(font=('Tahoma', 17, 'bold'))
        self.tabs.grid(row=0, column=0, pady=13)

        #self.laws_tab = self.tabs.add("Manage Laws")

        #self.information_tab = info.InformationTab(self.tabs.add("Information"), game_object)
        #self.provinces_tab = prov.ProvinceTab(self.tabs.add("View Provinces"), game_object)
        #self.construction_tab = const.ConstructionTab(self.tabs.add("Manage Construction"), game_object)
        #self.tabs.tab("Manage Construction")

        self.control_panel_frame = ctk.CTkFrame(root, fg_color='#252A34', width=1480)
        self.control_panel_frame.grid_propagate(False)
        self.control_panel_frame.grid_rowconfigure((0,1,2), weight=1)
        self.control_panel_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.control_panel_frame.grid(row=1, column=0)

        #self.resource_frame = ctk.CTkFrame(self.control_panel_frame, corner_radius=10, height=60, fg_color='#343B4A')
        #self.resource_frame.grid(row=0, column=0, padx=10, pady=10)

        self.day_label = widget.InfoWidget(self.control_panel_frame, 
                                                f"Day {game_object.day}", 
                                                0, 0)
        
        self.currency_label = widget.InfoWidget(self.control_panel_frame, 
                                                f"{e.getCurrencyAmount(game_object)} currency", 
                                                1, 0)
        
        self.satisfaction_label = widget.InfoWidget(self.control_panel_frame, 
                                                f"{game_object.satisfaction} satisfaction", 
                                                2, 0)
        
        self.factories_label = widget.InfoWidget(self.control_panel_frame, 
                                                 f"{e.getTotalFactories(game_object)} factories", 
                                                 0, 1)
        
        self.mines_label = widget.InfoWidget(self.control_panel_frame, 
                                                 f"{e.getTotalMines(game_object)} mines", 
                                                 1, 1)
        
        self.coal_label = widget.InfoWidget(self.control_panel_frame, 
                                                 f"{r.getCoalQuantity(game_object)} coal", 
                                                 0, 3)
        
        self.iron_label = widget.InfoWidget(self.control_panel_frame, 
                                                 f"{r.getIronQuantity(game_object)} iron", 
                                                 1, 3)
        
        self.stone_label = widget.InfoWidget(self.control_panel_frame, 
                                                 f"{r.getStoneQuantity(game_object)} stone", 
                                                 2, 3)

        

        self.button_frame = ctk.CTkFrame(self.control_panel_frame, corner_radius=10, height=180, width=200, fg_color='#2E3542')
        #self.button_frame.grid_propagate(False)
        self.button_frame.grid(row=0, column=2, rowspan=3, padx=5, pady=5)
        
        #self.progress_button = ctk.CTkButton(self.button_frame, text="PLAY", command=lambda:self.toggleProgress(game_object, root))
        #self.progress_button.grid(row=0, column=0)


        # Set starting tab to the information tab
        #self.tabs.set("Information")

    def toggleProgress(self, game_object : g.GameData, root : ctk.CTk):
        if not self.progressing: 
            self.progressing = True
            self.progress_button.configure(text="PAUSE")
            self.advanceTime(game_object, root)
        elif self.progressing: 
            self.progressing = False
            self.progress_button.configure(text="PLAY")

        print(self.progressing)

    def advanceTime(self, game_object : g.GameData, root : ctk.CTk):
        self.update(game_object, root)

        if self.progressing:
            root.after(2000, self.advanceTime, game_object, root)

    def displayEvent(self, game_object : g.GameData, root : ctk.CTk, event : str):
        event_frame = ctk.CTkFrame(root, border_width=3, corner_radius=3)
        event_frame.place(x=random.randint(100, 1020), y=random.randint(100, 680))
        event_label = ctk.CTkLabel(event_frame, text=event)
        event_button = ctk.CTkButton(event_frame, text="CLOSE", command=lambda:self.deleteWidget(event_frame))
        event_label.pack(padx=10, pady=10)
        event_button.pack(padx=10, pady=10)

    def deleteWidget(self, widget : ctk.CTk):
        widget.destroy()
        

    def update(self, game_object : g.GameData, root : ctk.CTk):

        print("progressing")

        event = t.updateDay(game_object)

        if event != None:
            self.displayEvent(game_object, root, event)

        #for province in game_object.provinces:
            #self.province_stats.configure(text=province.printStats())
            #print(province.printStats())
        


def mainGameLoop(game_object : g.GameData):
    window = ctk.CTk(fg_color='#1B1E24')
    window.title("Economy Game")
    window.geometry("1920x1080")
    window.configure()


    game_interface = EconomyGameInterface(window, game_object)

    window.mainloop()