# realms.py
import random
import minigames
from lore import REALMS, KUNJU_REALM_INTRO

class Realm:
    def __init__(self, kunju):
        self.kunju = kunju
        self.name = REALMS[kunju]
        self.intro_displayed = False
        self.secret_done = False  # NEW: Tracks if secret room has been completed
        self._inv = None  # will hold player inventory
        # rooms now hold only the core desc; intros & flavor go in code
        self.rooms = {
            'threshold': {
                'desc': None,
                'exits': {'forward': 'heart'},
                'puzzles': {}
            },
            'heart': {
                'desc': None,
                'exits': {'back': 'threshold', 'forward': 'portal_chamber'},
                'puzzles': {
                    'sigil': {
                        'type': 'minigame',
                        'name': 'challenge',
                        'solved': False
                    }
                }
            },
            'portal_chamber': {
                'desc': "A swirling portal hums with power. You feel the fragment's presence.",
                'exits': {'back': 'heart'},
                'puzzles': {}
            }
        }
        self.current = 'threshold'

    def setup(self, inventory):
        self._inv = inventory
        # map each realm to its unique challenge name
        mapping = {
            'Kunjimani Thottam':     'creation',
            'Aztec Forest':          'dance',
            'Soru Society':          'destruction',
            'Kunju Force':           'kunju_force',
            'Grando Linedo!':        'trivia',
            'Book World':            'memory',
            'Gymkhanna':             'strength_test',
            'Kaiyeh Thunnai Room':   'binary_trivia',
        }
        self.rooms['heart']['puzzles']['sigil']['name'] = mapping.get(self.name, 'generic')

    def describe_current(self):
        # threshold intro
        if self.current == 'threshold' and not self.intro_displayed:
            print(f"\n{KUNJU_REALM_INTRO[self.kunju]}")
            self.intro_displayed = True

        room = self.rooms[self.current]
        # build dynamic description
        if self.current == 'threshold':
            desc = f"You step into the {self.name}. Reality bends around you."
        elif self.current == 'heart':
            puzzle = room['puzzles']['sigil']
            if not puzzle['solved']:
                desc = f"You stand in the heart of {self.name}. A glowing sigil floats before you."
            else:
                desc = f"The heart of {self.name} lies calm. The spent sigil drifts quietly."
        else:  # portal_chamber
            desc = room['desc']

        # point-of-interest
        poi = []
        if self.current == 'heart':
            sig = room['puzzles']['sigil']
            poi.append('sigil' if not sig['solved'] else 'spent sigil')
        if self.current == 'portal_chamber':
            poi.append('portal')

        exits = ', '.join(room['exits'].keys())
        status = f"Exits: {exits}."
        if poi:
            status += f" Point of Interest: {', '.join(poi)}."
        status += "\nHint: use 'move <dir>', 'inspect <object>', 'solve', 'enter', 'inventory', 'help'."
        return f"{desc}\n{status}"

    def move(self, args):
        if not args:
            print("Move where? Exits:", ', '.join(self.rooms[self.current]['exits']))
            return
        d = args[0]
        if d in self.rooms[self.current]['exits']:
            self.current = self.rooms[self.current]['exits'][d]
            print(f"You move {d} to the {self.current}.")
        else:
            print("You can't go that way. Exits are:", ', '.join(self.rooms[self.current]['exits']))

    def inspect(self, args, inventory):
        room = self.rooms[self.current]
        if not args:
            print(self.describe_current())
            return
        target = ' '.join(args)

        # Heart sigil
        if self.current == 'heart' and target == 'sigil':
            puzzle = room['puzzles']['sigil']
            if not puzzle['solved']:
                print("An ethereal sigil floats before you, challenging your spirit.")
                self.solve_puzzle([], self._inv)
            else:
                print("The sigil’s glow has faded. You’ve already conquered this challenge.")
            return

        # Portal
        if self.current == 'portal_chamber' and target == 'portal':
            print("A swirling vortex of energy—step through to depart this realm.")
            return

        print("You see nothing special about that.")
        
    # NEW: Add the use method to the Realm class
    def use(self, args, inventory):
        """
        Handles the 'use' command within a Realm.
        Currently, it specifically handles using the 'portal' in the 'portal_chamber'.
        """
        if not args:
            print("Use what? Try 'use <object>'.")
            return

        target = ' '.join(args)

        # Handle 'use portal' command
        if self.current == 'portal_chamber' and target == 'portal':
            # The can_exit method already contains the logic for whether the portal can be used.
            # We just need to guide the user to the 'enter' command.
            if self.can_exit(): # This will print messages if conditions are not met
                print("The portal hums, ready for your departure. Type 'enter' to step through.")
            # If can_exit() returns False, it will already have printed a message, so no need to print more.
            return

        print("You can't use that here.")

    def solve_puzzle(self, args, inventory):
        room = self.rooms[self.current]
        puzzle = room['puzzles'].get('sigil')
        if not puzzle or puzzle['solved']:
            print("Nothing to solve here.")
            return

        name = puzzle['name']
        if name == 'dance':
            success = minigames.dance_off()
        elif name == 'trivia':
            success = minigames.one_piece_trivia()
        elif name == 'memory':
            pairs = [{'fragment': 'X', 'book': 'Y'}] * 4
            success = minigames.memory_match(pairs)
        elif name == 'creation':
            success = minigames.creation_quiz(self.kunju)
        elif name == 'destruction':
            success = minigames.destruction_quiz(self.kunju)
        elif name == 'kunju_force':
            success = minigames.kunju_force_test()
        elif name == 'strength_test':
            success = minigames.strength_test()
        elif name == 'binary_trivia':
            success = minigames.binary_trivia(self.kunju)
        else:
            input("Prove your worth (type anything): ")
            success = True

        if success:
            puzzle['solved'] = True
            inventory.append(f"{self.name} fragment")
            print(f"Challenge completed! You collect a fragment of {self.name}.")
            self.secret_room_flow(inventory)  # initiate secret_room hehe
        else:
            print("You failed, but gained insight.")

    def can_exit(self):
        if self.current == 'portal_chamber':
            heart = self.rooms['heart']['puzzles']['sigil']
            if not heart['solved']:
                print("The portal shudders. You must complete the challenge first.")
                return False
            if not getattr(self, 'secret_done', False):
                print("You sense a strange pull... there's more to discover before leaving this realm.")
                return False
        return True
        
    def secret_room_flow(self, inventory):
        from rooms import enter_secret_room  # ✅ entering secret room
        print("\n--- A hidden space cracks open in the emptiness... ---")
        print("You feel compelled to explore it before moving on.")
        enter_secret_room(self.kunju, inventory)
        self.secret_done = True




class RealmFactory:
    @staticmethod
    def create(kunju):
        return Realm(kunju)
