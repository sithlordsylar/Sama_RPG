import random
from temples import TempleFactory
from realms import RealmFactory
from combat import start_final_combat
from lore import KUNJUS

class Game:
    def __init__(self):
        self.temples = [TempleFactory.create(k) for k in KUNJUS]
        self.visited = []
        self.cards = []
        self.inventory = []

    def main_menu(self):
        while True:
            print("---------------------------------------------------------")
            print("Welcome to Sama-Ji TextRPG. Inspired by the legendary Zork")
            print("This game is developed in Python by the Left Hand of Sama-Ji \nTo choose the right Vessel for Sama-Ji's Return!")
            print("Owh Yeah!")
            print("---------------------------------------------------------")
            print("1) Start Game")
            print("2) How to Play")
            print("3) Exit")
            choice = input("Choose an option (1-3): ").strip()
            if choice == '1':
                self.start()
                break
            elif choice == '2':
                self.show_help()
            elif choice == '3':
                print("Goodbye!")
                exit()
            else:
                print("Invalid choice.")

    def show_help(self):
        print("\n--- How to Play ---")
        print("Use commands to interact with environments:")
        print(" - move <direction> (or 'go')")
        print(" - inspect <object> (or 'look', 'look around', 'read')")
        print(" - take <item> (or 'get')")
        print(" - use <item>")
        print(" - solve <puzzle> (or 'unlock', 'open')")
        print(" - inventory (or 'inv') to view inventory")
        print(" - enter to pass through opened doors or portals")
        print(" - help (or '?') to show this message anytime")
        print("\nPress Enter to return to menu...")
        input()

    def start(self):
        print("---------------------------------------------------------")
        print("You find yourself in a featureless white room.")
        print("A single door stands before you, and a small sign is affixed to it.")
        print("In the otherwise empty space, a tiny hole, about 5 cm across, floats in mid-air.")
        sign_read = False
        while True:
            cmd = input("\nWhat do you do? ").strip().lower()
            if cmd in ('read sign', 'inspect sign', 'look sign'):
                print("The sign reads: 'Life is like a blank canvas, you paint what you want to show.'")
                print("There's a subtitle in the sign that reads:\n'Here are some basic interaction mechanics of the game'")
                self.show_help()
                sign_read = True
            elif cmd in ('open door', 'enter door', 'open'):
                if not sign_read:
                    print("Is it safe? I better read the sign.")
                else:
                    print("You push the door open and step through...")
                    break
            elif cmd in ('inspect door', 'look door'):
                print("A divine aura radiates from within; your soul feels drawn toward it.")
            elif cmd in ('inspect hole', 'look hole'):
                print("There's something about this hole, it makes me feel funny and...")
                self.hole_interaction()
            elif cmd in ('look around', 'look', 'inspect room'):
                print("The white walls stretch endlessly; only the door, the sign, and the floating hole occupy the room.")
            elif cmd in ('help', '?'):
                self.show_help()
            else:
                print("Unknown command. (type 'help')")
        self.play_temple_sequence()

    def hole_interaction(self):
        while True:
            choice = input("\nOptions: look closer / give in to intrusive thoughts / leave\n> ").strip().lower()
            if choice == 'leave':
                print("You realize staring at the hole gives your boner, confused, you step back, refocusing on the door and sign.")
                return
            elif choice in ('look closer', 'look closer at hole'):
                print("You walk closer and realize you're getting harder… then all goes black.")
                print("You awaken back in the white room, dizzy but unharmed. Your boner gets harder")
                return
            elif choice in ('give in', 'give in to intrusive thoughts'):
                sub = input("\nOptions: lick it / do it\n> ").strip().lower()
                if sub == 'lick it':
                    print("You kneel… a stream of white liquid gushes… you fainted.")
                    return
                elif sub == 'do it':
                    print("You… insert the HDMI cable… you awaken back in the white room.")
                    return
                else:
                    print("Invalid choice.")
            else:
                print("Invalid option.")

    def play_temple_sequence(self):
        for temple in random.sample(self.temples, len(self.temples)):
            self.visited.append(temple.name)
            self.enter_area(temple, is_temple=True)
            if temple.card_collected:
                self.cards.append(temple.name)
                realm = RealmFactory.create(temple.name)
                self.enter_area(realm, is_temple=False)
            else:
                print(f"You leave the Temple of {temple.name} without its card.")
        self.ascend()
        self.final_challenge()

    def enter_area(self, area_obj, is_temple):
        # unified setup call
        area_obj.setup(self.inventory)
        print(f"\n--- Entering {'Temple' if is_temple else 'Realm'} of {area_obj.name} ---")
        print(area_obj.describe_current())

        while True:
            parts = input("> ").strip().lower().split()
            if not parts:
                continue
            verb, *args = parts
            moved = False

            if verb in ('move', 'go'):
                area_obj.move(args)
                moved = True

            elif verb in ('inspect', 'look'):
                if not args:
                    print(area_obj.describe_current())
                else:
                    area_obj.inspect(args, self.inventory)

            elif verb in ('take', 'get'):
                item = area_obj.take(args, self.inventory)
                if item:
                    print(f"You take the {item}.")

            elif verb == 'use':
                area_obj.use(args, self.inventory)

            elif verb in ('solve', 'unlock', 'open'):
                area_obj.solve_puzzle(args, self.inventory)

            elif verb in ('inventory', 'inv'):
                print("Inventory:", self.inventory or "(empty)")

            elif verb == 'enter':
                if area_obj.can_exit():
                    print(f"You pass through the threshold of {area_obj.name}.")
                    print(f"You depart the {'Temple' if is_temple else 'Realm'} of {area_obj.name}.")
                    break
                else:
                    print("You cannot enter yet.")

            elif verb in ('help', '?'):
                self.show_help()

            else:
                print("Unknown command. (type 'help')")

            if moved:
                print(area_obj.describe_current())

    def ascend(self):
        print("\nAs you collect the final Kunju card, a surge of power flows through you.")
        print("You have absorbed the essence of the Kunjus and become one with Sama-Ji.")

    def final_challenge(self):
        print("\n--- The Apex of Existence: Dimension 69 ---")
        print("The seal in Datorim has weakened—Ste'vi Ra and Veesus burst forth to challenge you!")
        start_final_combat(self.cards)

if __name__ == '__main__':
    Game().main_menu()
