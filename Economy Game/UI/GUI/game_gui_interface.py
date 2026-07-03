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
        # Create individual frames to group related statistics
        self.resource_stats = ctk.CTkFrame(self.information_tab, border_width=5, corner_radius=20, width=250, height=250)
        self.economy_stats = ctk.CTkFrame(self.information_tab, border_width=5, corner_radius=20, width=250, height=250)
        self.building_stats = ctk.CTkFrame(self.information_tab, border_width=5, corner_radius=20, width=250, height=250)

        self.resource_stats.grid_propagate(False)
        self.economy_stats.grid_propagate(False)
        self.building_stats.grid_propagate(False)

        self.resource_stats.grid(row=0, column=0, padx=7, pady=7)
        self.economy_stats.grid(row=1, column=0, padx=7, pady=7)
        self.building_stats.grid(row=2, column=0, padx=7, pady=7)

        # Create labels to display statistics 
        self.resource_title = ctk.CTkLabel(self.resource_stats, text="RESOURCES", font=('Bahnschrift Light SemiCondensed', 35, 'bold'))
        self.economy_title = ctk.CTkLabel(self.economy_stats, text="ECONOMY", font=('Bahnschrift Light SemiCondensed', 35, 'bold'))
        self.building_title = ctk.CTkLabel(self.building_stats, text="TOTAL BUILDINGS", font=('Bahnschrift Light SemiCondensed', 27, 'bold'))
        self.resource_label = ctk.CTkLabel(self.resource_stats, text=f"{r.getCoalQuantity(game_object)} coal\n{r.getIronQuantity(game_object)} iron\n{r.getStoneQuantity(game_object)} stone", font=('Consolas', 20))
        self.economy_label = ctk.CTkLabel(self.economy_stats, text=f"Currency: {e.getCurrencyAmount(game_object)}\nDebt: {e.getDebtAmount(game_object)}", font=('Consolas', 20))
        self.building_label = ctk.CTkLabel(self.building_stats, text=f"Total Factories: {e.getTotalFactories(game_object)}\nTotal Mines: {e.getTotalMines(game_object)}", font=('Consolas', 20))

        self.resource_stats.grid_columnconfigure(0, weight=1)
        self.economy_stats.grid_columnconfigure(0, weight=1)
        self.building_stats.grid_columnconfigure(0, weight=1)

        self.resource_title.grid(row=0, column=0, pady=15)
        self.economy_title.grid(row=0, column=0, pady=15)
        self.building_title.grid(row=0, column=0, pady=15)

        self.resource_label.grid(row=1, column=0)
        self.economy_label.grid(row=1, column=0)
        self.building_label.grid(row=1, column=0)

        # Main progress button to progress through the days
        self.progress_button = ctk.CTkButton(self.information_tab, text="PROGRESS TO \nNEXT DAY", command=lambda:self.update(game_object, root), font=('Tahoma', 20, 'bold'), width=400, height=250, border_width=5, corner_radius=20)
        self.progress_button.grid(row=2, column=1,padx=7, pady=7)

        self.construction_stats = ctk.CTkScrollableFrame(self.information_tab, border_width=5, corner_radius=20, width=250, height=500)
        self.construction_stats.grid(row=0, column=2, rowspan=2, padx=7, pady=7)
        self.construction_stats.columnconfigure(0, weight=1)

        self.construction_title = ctk.CTkLabel(self.construction_stats, text="BUILDINGS IN\nCONSTRUCTION", font=('Bahnschrift Light SemiCondensed', 25, 'bold'))
        self.construction_title.grid(row=0, column=0, pady=5)

        self.construction_label = ctk.CTkLabel(self.construction_stats, text=d.returnBuildingsInConstruction(game_object), font=('Consolas', 18))
        self.construction_label.grid(row=1, column=0, pady=8)

    def displayProvincesMenu(self, game_object : g.GameData, root : ctk.CTk):

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

    def displayConstructionMenu(self, game_object : g.GameData, root : ctk.CTk):
        # Create a specific frame where the user can choose what province to construct things in
        self.province_menu_frame = ctk.CTkFrame(self.construction_tab, border_width=5, corner_radius=20, width=250, height=750)
        self.province_menu_frame.grid_propagate(False)
        self.province_menu_frame.grid_columnconfigure(0, weight=1)
        self.province_menu_frame.grid_rowconfigure((0, 1), weight=1)
        #self.province_menu_frame.grid_rowconfigure(1, weight=1)
        self.province_menu_frame.grid(row=0, column=0)

        # Get all province names and store them in an options menu
        self.province_names = [province.getName() for province in game_object.provinces]
        self.selected_province = game_object.provinces[0]

        self.province_options_frame = ctk.CTkFrame(self.province_menu_frame, border_width=5, height=300)

        self.province_options_frame.grid_propagate(False)
        self.province_options_frame.grid_columnconfigure(0, weight=1)
        self.province_options_frame.grid(row=0, column=0)

        self.province_options = ctk.CTkOptionMenu(self.province_options_frame, values=self.province_names, width=100, height=20, font=('Bahnschrift Light SemiCondensed', 20, 'bold'))
        self.province_options.configure(command=lambda choice: self.changeProvinceSelection(choice, game_object))
        self.province_options.set(self.province_names[0])

        self.province_options.grid_propagate(False)
        #self.province_options.grid_columnconfigure(0, weight=1)
        self.province_options.grid(row=0, column=0, pady=15)

        self.construction_hint = ctk.CTkLabel(self.province_options_frame, text="Use the\ndrop down\nmenu to\nchoose a\nprovince.\nThen use\nthe slider\nto configure\n# of buildings.", font=('Consolas', 20))
        self.construction_hint.grid(row=1, column=0)

        self.amount_slider_frame = ctk.CTkFrame(self.province_menu_frame, border_width=5, height=300)

        self.amount_slider_frame.grid_propagate(False)
        self.amount_slider_frame.grid_columnconfigure(0, weight=1)
        self.amount_slider_frame.grid_rowconfigure((0, 1), weight=1)
        self.amount_slider_frame.grid(row=1, column=0)

        self.amount_slider = ctk.CTkSlider(self.amount_slider_frame, from_=1, to=10, number_of_steps=9, orientation="vertical", width=30)
        self.amount_slider.set(1)
        self.current_amount = int(self.amount_slider.get())
        self.amount_label = ctk.CTkLabel(self.amount_slider_frame, text=self.current_amount, font=('Bahnschrift Light SemiCondensed', 30, 'bold'))
        self.amount_label.grid(row=0, column=0, pady=7)
        self.amount_slider.configure(command=self.updateBuildingAmount)
        self.amount_slider.grid(row=1, column=0, pady=7)

        # Create a specific frame to construct factories
        self.factory_construction_frame = ctk.CTkFrame(self.construction_tab, border_width=5, corner_radius=3)
        self.factory_construction_frame.grid(row=0, column=1)

        # Create a specific frame to construct mines
        self.mine_construction_frame = ctk.CTkFrame(self.construction_tab, border_width=5, corner_radius=3)
        self.mine_construction_frame.grid(row=0, column=2)

        # Create a specific frame to construct infrastructure
        self.infrastructure_construction_frame = ctk.CTkFrame(self.construction_tab, border_width=5, corner_radius=3)
        self.infrastructure_construction_frame.grid(row=0, column=3)

        # Create buttons to add
        self.factory_label = ctk.CTkButton(self.factory_construction_frame, text="Add Factories to Queue", command=lambda:self.purchaseFactory(game_object, root))
        self.mine_label = ctk.CTkButton(self.mine_construction_frame, text="Add Factory to Queue")
        self.infrastructure_label = ctk.CTkButton(self.infrastructure_construction_frame, text="Add Factory to Queue")

        #self.factory_label.pack()
        
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
            self.economy_label.configure(text=f"ECONOMY\nCurrency: {e.getCurrencyAmount(game_object)}\nDebt: {e.getDebtAmount(game_object)}")
            self.building_label.configure(text=f"TOTAL BUILDINGS\nTotal Factories: {e.getTotalFactories(game_object)}\nTotal Mines: {e.getTotalMines(game_object)}")
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

        for province in game_object.provinces:
            self.province_stats.configure(text=province.printStats())
            print(province.printStats())
        
        self.resource_label.configure(text=f"{r.getCoalQuantity(game_object)} coal\n{r.getIronQuantity(game_object)} iron\n{r.getStoneQuantity(game_object)} stone")
        self.economy_label.configure(text=f"ECONOMY\nCurrency: {e.getCurrencyAmount(game_object)}\nDebt: {e.getDebtAmount(game_object)}")
        self.building_label.configure(text=f"TOTAL BUILDINGS\nTotal Factories: {e.getTotalFactories(game_object)}\nTotal Mines: {e.getTotalMines(game_object)}")
        self.construction_label.configure(text=d.returnBuildingsInConstruction(game_object))
        


def mainGameLoop(game_object : g.GameData):
    window = ctk.CTk()
    window.title("Economy Game")
    window.geometry("1920x1080")
    window.configure()


    game_interface = EconomyGameInterface(window, game_object)

    window.mainloop()