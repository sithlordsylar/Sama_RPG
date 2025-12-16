import random
from lore import REALMS, KUNJU_LORE, KUNJU_SANCTUMS, KUNJU_SANCTUM_ITEMS
from minigames import get_chest_riddle

class Temple:
    def __init__(self, kunju):
        self.name = kunju
        self.realm_name = REALMS[kunju]
        self.kunju_lore = KUNJU_LORE.get(kunju, "An ancient being shrouded in mystery.")
        self.card_collected = False
        self.lore_displayed = False

        # sanctum description & raw items
        self.sanctum_desc = KUNJU_SANCTUMS.get(kunju, "An aura of divine reverence fills the air.")
        raw_items = KUNJU_SANCTUM_ITEMS.get(kunju, {})

        # normalize sanctum_items to name->description dict
        if isinstance(raw_items, dict):
            self.sanctum_items = raw_items
        elif isinstance(raw_items, list):
            # if list of (name,desc) tuples, convert to dict
            if raw_items and isinstance(raw_items[0], tuple) and len(raw_items[0]) == 2:
                self.sanctum_items = dict(raw_items)
            else:
                # list of names -> placeholder desc
                self.sanctum_items = {name: "You see nothing special about it." for name in raw_items}
        else:
            self.sanctum_items = {}

        # get a random riddle for this chest
        clue, answers = get_chest_riddle(kunju)
        self.riddle_clue = clue
        self.riddle_answers = answers

        # build rooms
        self.rooms = {
            'entrance': {
                'desc': (
                    f"You stand before the Temple of {self.name}. Moss covers ancient stone walls. "
                    "There are ancient writings you can't decipher.\n"
                    "You hear chants: 'Owh Yeah! Owh Yeah!'\n"
                    "'Kunji on the loose! Kunji on the loose!'"
                ),
                'exits': {'north': 'antechamber'},
                'items': [],
                'puzzles': {}
            },
            'antechamber': {
                'desc': "A dimly lit antechamber.",
                'exits': {'south': 'entrance', 'north': 'sanctum'},
                'items': [],
                'puzzles': {
                    'chest': {
                        'type': 'chest',
                        'clue': self.riddle_clue,
                        'answers': self.riddle_answers,
                        'contains': 'temple key',
                        'solved': False
                    }
                }
            },
            'sanctum': {
                'desc': self.sanctum_desc,
                'exits': {'south': 'antechamber'},
                'items': list(self.sanctum_items.keys()),
                'puzzles': {
                    'sealed door': {
                        'type': 'door',
                        'requires': 'temple key',
                        'solved': False
                    }
                }
            }
        }

        self.current = 'entrance'


    def setup(self, inventory):
        if self.current == 'entrance' and not self.lore_displayed:
            print(f"\n[Lore of {self.name}]\n{self.kunju_lore}")
            self.lore_displayed = True


    def describe_current(self):
        room = self.rooms[self.current]
        desc = room['desc']

        # ante‑chamber chest detail
        if self.current == 'antechamber':
            c = room['puzzles']['chest']
            desc += "\n" + (
                "An open chest lies against the west wall."
                if c['solved']
                else "A locked chest rests against the west wall."
            )

        # sanctum door detail
        if self.current == 'sanctum':
            d = room['puzzles']['sealed door']
            desc += "\n" + (
                "The sealed door now stands open."
                if d['solved']
                else "A sealed door bars your path with glowing runes."
            )

        # build Point‑of‑Interest list
        poi = list(room['puzzles'].keys())
        if self.current == 'sanctum':
            poi.append('altar')
            poi.extend(self.sanctum_items.keys())

        exits = ', '.join(room['exits'].keys())
        status = f"Exits: {exits}."
        if poi:
            status += f" Point of Interest: {', '.join(poi)}."
        return f"{desc}\n{status}"


    def move(self, args):
        if not args:
            print("Move where? Try one of:", ', '.join(self.rooms[self.current]['exits'].keys()))
            return
        d = args[0]
        if d in self.rooms[self.current]['exits']:
            self.current = self.rooms[self.current]['exits'][d]
            print(f"You move {d} to the {self.current}.")
        else:
            print("You can't go that way. Available exits:", ', '.join(self.rooms[self.current]['exits'].keys()))


    def inspect(self, args, inventory):
        room = self.rooms[self.current]
        if not args:
            print(self.describe_current())
            return
        target = ' '.join(args)

        # chest
        if target == 'chest' and 'chest' in room['puzzles']:
            p = room['puzzles']['chest']
            if not p['solved']:
                print(f"A locked chest. Clue: {p['clue']}")
                self.solve_puzzle([], inventory)
            else:
                print("The chest is already open.")
            return

        # door
        if target in ('door','sealed door') and 'sealed door' in room['puzzles']:
            p = room['puzzles']['sealed door']
            if p['solved']:
                print("The door stands open. Type 'enter' to proceed.")
            else:
                print("A sturdy sealed door inscribed with glowing runes. It needs a key or incantation.")
                if p['requires'] in inventory:
                    self.use([p['requires']], inventory)
                else:
                    print(f"You are missing the {p['requires']}.")
            return

        # altar
        if target == 'altar' and self.current == 'sanctum':
            if not self.card_collected:
                print(f"The great altar enshrines {self.name}. A sacred statue stands depicting their true form.")
                print("Something shiny catches your eye...")
                print(f"On the altar, you find the Limited Edition Sama-Ji TCG card of {self.name} and take it.")
                self.card_collected = True
            else:
                print("You already took the treasure from the altar.")
            return

        # any other sanctum item (case‑insensitive)
        for name, desc in self.sanctum_items.items():
            if name.lower() == target and self.current == 'sanctum':
                print(desc)
                return

        print("You see nothing special about that.")


    def take(self, args, inventory):
        room = self.rooms[self.current]
        if not args:
            print("Take what? Try 'take <item>'.")
            return None
        item = ' '.join(args)
        if item in room['items']:
            inventory.append(item)
            room['items'].remove(item)
            return item
        print(f"There's no {item} here.")
        return None


    def use(self, args, inventory):
        if not args:
            print("Use what? Try 'use <item>'.")
            return
        item = ' '.join(args)
        room = self.rooms[self.current]
        for name,p in room['puzzles'].items():
            if p['type']=='door' and p['requires']==item and not p['solved']:
                p['solved'] = True
                print(f"You use {item} to unlock the sealed door. Owh Yeah! The path opens. Type 'enter' to proceed.")
                return
        print("You can't use that here.")


    def solve_puzzle(self, args, inventory):
        room = self.rooms[self.current]

        # chest first
        chest = room['puzzles'].get('chest')
        if chest and not chest['solved']:
            print(f"Clue: {chest['clue']}")
            guess = input("Enter the chest's answer: ").strip().lower()
            if guess in [a.lower() for a in chest['answers']]:
                chest['solved'] = True
                key = chest['contains']
                inventory.append(key)
                print(f"The chest clicks open and you immediately pocket the {key}. Owh Yeah!\n Type in 'go north' to proceed further into the Altar Room.")
            else:
                print("Wrong answer.\nConsult your consciouseness.\nYou know the answer.")
            return

        # then door
        door = room['puzzles'].get('sealed door')
        if door and not door['solved']:
            req = door['requires']
            if req not in inventory:
                print(f"The sealed door glows. You feel it needs a specific item... maybe a '{req}'?")
            else:
                door['solved'] = True
                print(f"You use the {req} to unlock the sealed door. Owh Yeah! The path opens. Type 'enter' to proceed.")
            return

        print("There's no puzzle to solve here.")


    def can_exit(self):
        if self.current == 'sanctum':
            door = self.rooms['sanctum']['puzzles']['sealed door']
            if not door['solved']:
                print("The door remains sealed. Perhaps there's a key or riddle.")
                return False
            if not self.card_collected:
                print("The great altar stands before you, glowing faintly. Try inspecting it.")
                return False
            return True
        return True


class TempleFactory:
    @staticmethod
    def create(kunju):
        return Temple(kunju)
