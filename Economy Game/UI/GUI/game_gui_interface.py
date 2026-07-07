import Systems.time_system as t, Systems.economy_system as e, Systems.resource_system as r, Systems.time_system as t, Systems.development_systems as d, Data.game_data as g

import UI.GUI.information_tab as info, UI.GUI.provinces_tab as prov, UI.GUI.construction_tab as const

import customtkinter as ctk
import random

class EconomyGameInterface:
    def __init__ (self, root, game_object : g.GameData):

        # Set title of game window
        self.title = ctk.CTkLabel(root, text="Economy Game")

        # Create game tab manager and 4 tabs to manage different aspects of the game
        self.tabs = ctk.CTkTabview(root, height=1000, width=1480)
        self.tabs._segmented_button.configure(font=('Tahoma', 17, 'bold'))
        self.tabs.grid(row=0, column=0, pady=5)

        #self.laws_tab = self.tabs.add("Manage Laws")

        self.information_tab = info.InformationTab(self.tabs.add("Information"), game_object)
        self.provinces_tab = prov.ProvinceTab(self.tabs.add("View Provinces"), game_object)
        self.construction_tab = const.ConstructionTab(self.tabs.add("Manage Construction"), game_object)
        self.tabs.tab("Manage Construction")


        # Set starting tab to the information tab
        self.tabs.set("Information")

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



        event = t.updateDay(game_object)

        if event != None:
            self.displayEvent(game_object, root, event)

        #for province in game_object.provinces:
            #self.province_stats.configure(text=province.printStats())
            #print(province.printStats())
        


def mainGameLoop(game_object : g.GameData):
    window = ctk.CTk()
    window.title("Economy Game")
    window.geometry("1920x1080")
    window.configure()


    game_interface = EconomyGameInterface(window, game_object)

    window.mainloop()