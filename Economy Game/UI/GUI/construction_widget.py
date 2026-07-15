import customtkinter as ctk, CTkToolTip as ctktooltip, Systems.economy_system as e


class ConstructionWidget:

    button_font = ('Bahnschrift Light SemiCondensed', 25, 'bold')
    text_font = ('Consolas', 20)

    def __init__(self, parent, row : int, col : int, image_one, image_two, image_three, game_object, function_one, function_two, function_three):

        self.container_frame = ctk.CTkFrame(parent, corner_radius=10, width=250, height=250, fg_color='#292F3B')
        self.container_frame.grid_propagate(False)
        self.container_frame.grid_columnconfigure(0, weight=1)
        self.container_frame.grid_rowconfigure(0, weight=1)
        self.container_frame.grid(row=row, column=col, padx=7, pady=7)

        self.centering_frame = ctk.CTkFrame(self.container_frame, fg_color='transparent')
        self.centering_frame.grid(row=0, column=0)

        self.factory_construction = ctk.CTkButton(self.centering_frame, image=image_one, text='', fg_color='#232633', hover_color='#3E455A', height=60, width=60, command=lambda:function_one(game_object))
        self.factory_construction.grid(row=0, column=0, padx=5)
        self.factory_tool_tip = ctktooltip.CTkToolTip(self.factory_construction, message=f"A factory costs {e.getCostOfFactory()} currency and {e.getRequiredIronOfFactory()} iron.", delay=0)

        self.mine_construction = ctk.CTkButton(self.centering_frame, image=image_two, text='', fg_color='#232633', hover_color='#3E455A', height=60, width=60, command=lambda:function_two(game_object))
        self.mine_construction.grid(row=0, column=1, padx=5)
        self.mine_tool_tip = ctktooltip.CTkToolTip(self.mine_construction, message=f"A mine costs {e.getCostOfMine()} currency and {e.getRequiredStoneOfMine()} stone.", delay=0)

        self.infrastructure_construction = ctk.CTkButton(self.centering_frame, image=image_three, text='', fg_color='#232633', hover_color='#3E455A', height=60, width=60, command=lambda:function_three(game_object))
        self.infrastructure_construction.grid(row=0, column=2, padx=5)
        self.infrastructure_tool_tip = ctktooltip.CTkToolTip(self.infrastructure_construction, message=f"An infrastructure level costs {e.getCostOfInfrastructure()} currency and {e.getRequiredStoneOfInfrastructure()} stone.", delay=0)

    def disableFactoryConstruction(self):
        self.factory_construction.configure(state="disabled")
        #self.factory_tool_tip.configure(f"Either you are building over the limit, or you cannot afford these many factories!")

    def enableFactoryConstruction(self):
        self.factory_construction.configure(state="normal")
        #self.factory_tool_tip.configure(f"A factory costs {e.getCostOfFactory()} currency and {e.getRequiredIronOfFactory()} iron.")
    
    def disableMineConstruction(self):
        self.mine_construction.configure(state="disabled")
        #self.mine_tool_tip.configure(f"Either you are building over the limit, or you cannot afford these many mines!")

    def enableMineConstruction(self):
        self.mine_construction.configure(state="normal")
        #self.mine_tool_tip.configure(f"A mine costs {e.getCostOfMine()} currency and {e.getRequiredStoneOfMine()} stone.")

    def disableInfrastructureonstruction(self):
        self.infrastructure_construction.configure(state="disabled")
        #self.infrastructure_tool_tip.configure(f"Either you are building over the limit, or you cannot afford these many infrastructure levels!")
    
    def enableInfrastructureConstruction(self):
        self.infrastructure_construction.configure(state="normal")
        #self.infrastructure_tool_tip.configure(f"An infrastructure level costs {e.getCostOfInfrastructure()} currency and {e.getRequiredStoneOfInfrastructure()} stone.")

    def getFactoryConstructionStatus(self):
        return True if self.factory_construction.cget("state") == "normal" else False
    
    def getMineConstructionStatus(self):
        return True if self.mine_construction.cget("state") == "normal" else False
    
    def getInfrastructureConstructionStatus(self):
        return True if self.infrastructure_construction.cget("state") == "normal" else False
