import tkinter as tk
import Systems.time_system as t, Systems.economy_system as e, Data.game_data as g

import customtkinter as ctk

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
        self.tabs.pack(pady=50)

        self.information_tab = self.tabs.add("Information")
        self.provinces_tab = self.tabs.add("View Provinces")
        self.construction_tab = self.tabs.add("Manage Construction")
        self.laws_tab = self.tabs.add("Manage Laws")

        self.tabs.set("Information")

    def changeTab(self, game_object : g.GameData, root : ctk.CTk):
        if self.tabs.get() == 'Information':
            self.displayInformationMenu(game_object, root)
        elif self.tabs.get() == 'View Provinces':
            self.displayProvincesMenu(game_object, root)
        elif self.tabs.get() == 'Manage Construction':
            self.displayConstructionMenu(game_object, root)
        elif self.tabs.get() == 'Manage Laws':
            self.displayLawsAndManagementMenu(game_object, root)

    def displayInformationMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass

    def displayProvincesMenu(self, game_object : g.GameData, root : ctk.CTk):
        frame = ctk.CTkFrame(self.provinces_tab, border_width=10)
        frame.pack()
        for province in game_object.provinces:
            province_stats = ctk.CTkLabel(frame, text=province.printStats())
            province_stats.pack(side="left", padx=10, pady=10)

    def displayConstructionMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass

    def displayLawsAndManagementMenu(self, game_object : g.GameData, root : ctk.CTk):
        pass


def mainGameLoop(game_object : g.GameData):
    window = ctk.CTk()
    window.title("Economy Game")
    window.geometry("1920x1080")
    window.config()


    game_interface = EconomyGameInterface(window, game_object)

    window.mainloop()