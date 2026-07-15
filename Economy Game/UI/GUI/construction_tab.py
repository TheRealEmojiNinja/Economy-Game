import customtkinter as ctk, UI.GUI.selector_widget as selector_widget, UI.GUI.spin_box_widget as spin_box_widget, UI.GUI.construction_widget as construction_widget, Systems.development_systems as d, Systems.economy_system as e, Data.game_data as g

from PIL import Image

class ConstructionTab:

    base_size = (35, 35)
    bigger_size = (44, 44)

    icons = {"Plus":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/plus.png'), dark_image=None, size=base_size),
             "Minus":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/minus.png'), dark_image=None, size=base_size),
             "Factory":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/factory.png'), dark_image=None, size=bigger_size),
             "Mine":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/gold-mine.png'), dark_image=None, size=bigger_size),
             "Infrastructure":ctk.CTkImage(light_image=Image.open('Economy Game/Assets/Graphics/road.png'), dark_image=None, size=bigger_size)}
    
    def __init__(self, parent, game_object):

        self.province_names = [province.getName().upper() for province in game_object.provinces]
        self.province_selector = selector_widget.SelectorWidget(parent, 
                                                                "Select a province from\nthe dropdown menu\nto construct\nbuildings in.", 
                                                                self.province_names, self.changeProvinceSelection, game_object)
        self.selected_province = game_object.provinces[0]
        self.province_selector.setValue(self.province_names[0])

        self.current_amount = 1

        self.number_of_buildings_spinbox = spin_box_widget.SpinBoxWidget(parent, 
                                                                         "Choose the\nnumber of\nbuildings to\nadd to the\nconstruction\nqueue.", 
                                                                         self.current_amount, 
                                                                         ConstructionTab.icons["Minus"], ConstructionTab.icons["Plus"], 
                                                                         self.decreaseAmount, self.increaseAmount, game_object)

        self.construction_widget = construction_widget.ConstructionWidget(parent, 1, 1, ConstructionTab.icons["Factory"], ConstructionTab.icons["Mine"], ConstructionTab.icons["Infrastructure"], self.purchaseFactory, self.purchaseMine, self.purchaseInfrastructure)

        self.updateConstructionActions(game_object)
        
    def changeProvinceSelection(self, choice, game_object : g.GameData):
            index = self.province_names.index(choice)
            self.selected_province = game_object.provinces[index]
            #self.updateConstructionActions(game_object)
    
    def updateConstructionActions(self, game_object : g.GameData):
        print("UPDATING")
        factories_can_be_bought = not d.overMaxFactoryLimit(game_object, game_object.provinces.index(self.selected_province), self.current_amount) and d.factoriesCanBeBought(game_object, game_object.provinces.index(self.selected_province), self.current_amount)
        print(self.construction_widget.getFactoryConstructionStatus())
        if factories_can_be_bought and not self.construction_widget.getFactoryConstructionStatus():
            self.construction_widget.enableFactoryConstruction()
        elif not factories_can_be_bought and self.construction_widget.getFactoryConstructionStatus():
            self.construction_widget.disableFactoryConstruction()

    
    def decreaseAmount(self, game_object : g.GameData):
        if self.current_amount > 0:
            self.current_amount -= 1
            self.number_of_buildings_spinbox.enableRightButton()
        
        if self.current_amount == 0:
            self.number_of_buildings_spinbox.disableLeftButton()
        
        self.number_of_buildings_spinbox.refresh(self.current_amount)
        #self.updateConstructionActions(game_object)

    def increaseAmount(self, game_object : g.GameData):
        if self.current_amount < 10:
            self.current_amount += 1
            self.number_of_buildings_spinbox.enableLeftButton()
        
        if self.current_amount == 10:
            self.number_of_buildings_spinbox.disableRightButton()

        self.number_of_buildings_spinbox.refresh(self.current_amount)
        #self.updateConstructionActions(game_object)

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
        result, cost, needed_stone = d.addMinesToQueue(game_object, self.current_amount, game_object.provinces.index(self.selected_province))

        pass

    def purchaseInfrastructure(self, game_object : g.GameData, root : ctk.CTk):
        pass

    def deleteWidget(self, widget : ctk.CTk):
        widget.destroy()
