
weapon = False
name = input()


def foyerScene():
    directions = ["North", "South", "East", "West"]
    print("You're in the hotel foyer."
          "The high ceilings reflect luxury and wealth."
          "Shame there's no one to marvel at it."
          "Strangely, everything still works.")
    print("There's a lot to do in here. What's first? North/South/East/West")
    command = input()


def liftLobby():
    directions = ["North", "South", "East", "West"]
    print("You're in the lift lobby. The lift's dead, though. Find a way to switch it on.")
    print("As you look around, you find a flickering switch. Do you activate it? Yes/No")
    command = input()

def kitchenScene():
    directions = ["North", "South", "East", "West"]
    item = ["a", "b"]
    print("You're in the kitchen. It seems that there's a fire in here."
          "Thick, black smoke shrouds your view. You need to act quickly."
          "What do you look for first?"
          "a) Fire extinguisher"
          "b) Fire blanket")
    command = input()

def vipLounge():
    monster = ["zombies"]
    item = ["Gold bar"]
    print("You enter the VIP lounge. It looks expensive."
          "Wait... Is that a gold bar?")
    print("What do you do now? (Take/Leave)")

def Level2():
    item = ["Golden key"]
    directions = ["North", "South", "East", "West"]
    print("I need to find my way to the rooftop.")






