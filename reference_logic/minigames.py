# minigames.py
import random
import time
from lore import ONE_PIECE_TRIVIA, PICKLE_DANCE_SEQS
from newtrivia import CREATION_TRIVIA, DESTRUCTION_TRIVIA, BINARY_TRIVIA

# 1) Three custom chest riddles per Kunju
CHEST_RIDDLES = {
    "Vikna Otsutsuki": [
        {
            "clue": "I dwell in the depths, created by divine, I shout 'kunju!', while glowing soft in the ocean’s dark. What am I?",
            "answers": ["kunjumani", "kunju", "kunjumon"]
        },
        {
            "clue": "Power in the eyes, caused by pain and love, catch fragments of the future, or casts an illusion. What is it?",
            "answers": ["sharingan", "mangekyou sharingan", "rinnegan"]
        },
        {
            "clue": "The kunjumon of the Marina Trench chants it, sama-ji says it's on the loose. What is it?",
            "answers": ["kunju", "kunju on the loose"]
        },
    ],
    "Joshua Joestar": [
        {
            "clue": "You say muda, I say ora, you said Star Platinum is the same stand as mine. What am I?",
            "answers": ["the world", "za warudo", "dio"]
        },
        {
            "clue": "Roses are red, violets are blue, if Rx7 goes brap, what goes stututututuuu?",
            "answers": ["gtr", "skyline", "skyline r34", "skyline gtr34", "supra"]
        },
        {
            "clue": "2+2 is 4, minus 1 that's 3 quick____?",
            "answers": ["math", "maths"]
        },
    ],
    "Melvin Satoru": [
        {
            "clue": "Yokoso, watashi no______",
            "answers": ["soul society"]
        },
        {
            "clue": "At the end of the first Transformers movie, what song plays as Optimus gives his iconic speech?",
            "answers": ["what i've done", "linkin park"]
        },
        {
            "clue": "A Soul Reaper's Zampakuto have 3 stages; Sealed, Shikai and______",
            "answers": ["bankai"]
        },
    ],
    "Arvindo Freecss": [
        {
            "clue": "There's the Speed Force, The Light Force, and then there's Arvindo's_________",
            "answers": ["kunju force", "kunju-force"]
        },
        {
            "clue": "The Bungee Gum have the property of both gum and______",
            "answers": ["rubber", "gomu gomu"]
        },
        {
            "clue": "Name something Arvindo Freecss would say",
            "answers": ["umbu", "kaddi", "kadi", "sappu", "owh god", "kunida", "sappi"]
        },
    ],
    "Rishi D. Owh Yeah": [
        {
            "clue": "When the universe were created, the kunjumon croaked_______",
            "answers": ["owh yeah", "oh yeah"]
        },
        {
            "clue": "Type UwU to get UwU-fied",
            "answers": ["uwu"]
        },
        {
            "clue": "Name one power system from the Big 3",
            "answers": ["haki", "reiatsu", "chakra", "bankai", "shikai"]
        },
    ],
    "Son Isaac": [
        {
            "clue": "Who lives in the pineapple under the sea?",
            "answers": ["spongebob squarepants", "spongebob"]
        },
        {
            "clue": "Who teaches Kamehameha to Goku?",
            "answers": ["roshi", "master roshi"]
        },
        {
            "clue": "What is Jiraiya's nickname?",
            "answers": ["pervy sage", "ero senin"]
        },
    ],
    "Mob Siva": [
        {
            "clue": "Who gained immense power after doing 100 push-ups, 100 sit-ups, 100 squats, and a 10km run?",
            "answers": ["saitama", "one punch man"]
        },
        {
            "clue": "Why did Monkey D. Luffy enter the Grand Line? To find_____",
            "answers": ["one piece"]
        },
        {
            "clue": "What engine does the GT-R34 have as default?",
            "answers": ["RB26DETT", "rb26", "rb26dett"]
        },
    ],
    "Sousuke Vertine": [
        {
            "clue": "What is the sacred act of Sama-Ji?",
            "answers": ["kaiye thunnai", "kaiye tunai", "kaiye thunai"]
        },
        {
            "clue": "What do we call when someone is acting like a sappi pundek?",
            "answers": ["kandara kawasaki", "pundek", "punda"]
        },
        {
            "clue": "Owh Yeah! Kunju on the_____",
            "answers": ["loose", "lose"]
        },
    ],
}

def get_chest_riddle(kunju):
    """
    Return a random (clue, answers) tuple for the given kunju.
    """
    riddles = CHEST_RIDDLES.get(kunju, [])
    if not riddles:
        return ("", [])
    choice = random.choice(riddles)
    return choice['clue'], choice['answers']


