import customtkinter as ctk, UI.GUI.construction_widget as const_widget, UI.GUI.selector_widget as selector_widget, Systems.economy_system as e, Data.game_data as g

class ConstructionTab:
    def __init__(self, parent, game_object):

        # Create a specific frame where the user can choose what province to construct things in
        #parent, corner_radius=10, width=300, height=500, fg_color='#292F3B'
        #self.province_menu_frame = ctk.CTkFrame(parent, border_width=5, corner_radius=20, width=250, height=750)
        #self.province_menu_frame.grid_propagate(False)
        #self.province_menu_frame.grid_columnconfigure(0, weight=1)
        #self.province_menu_frame.grid_rowconfigure((0, 1), weight=1)
        #self.province_menu_frame.grid_rowconfigure(1, weight=1)
        #self.province_menu_frame.grid(row=0, column=0, rowspan=20, padx=7, pady=7)

        self.province_names = [province.getName().upper() for province in game_object.provinces]
        self.province_selector = selector_widget.SelectorWidget(parent, "Select a province from\nthe dropdown menu\nto construct\nbuildings in.", self.province_names, self.changeProvinceSelection, game_object)
        self.selected_province = game_object.provinces[0]
        self.province_selector.setValue(self.province_names[0])

        # Get all province names and store them in an options menu
        #self.province_names = [province.getName() for province in game_object.provinces]
        #self.selected_province = game_object.provinces[0]

        #self.province_options_frame = ctk.CTkFrame(self.province_menu_frame, border_width=5, height=300)

        #self.province_options_frame.grid_propagate(False)
        #self.province_options_frame.grid_columnconfigure(0, weight=1)
        #self.province_options_frame.grid(row=0, column=0)

        #self.province_options = ctk.CTkOptionMenu(self.province_options_frame, values=self.province_names, width=100, height=20, font=('Bahnschrift Light SemiCondensed', 20, 'bold'))
        #self.province_options.configure(command=lambda choice: self.changeProvinceSelection(choice, game_object))
        #self.province_options.set(self.province_names[0])

        #self.province_options.grid_propagate(False)
        #self.province_options.grid_columnconfigure(0, weight=1)
        #self.province_options.grid(row=0, column=0, pady=15)

        self.current_amount = 1

        self.spin_box_frame = ctk.CTkFrame(parent, corner_radius=10, width=300, height=300, fg_color='#292F3B')
        self.spin_box_frame.grid_propagate(False)
        self.spin_box_frame.grid_columnconfigure(0, weight=1)
        self.spin_box_frame.grid_rowconfigure(0, weight=1)
        self.spin_box_frame.grid(row=0, column=1)

        self.subtract_button = ctk.CTkButton(self.spin_box_frame, text='-', command=self.decreaseAmount)
        self.subtract_button.grid(row=0, column=0, padx=5)

        self.number_label = ctk.CTkLabel(self.spin_box_frame, text=self.current_amount)
        self.number_label.grid(row=0, column=1, padx=5)

        self.add_button = ctk.CTkButton(self.spin_box_frame, text='+', command=self.increaseAmount)
        self.add_button.grid(row=0, column=2, padx=5)

        #self.amount_slider_frame = ctk.CTkFrame(self.province_menu_frame, border_width=5, height=300)

        #self.amount_slider_frame.grid_propagate(False)
        #self.amount_slider_frame.grid_columnconfigure(0, weight=1)
        #self.amount_slider_frame.grid_rowconfigure((0, 1), weight=1)
        #self.amount_slider_frame.grid(row=1, column=0)

        #self.amount_slider = ctk.CTkSlider(self.amount_slider_frame, from_=1, to=10, number_of_steps=9, orientation="vertical", width=30)
        #self.amount_slider.set(1)
        #self.current_amount = int(self.amount_slider.get())
        #self.amount_label = ctk.CTkLabel(self.amount_slider_frame, text=self.current_amount, font=('Bahnschrift Light SemiCondensed', 30, 'bold'))
        #self.amount_label.grid(row=0, column=0, pady=7)
        #self.amount_slider.configure(command=self.updateBuildingAmount)
        #self.amount_slider.grid(row=1, column=0, pady=7)


        '''self.factory_construction_panel = const_widget.ConstructionWidget(parent, 
                                                                    "Add Factories\nto Queue", 
                                                                    f"A Factory costs\n{e.getCostOfFactory()} currency\nand {e.getRequiredIronOfFactory()} iron", 
                                                                    0, 
                                                                    1, 
                                                                    self.purchaseFactory(game_object, parent))

        self.mine_construction_panel = const_widget.ConstructionWidget(parent,
                                                                 "Add Mines\nto Queue",
                                                                 f"A Mine costs\n{e.getCostOfMine()} currency\nand {e.getRequiredStoneOfMine()} stone",
                                                                 0,
                                                                 2,
                                                                 self.purchaseMine(game_object, parent))
        
        self.infrastructure_construction_panel = const_widget.ConstructionWidget(parent,
                                                                           "Add\nInfrastructure\nto Queue",
                                                                           f"Infrastructure costs\n{e.getCostOfInfrastructure()} currency\nand {e.getRequiredStoneOfInfrastructure()} stone",
                                                                           0,
                                                                           3,
                                                                           self.purchaseInfrastructure(game_object, parent))'''

    def changeProvinceSelection(self, choice, game_object : g.GameData):
            index = self.province_names.index(choice)
            self.selected_province = game_object.provinces[index]

    def updateBuildingAmount(self, value):
        self.current_amount = int(value)
        self.amount_label.configure(text=int(value))
    
    def decreaseAmount(self):
        if self.current_amount > 0:
            self.current_amount -= 1
            self.add_button.configure(state="normal")
        
        if self.current_amount == 0:
            self.subtract_button.configure(state="disabled")
        
        self.number_label.configure(text=self.current_amount)

    def increaseAmount(self):
        if self.current_amount < 10:
            self.current_amount += 1
            self.subtract_button.configure(state="normal")
        
        if self.current_amount == 10:
            self.add_button.configure(state="disabled")

        self.number_label.configure(text=self.current_amount)

    def purchaseFactory(self, game_object : g.GameData, root : ctk.CTk):
        '''print(self.current_amount)
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
        button.pack(padx=10, pady=10)'''
        pass

    def purchaseMine(self, game_object : g.GameData, root : ctk.CTk):
        pass

    def purchaseInfrastructure(self, game_object : g.GameData, root : ctk.CTk):
        pass

    def deleteWidget(self, widget : ctk.CTk):
        widget.destroy()
