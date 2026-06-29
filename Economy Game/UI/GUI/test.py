import tkinter as tk
import Systems.time_system as t, Systems.economy_system as e, Data.game_data as g

def mainGameLoop(game_object : g.GameData):
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
    pass