def dance_off():
    """
    Present a dance sequence for the player to mimic.
    Returns True if the player inputs the correct sequence.
    """
    seq = random.choice(PICKLE_DANCE_SEQS)
    print("An ancient rhythm pulses and goes 'Ayayayaya'… follow these moves:")
    print(" -> ".join(seq))
    for i, step in enumerate(seq, 1):
        guess = input(f"Move {i}: ").strip().lower()
        if guess != step:
            print("You falter, but some beat remains within you.")
            return False
    print("You move in perfect harmony. Owh Yeah!")
    return True


def one_piece_trivia():
    """
    Ask 4 random One Piece trivia questions. Return True if all are correct.
    """
    questions = random.sample(ONE_PIECE_TRIVIA, 4)
    correct = 0
    for q in questions:
        print(f"\n{q['q']}")
        for opt in q['options']:
            print(f" - {opt}")
        ans = input("Your answer: ").strip().lower()
        if ans == q['a'].lower():
            print("Correct!")
            correct += 1
        else:
            print(f"Incorrect. It was: {q['a']}")
    print(f"You got {correct}/4.")
    return correct == 4


def memory_match(pairs):
    """
    A simple memory match given a list of pairs with 'fragment' and 'book'.
    Returns True after completing all matches.
    """
    board = pairs[:]
    random.shuffle(board)
    matches = 0
    while matches < len(board)//2:
        for idx in range(len(board)):
            print(f"{idx+1}: [Hidden]")
        try:
            i1 = int(input("Flip card 1 #: ")) - 1
            i2 = int(input("Flip card 2 #: ")) - 1
        except ValueError:
            print("Use numbers.")
            continue
        if i1==i2 or i1<0 or i2<0 or i1>=len(board) or i2>=len(board):
            print("Invalid picks.")
            continue
        c1, c2 = board[i1], board[i2]
        print(f"  {c1['fragment']} ↔ {c1['book']}\n  {c2['fragment']} ↔ {c2['book']}")
        if c1['book']==c2['book']:
            print("Match! Owh Yeah!")
            for j in sorted((i1,i2), reverse=True):
                board.pop(j)
            matches+=1
        else:
            print("No match.")
    print("All paired! Path forwards opens.")
    return True


# --- New challenge functions from realms.py ---

def creation_quiz(kunju):
    print(f"\n-- You feel the Power of The Right Eye of Sama-Ji surge forth in you! {kunju} --")
    riddles = random.sample(CREATION_TRIVIA, 3)
    for r in riddles:
        print(f"\n{r['clue']}")
        ans = input("Answer: ").strip().lower()
        if ans not in [a.lower() for a in r['answers']]:
            print("Incorrect. Your creation falters into a disgusting, disfigured being. It purges itself from existence.")
            return False
        print("Correct!")
    print("Creation succeeds! You have created a universe and filled it with life! Owh Yeah!")
    return True

def destruction_quiz(kunju):
    print(f"\n-- Let's exorcise some cursed spirit and Hollow and save some souls! {kunju} --")
    riddles = random.sample(DESTRUCTION_TRIVIA, 3)
    for r in riddles:
        print(f"\n{r['clue']}")
        ans = input("Answer: ").strip().lower()
        if ans not in [a.lower() for a in r['answers']]:
            print("Incorrect. Countless innocent souls perished, tilting the balance of the world slightly.")
            return False
        print("Correct!")
    print("You maintained the balance of souls and the 69 Dimensions. Owh Yeah!")
    return True

def kunju_force_test():
    print("\n-- Kunju Force Attunement --")
    print("Press Enter rapidly 5 times to bend space-time and unleash your Kunju-Force!")
    for i in range(5):
        input(f"Press {i+1}: ")
    result = random.choice(["Your Kunju is small but barely meet the requirement of the force.", "That's a very mid Kunju, at least not smallest in the Kunju-Force.", "Owh Yeah! Kunju On the Loose!"])
    print(result)
    return True

def strength_test():
    print("\n-- Divine Strength Test --")
    print("Press Enter rapidly 5 times to demonstrate your might.")
    for i in range(5):
        input(f"Reps {i+1}: ")
    result = random.choice(["You feel your hairs falling, you're bald but you sense immense strength.", "Your strenght is barely mid. Mob Psycho 50%?", "MOB PSYCHO 100000000%! ORA ORA ORA ORA ORA!"])
    print(result)
    return True

def binary_trivia(kunju):
    print(f"\n-- Initiating Binary Trial for {kunju} --")
    questions = random.sample(BINARY_TRIVIA, 3)
    for q in questions:
        print(f"\n{q['clue']} (true/false)")
        ans = input("Answer: ").strip().lower()
        if ans != q['answers'].lower():
            print("Wrong.")
            return False
        print("Correct!")
    print("You’ve mastered the binary truths! Owh Yeah!")
    return True

