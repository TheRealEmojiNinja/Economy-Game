import customtkinter as ctk

class ConstructionTab:
    def __init__(self, parent, game_object):
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