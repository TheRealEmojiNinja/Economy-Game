import tkinter as tk
import Systems.time_system as t, Systems.economy_system as e, Systems.resource_system as r, Systems.time_system as t, Data.game_data as g

import customtkinter as ctk
import random

'''def mainGameLoop(game_object : g.GameData):
    window = tk.Tk()
    window.title("Economy Game")
    window.geometry("1920x1080")
    window.config(background="#000000")

    test_label = tk.Label(window, text=f"{e.getCurrencyAmount(game_object)}")
    test_label.pack()

    progression_button = tk.Button(window, text="CONTINUE TO NEXT DAY", font=('Courier New', 16), command=lambda: t.updateDay(game_object))
    progression_button.pack()


    window.mainloop()


def mainMenu(game_object : g.GameData, game_window : tk.Tk):
    pass

def updateLabel(game_object : g.GameData, game_window : tk.Tk, label : tk.Label):
    pass'''

class EconomyGameInterface:
    def __init__ (self, root, game_object : g.GameData):

        self.title = ctk.CTkLabel(root, text="Economy Game")

        self.tabs = ctk.CTkTabview(root, height=800, width=1480, command=lambda:self.changeTab(game_object, root))
        self.tabs.pack(pady=10)

        self.information_tab = self.tabs.add("Information")
        self.provinces_tab = self.tabs.add("View Provinces")
        self.construction_tab = self.tabs.add("Manage Construction")
        self.laws_tab = self.tabs.add("Manage Laws")

        self.displayInformationMenu(game_object, root)
        self.displayProvincesMenu(game_object, root)
        self.displayConstructionMenu(game_object, root)
        self.displayLawsAndManagementMenu(game_object, root)

        self.tabs.set("Information")

        self.progress_button = ctk.CTkButton(root, text="PROGRESS TO NEXT DAY", command=lambda:self.update(game_object, root))
        self.progress_button.pack()

    def changeTab(self, game_object : g.GameData, root : ctk.CTk):
        if self.tabs.get() == 'Information':
            self.tabs.set("Information")
        elif self.tabs.get() == 'View Provinces':
            self.tabs.set("View Provinces")
        elif self.tabs.get() == 'Manage Construction':
            self.tabs.set("Manage Construction")
        elif self.tabs.get() == 'Manage Laws':
            self.tabs.set("Manage Laws")

    def displayInformationMenu(self, game_object : g.GameData, root : ctk.CTk):
        self.resource_stats = ctk.CTkFrame(self.information_tab, border_width=5, corner_radius=3)
        self.economy_stats = ctk.CTkFrame(self.information_tab, border_width=5, corner_radius=3)
        self.building_stats = ctk.CTkFrame(self.information_tab, border_width=5, corner_radius=3)

        self.resource_stats.grid(row=0, column=0, padx=20, pady=20)
        self.economy_stats.grid(row=0, column=1, padx=20, pady=20)
        self.building_stats.grid(row=0, column=2, padx=20, pady=20)

        self.resource_label = ctk.CTkLabel(self.resource_stats, text=f"RESOURCES\nCoal: {r.getCoalQuantity(game_object)}\nIron: {r.getIronQuantity(game_object)}\nStone: {r.getStoneQuantity(game_object)}", border_width=3, corner_radius=5)
        self.economy_label = ctk.CTkLabel(self.economy_stats, text=f"ECONOMY\nCurrency: {e.getCurrencyAmount(game_object)}\nDebt: {e.getDebtAmount(game_object)}", border_width=3, corner_radius=5)
        self.building_label = ctk.CTkLabel(self.building_stats, text=f"TOTAL BUILDINGS\nTotal Factories: {e.getTotalFactories(game_object)}\nTotal Mines: {e.getTotalMines(game_object)}", border_width=3, corner_radius=5)

        self.resource_label.pack()
        self.economy_label.pack()
        self.building_label.pack()

    def displayProvincesMenu(self, game_object : g.GameData, root : ctk.CTk):

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
                j += 1

    def displayConstructionMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass

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

        for province in game_object.provinces:
            self.province_stats.configure(text=province.printStats())
            print(province.printStats())
        
        self.resource_label.configure(text=f"RESOURCES\nCoal: {r.getCoalQuantity(game_object)}\nIron: {r.getIronQuantity(game_object)}\nStone: {r.getStoneQuantity(game_object)}")
        self.economy_label.configure(text=f"ECONOMY\nCurrency: {e.getCurrencyAmount(game_object)}\nDebt: {e.getDebtAmount(game_object)}")
        self.building_label.configure(text=f"TOTAL BUILDINGS\nTotal Factories: {e.getTotalFactories(game_object)}\nTotal Mines: {e.getTotalMines(game_object)}")
        


def mainGameLoop(game_object : g.GameData):
    window = ctk.CTk()
    window.title("Economy Game")
    window.geometry("1920x1080")
    window.configure()


    game_interface = EconomyGameInterface(window, game_object)

    window.mainloop()