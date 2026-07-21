import customtkinter as ctk, Systems.Resource.raw_resource_system as r, Systems.Events.event_system as event, Systems.Development.general_development as d, Data.game_data as g, UI.GUI.scrollable_widget as scrollable_widget

class DashBoardTab:

    rules = ['This official government guide will help you navigate the different challenges that come with running the economy. Use the arrows below to flip between pages.',
             'Below in the main control panel you will see an assortment of information. You can hover over each to get a brief description via tooltips. The panel also contains the main buttons to facilitate the progress of ingame time.',
             'There are three types of buildings you are able to construct, provided you have the resources needed. These are factories, mines, and infrastructure.',
             'Factories produce money over time, providing a source of income to be able to fund more projects. Mines extract resources like coal, iron and stone. Infrastructure is a more unique type of building that will be explained in another page.',
             'Factories rely on coal to generate money. Without a sufficient supply of coal, factories will not be able to operate until there is enough coal again.',
             'In addition, random events may occur that affect different aspects of the game. These can be seen in the \'Event History\' tab. For the most part, these happen out of the player\'s control although some can be affected by the strength of the economy.']

    def __init__(self, parent, game_object):

        self.game_rules_container = ctk.CTkFrame(parent, corner_radius=10, width=300, height=500, fg_color='#292F3B')
        self.game_rules_container.grid_propagate(False)
        self.game_rules_container.grid_columnconfigure(0, weight=1)
        self.game_rules_container.grid_rowconfigure(0, weight=1)
        self.game_rules_container.grid(row=0, column=0, padx=7, pady=7)

        self.game_rules_centering_frame = ctk.CTkFrame(self.game_rules_container, fg_color='transparent')
        self.game_rules_centering_frame.grid(row=0, column=0)

        self.game_rules_title = ctk.CTkLabel(self.game_rules_centering_frame, text="LEADER'S GUIDE\nON RUNNING THE\nECONOMY\n", font=('Bahnschrift Light SemiCondensed', 25, 'bold'))
        self.game_rules_title.grid(row=0, column=0, pady=5, columnspan=2)

        self.game_rules_info = ctk.CTkLabel(self.game_rules_centering_frame, text=DashBoardTab.rules[0], font=('Consolas', 15), wraplength=200, height=225, width=200)
        self.game_rules_info.grid(row=1, column=0, pady=5, columnspan=2)

        self.left_button = ctk.CTkButton(self.game_rules_centering_frame, text='<', font=('Bahnschrift Light SemiCondensed', 25, 'bold'), command=self.leftButtonPressed, fg_color='#232633', hover_color='#3E455A', width=50)
        self.left_button.grid(row=2, column=0, padx=1, pady=7)

        self.right_button = ctk.CTkButton(self.game_rules_centering_frame, text='>', font=('Bahnschrift Light SemiCondensed', 25, 'bold'), command=self.rightButtonPressed, fg_color='#232633', hover_color='#3E455A', width=50)
        self.right_button.grid(row=2, column=1, padx=1, pady=7)

        self.event_history_widget = scrollable_widget.ScrollableWidget(parent, "EVENT HISTORY", event.getEventHistory(game_object), 0, 1)

    def refreshValues(self, game_object : g.GameData):
        self.event_history_widget.refresh(event.getEventHistory(game_object))

    def rightButtonPressed(self):
        current_index = DashBoardTab.rules.index(self.game_rules_info.cget("text"))
        last_index = len(DashBoardTab.rules)-1

        if current_index == last_index:
            self.game_rules_info.configure(text=DashBoardTab.rules[0])
        else:
            self.game_rules_info.configure(text=DashBoardTab.rules[current_index+1])

    def leftButtonPressed(self):
        current_index = DashBoardTab.rules.index(self.game_rules_info.cget("text"))
        first_index = 0
        last_index = len(DashBoardTab.rules)-1

        if current_index == first_index:
            self.game_rules_info.configure(text=DashBoardTab.rules[last_index])
        else:
            self.game_rules_info.configure(text=DashBoardTab.rules[current_index-1])

