# The function that displays the main game console
def mainGameScreen():
    global coal, iron, stone, day
    print("────────────────────────────────────────────────────────────────────────────────")
    print("\t\t\t\t———Day " + str(day) + "———\n")
    print("\t\t\t  ———Total Resources———")
    print("\t🪨  (Coal): " + str(vm.getCoalQuantity()) + " \t🪨  (Iron): " + str(vm.getIronQuantity()) + " \t🪨  (Stone): " + str(vm.getStoneQuantity()))
    print("\t\t\t💰 (Economic Budget): " + str(vm.getCurrencyAmount()))
    print("\n\t\t-👉 (1)View Provinces-")
    print("\t\t-👉 (2)Construct-")
    print("\t\t-👉 (3)Laws/Management-")
    print("\t\t-👉 (4)Continue to Next Day-")
    print("────────────────────────────────────────────────────────────────────────────────")