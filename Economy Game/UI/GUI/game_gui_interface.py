import Systems.time_system as t, Systems.economy_system as e, Systems.resource_system as r, Systems.time_system as t, Systems.development_systems as d, Data.game_data as g

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

        self.information_tab = self.tabs.add("Information")
        self.provinces_tab = self.tabs.add("View Provinces")
        self.construction_tab = self.tabs.add("Manage Construction")
        self.laws_tab = self.tabs.add("Manage Laws")

        # Load all menus initially
        self.displayInformationMenu(game_object, root)
        self.displayProvincesMenu(game_object, root)
        self.displayConstructionMenu(game_object, root)
        self.displayLawsAndManagementMenu(game_object, root)

        # Set starting tab to the information tab
        self.tabs.set("Information")

    def displayInformationMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass

    def displayProvincesMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass

    def displayConstructionMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass
        
    def changeProvinceSelection(self, choice, game_object : g.GameData):
        index = self.province_names.index(choice)
        self.selected_province = game_object.provinces[index]

    def updateBuildingAmount(self, value):
        self.current_amount = int(value)
        self.amount_label.configure(text=int(value))

    def purchaseFactory(self, game_object : g.GameData, root : ctk.CTk):
        print(self.current_amount)
        result, cost, needed_iron = d.addFactoriesToQueue(game_object, self.current_amount, game_object.provinces.index(self.selected_province))
        result_frame = ctk.CTkFrame(root, border_width=3, corner_radius=3)
        result_frame.place(x=560, y=540)

        if result:
            result_text = f"Purchase successful! {self.current_amount} factories are now currently being constructed for {cost} currency and {needed_iron} iron!"
            self.construction_label.configure(text=d.returnBuildingsInConstruction(game_object))
            self.resource_label.configure(text=f"{r.getCoalQuantity(game_object)} coal\n{r.getIronQuantity(game_object)} iron\n{r.getStoneQuantity(game_object)} stone")
            self.economy_label.configure(text=f"{e.getCurrencyAmount(game_object)} currency\n{e.getDebtAmount(game_object)} in debt")
            self.building_label.configure(text=f"{e.getTotalFactories(game_object)} total factories\n{e.getTotalMines(game_object)} total mines")
        else:
            result_text = f"Either you are building over the remaining factory slots, or you cannot afford {self.current_amount} factories for {cost} currency and {needed_iron} iron."

        result_label = ctk.CTkLabel(result_frame, text=result_text)
        button = ctk.CTkButton(result_frame, text="CLOSE", command=lambda:self.deleteWidget(result_frame))

        result_label.pack(padx=10, pady=10)
        button.pack(padx=10, pady=10)

    def displayLawsAndManagementMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass

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