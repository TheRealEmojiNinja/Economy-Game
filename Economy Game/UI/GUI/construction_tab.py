import customtkinter as ctk, UI.GUI.construction_widget as const_widget, UI.GUI.selector_widget as selector_widget, Systems.economy_system as e, Data.game_data as g

from PIL import Image

class ConstructionTab:

    base_size = (35, 35)

    icons = {"Plus":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/plus.png'), dark_image=None, size=base_size),
             "Minus":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/minus.png'), dark_image=None, size=base_size),
             "Factory":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/factory.png'), dark_image=None, size=base_size),
             "Mine":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/gold-mine.png'), dark_image=None, size=base_size),
             "Infrastructure":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/road.png'), dark_image=None, size=base_size)}
    
    def __init__(self, parent, game_object):

        self.province_names = [province.getName().upper() for province in game_object.provinces]
        self.province_selector = selector_widget.SelectorWidget(parent, "Select a province from\nthe dropdown menu\nto construct\nbuildings in.", self.province_names, self.changeProvinceSelection, game_object)
        self.selected_province = game_object.provinces[0]
        self.province_selector.setValue(self.province_names[0])

        self.current_amount = 1

        self.number_change_frame = ctk.CTkFrame(parent, corner_radius=10, width=250, height=250, fg_color='#292F3B')
        self.number_change_frame.grid_propagate(False)
        self.number_change_frame.grid_columnconfigure(0, weight=1)
        self.number_change_frame.grid_rowconfigure(0, weight=1)
        self.number_change_frame.grid(row=0, column=1)

        self.spin_box_frame = ctk.CTkFrame(self.number_change_frame, corner_radius=10, width=250, height=250, fg_color='#2D3341')
        self.spin_box_frame.grid_propagate(False)
        self.spin_box_frame.grid_columnconfigure(0, weight=1)
        self.spin_box_frame.grid_rowconfigure(0, weight=1)
        self.spin_box_frame.grid(row=0, column=0, padx=10, pady=10)

        self.instruction_label = ctk.CTkLabel(self.spin_box_frame, text="Choose the\nnumber of\nbuildings to\nadd to the\nconstruction\nqueue.", font=('Consolas', 20))
        self.instruction_label.grid(row=0, column=0, pady=5)

        self.spin_box_centering_frame = ctk.CTkFrame(self.spin_box_frame, fg_color='transparent')
        self.spin_box_centering_frame.grid(row=1, column=0, pady=7)

        self.subtract_button = ctk.CTkButton(self.spin_box_centering_frame, image=ConstructionTab.icons["Minus"], text='', command=self.decreaseAmount, fg_color='#232633', hover_color='#3E455A', height=50, width=50)
        self.subtract_button.grid(row=0, column=0, padx=10)

        self.number_label = ctk.CTkLabel(self.spin_box_centering_frame, text=self.current_amount, font=('Bahnschrift Light SemiCondensed', 30, 'bold'), width=30, height=50)
        self.number_label.grid(row=0, column=1, padx=5)

        self.add_button = ctk.CTkButton(self.spin_box_centering_frame, image=ConstructionTab.icons["Plus"], text='', command=self.increaseAmount, fg_color='#232633', hover_color='#3E455A', height=50, width=50)
        self.add_button.grid(row=0, column=2, padx=10)

        '''self.factory_construction_panel = const_widget.ConstructionWidget(parent, 
                                                                    "Add Factories\nto Queue", 
                                                                    f"A Factory costs\n{e.getCostOfFactory()} currency\nand {e.getRequiredIronOfFactory()} iron", 
                                                                    0, 
                                                                    2, 
                                                                    self.purchaseFactory(game_object, parent))

        self.mine_construction_panel = const_widget.ConstructionWidget(parent,
                                                                 "Add Mines\nto Queue",
                                                                 f"A Mine costs\n{e.getCostOfMine()} currency\nand {e.getRequiredStoneOfMine()} stone",
                                                                 1,
                                                                 2,
                                                                 self.purchaseMine(game_object, parent))
        
        self.infrastructure_construction_panel = const_widget.ConstructionWidget(parent,
                                                                           "Add\nInfrastructure\nto Queue",
                                                                           f"Infrastructure costs\n{e.getCostOfInfrastructure()} currency\nand {e.getRequiredStoneOfInfrastructure()} stone",
                                                                           2,
                                                                           2,
                                                                           self.purchaseInfrastructure(game_object, parent))'''
        
        self.construction_frame = ctk.CTkFrame(parent, corner_radius=10, width=250, height=250, fg_color='#292F3B')
        self.construction_frame.grid_propagate(False)
        self.construction_frame.grid_columnconfigure(0, weight=1)
        self.construction_frame.grid_rowconfigure(0, weight=1)
        self.construction_frame.grid(row=1, column=1)

        self.construction_centering_frame = ctk.CTkFrame(self.construction_frame, fg_color='transparent')
        self.construction_centering_frame.grid(row=0, column=0)

        self.factory_construction = ctk.CTkButton(self.construction_centering_frame, image=ConstructionTab.icons["Factory"], text='', fg_color='#232633', hover_color='#3E455A', height=50, width=50)
        self.factory_construction.grid(row=0, column=0, padx=5)

        self.mine_construction = ctk.CTkButton(self.construction_centering_frame, image=ConstructionTab.icons["Mine"], text='', fg_color='#232633', hover_color='#3E455A', height=50, width=50)
        self.mine_construction.grid(row=0, column=1, padx=5)

        self.infrastructure_construction = ctk.CTkButton(self.construction_centering_frame, image=ConstructionTab.icons["Infrastructure"], text='', fg_color='#232633', hover_color='#3E455A', height=50, width=50)
        self.infrastructure_construction.grid(row=0, column=2, padx=5)
        

    def changeProvinceSelection(self, choice, game_object : g.GameData):
            index = self.province_names.index(choice)
            self.selected_province = game_object.provinces[index]
    
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
