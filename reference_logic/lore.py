import random

# List of Kunjus
KUNJUS = [
    "Vikna Otsutsuki", "Joshua Joestar", "Melvin Satoru", "Arvindo Freecss",
    "Rishi D. Owh Yeah", "Son Isaac", "Mob Siva", "Sousuke Vertine"
]

# Mapping of Kunju to realm name
REALMS = {
    "Vikna Otsutsuki": "Kunjimani Thottam",
    "Joshua Joestar": "Aztec Forest",
    "Melvin Satoru": "Soru Society",
    "Arvindo Freecss": "Kunju Force",
    "Rishi D. Owh Yeah": "Grando Linedo!",
    "Son Isaac": "Book World",
    "Mob Siva": "Gymkhanna",
    "Sousuke Vertine": "Kaiyeh Thunnai Room"
}

# One Piece trivia bank (8 questions)
ONE_PIECE_TRIVIA = [
    {
        'q': "What is the name of the ship that was originally owned by Gol D. Roger?",
        'options': ["Thousand Sunny", "Oro Jackson", "Going Merry", "Moby Dick"],
        'a': "Oro Jackson"
    },
    {
        'q': "Who ate the Gomu Gomu no Mi fruit?",
        'options': ["Roronoa Zoro", "Monkey D. Luffy", "Portgas D. Ace", "Sanji"],
        'a': "Monkey D. Luffy"
    },
    {
        'q': "Which sea is the East Blue adjacent to?",
        'options': ["Calm Belt", "South Blue", "West Blue", "North Blue"],
        'a': "Calm Belt"
    },
    {
        'q': "Who is known as the ‘Pirate Hunter’?",
        'options': ["Sanji", "Franky", "Roronoa Zoro", "Usopp"],
        'a': "Roronoa Zoro"
    },
    {
        'q': "What bounty does Luffy have after the Dressrosa arc?",
        'options': ["500mil Berries", "1bil Berries", "300mil Berries", "700mil Berries"],
        'a': "500mil Berries"
    },
    {
        'q': "Which of these Devil Fruits is a Logia type?",
        'options': ["Gomu Gomu no Mi", "Hito Hito no Mi", "Ito Ito no Mi", "Mera Mera no Mi"],
        'a': "Mera Mera no Mi"
    },
    {
        'q': "Who is the captain of the Straw Hat Pirates?",
        'options': ["Usopp", "Tony Tony Chopper", "Monkey D. Luffy", "Nami"],
        'a': "Monkey D. Luffy"
    },
    {
        'q': "What is the name of the pirate crew led by Blackbeard?",
        'options': ["Blackbeard Pirates", "Red Hair Pirates", "Heart Pirates", "Kid Pirates"],
        'a': "Blackbeard Pirates"
    }
]

# Predefined dance sequences for the Ancient Dubstep Dance-Off
PICKLE_DANCE_SEQS = [
    ['left', 'up', 'right', 'down'],
    ['up', 'up', 'down', 'down'],
    ['left', 'right', 'left', 'right'],
    ['down', 'left', 'up', 'right']
]

# Descriptions of each Kunju for temple introductions
KUNJU_LORE = {
    "Vikna Otsutsuki": (
        "Created from the Right Eye of Sama-ji – Manipulator of the Past.\n"
        "His gaze holds the echoes of creation, and from his divine fragments, "
        "he formed Kunjumani Thottam, the sacred homeland of the Kunjumons.\n"
        "Hidden in the depths of the Mariana Trench, the mysterious Kunjumonz dwell—"
        "a species yet to be fully understood by mortal minds.\n"
        "He embodies the creation power of Sama-Ji; Chibaku Tensei."
    ),
    "Joshua Joestar": (
        "Formed from the Left Eye of Sama-Ji – Manipulator of the Future.\n"
        "He is the harbinger of destruction, the shadow that looms over all things destined to fall.\n"
        "It was his power that brought ruin to Hiroshima and Nagasaki, erased the islands of Lulusia and Ohara,\n"
        "and shaped the path of fate itself.\n"
        "He embodies the destruction power of Sama-Ji; Shinra Tensei."
    ),
    "Melvin Satoru": (
        "The Left Hand of Sama-Ji – The source of all Evil Energy.\n"
        "From him flows the cursed power of Yin Chakra, Cursed Energy, and Death itself.\n"
        "Under the order of Sama-Ji, Melvin Satoru and Vikna Otsutsuki once brought forth\n"
        "the creation of the infamous 3rd Dimension being called Rudolph Hitla, later undone by\n"
        "Joshua Joestar and Arvindo Freecss.\n"
        "He embodies the negative power of Sama-Ji; The Umbi-Force."
    ),
    "Arvindo Freecss": (
        "The Right Hand gain consciousness – The source of all Good Energy.\n"
        "He is the wellspring of Yang Chakra, Ki/Nen, and Life.\n"
        "When Melvin Satoru and Vikna Otsutsuki brought forth the chaotic avatar of Sama-Ji, Rudolph Hitla—\n"
        "Arvindo Freecss and Joshua Joestar transformed him to do good under the red flag of USSR\n"
        "and turned him into a red-nosed reindeer.\n"
        "He embodies the positive power of Sama-Ji; The Kunji-Force."
    ),
    "Rishi D. Owh Yeah": (
        "The all-loving heart of Sama-Ji – Neither purely good nor evil.\n"
        "He maintains the balance of Reiatsu, Sage Chakra, and RGB Chroma Power.\n"
        "He is the manipulator of the Present; his will shapes the now.\n"
        "He embodies the balancing power of Sama-Ji and reigns over the croaking Kunjumon;\n"
        "thus given the embodiment of the phrase: The Owh Yeah."
    ),
    "Son Isaac": (
        "The Ever-Expanding Brain of Sama-Ji – The font of Wisdom, Knowledge, Consciousness, and Free Will.\n"
        "He shapes the thoughts and desires of all beings and grants blessings of intellect\n"
        "to super-intelligent minds across all universes—from Albert Einstein to Mayuri Kurotsuchi.\n"
        "He embodies the facts, strategy, truths, and knowledge of Sama-Ji; The Delta-Force."
    ),
    "Mob Siva": (
        "The Body of Sama-Ji – The source of Strength and Defense.\n"
        "His power manifests in the legendary shields of Susanoo, the Hierro of Hollows,\n"
        "and the Armament Haki of Grand Line warriors, as well as Saitama’s one-punch might.\n"
        "He embodies the durability and strength of Sama-Ji; The Steroid."
    ),
    "Sousuke Vertine": (
        "The True Essence – The Source of All Creation.\n"
        "Every drop of liquid he releases births galaxies, universes, and new life.\n"
        "When Sama-Ji performs Kaiye Thunai, the Ritual of Creation, worlds flourish in his image.\n"
        "He embodies the creative power of Sama-Ji; Kaiye Thunai."
    )
}

# 2) Custom sanctum descriptions (when you step into the altar room)
KUNJU_SANCTUMS = {
    "Vikna Otsutsuki": (
        "You arrive at the magnificent courtyard of Kunjimani Thottam, bioluminescent corals\n"
        "drift through ancient pillars. At its center, a altar stands with aura pulses heavily..."
    ),
    "Joshua Joestar": (
        "The ground here is paved with shattered obsidian. Statues of fallen empires\n"
        "surround the altar—each carved in the shape of a forgotten warlord..."
    ),
    "Melvin Satoru": (
        "A choking haze of crimson energy fills the hall. Bones and rusted chains\n"
        "twist around the dais where the altar stands, oozing dark cloudy energy..."
    ),
    "Arvindo Freecss": (
        "Sunlight streams through fractured glass, casting rainbows on golden vines.\n"
        "Birdsong echoes off gilded walls as the altar of Life pulses with warmth..."
    ),
    "Rishi D. Owh Yeah": (
        "Crystal chalices float mid-air, suspended by unseen forces. Soft croaking\n"
        "chants drift in the mist, centering on the rose-gold altar of Balance..."
    ),
    "Son Isaac": (
        "Towering shelves of floating tomes swirl in infinite orbits. A lectern holds\n"
        "an ever-changing map of the multiverse beside the central Knowledge Altar..."
    ),
    "Mob Siva": (
        "Granite pillars engraved with battle scars ring the arena hall.\n"
        "Weights of impossible size hover, while the stone altar radiates raw might..."
    ),
    "Sousuke Vertine": (
        "Liquid silver drips from spiraling columns. Biolabs hum with creation energy\n"
        "around the Genesis Altar, where every drop births new life forms..."
    ),
}

# 3) Three “flavor” items per sanctum (name → description)
KUNJU_SANCTUM_ITEMS = {
    "Vikna Otsutsuki": [
        ("Bacta Tank of Eyes", "A tank filled with bioluminescent liquid. \nInside the tank are millions of eyes of various paterns. \nThe plaque reads: \n'The Tank of Eyes'\nThe tank consists of various blessed eyes\nbelonging to various races from\nThe Otsutsukis to the Uchihas."),
        ("Blueprint of Life", "A blueprint filled with unknowns scripts.\nIt seems very technical and advanced."),
        ("Proto-Kunju", "The plaque reads: \n'The first Kunjumonz of the Kunjimani Thottam.\nA Prototype of what becomes the greatest invention of\nThe Almighty Vikna Otsusuki-Sama.'\n'Note: The Kunjumonz are advanced premodial beings\ncapable of living in any environment including\nthe vast empty space of nothingness.\nVikna Otsutsuki was ordered by the\nSupreme Swamiji Lord Vikramnantha Sama-Ji\nto create a being that will exist aslong as existence exist alongside with Sama-Ji.\nOwh Yeah! Kunju on The Loose!'")
    ],
    "Joshua Joestar": [
        ("Documents of Project Manhattan", "This-It can't be! It's the Project Manhattan!"),
        ("Motherframe", "A huge tank filled with luminescent liquid.\nIn the middle is a fire? A Fire in liquid?.\nThe Plaque Reads:\nMotherframe: A source of unlimited clean power.\nUsed to power various weapons of history.\nStatus: Sealed\nCreator & Sealed by: Joshua Joestar\nConfirmed Usage:\n1.The Destruction of Lulusia by Saint Nerona Imu.\n2.The Destruction of Planet Pluto before Sama-Ji resurected it.\n3.Almost used in the Manhattan Project as a way to destroy earth for recreation.\n4.Destruction of multiple planets by Lord Beerus."),
        ("Book of Apocalypse", "Inscribed with prophecies of apocalypse from various universe, planets, species and religion.")
    ],
    "Melvin Satoru": [
        ("Cursed Chain", "Forged in hatred, it tightens when you draw blood."),
        ("The Schyte of Death", "The Schyte reek of death and blood.\nThe Plaque Reads:\nThe Schyte of Death is the centralized power system of death itself.\nThis Schyte was the first to be created that have the power to undo life.\nBestowed with energy of Melvin Satoru, this Schyte serves as the server\nwhere all the Schytes and Zampakuto of Death Gods gain their power."),
        ("Glass of Souls - A", "The eternal movements of souls are monitored here as they come from Sama-ji and returns to Sama-ji in all eternity")
    ],
    "Arvindo Freecss": [
        ("The Chalice of Life", "A glowing chalice containing the essence of every creation"),
        ("Terrarium of Life", "A Massive Terrarium with uncountable amount of tiny colonies.\nThe Plaque Reads:\nThe Terrarium of Life.\nThis Terrarium houses all the planets and creatures of the multiverse.\nIt is an overview of every creation.\nAs Melvin Satoru claims life, Arvindo Freecs gives them.\nHe monitors and blesses all creation under the guidance of Sama-Ji\nTotal Dimensions:68 + 1 Core\nTotal Universes: 6942069 - 69\nTotal life existing now: 2.76×10^54 life forms\nTotal life existed since creation: 2.76×10^54 life forms"),
        ("Glass of Souls - B", "The eternal movements of souls are monitored here as they come from Sama-ji and returns to Sama-ji in all eternity")
    ],
    "Rishi D. Owh Yeah": [
        ("The Horn of Owh Yeah", "A unique horn looks like it was made out of pure diamond with gold imbued into it.\nThe Plaque Reads:\nThe Horn of Owh Yeah!\nThe Horn have powers to bring forth the attention of all living creations\nso they may hear the message of\nSupreme Swamiji Lord Vikramnantha Sama-Ji.\nThe horn will also be used to call upon all the Kunjus for meeting\nat the neutral dimension of Drifto Corner"),
        ("RGB CHROMA HUB", "A unique machine with various lights coming from it. The plaque is unreadable."),
        ("The UwU of UwUs", "I have no fucking clue what the fuck this should be.")
    ],
    "Son Isaac": [
        ("Infinite Quill", "A unique quill hovers above a vast meteorite stone table. There are no papers nor ink well.\nThe Plaque Reads:\nThe Infinite Quill\nThe quill draws maps of worlds yet unimagined.\nAllowing Son Isaac to be the architect of all creations and map out the universe no as it is, but as it should be.\nThe quill disperse it's own ink and as the ink touches and creates a land\na new world will be born.\nAll in the Name of The Great Sama-ji and his 8Kunjus."),
        ("The Quantum Box", "A floating black box. Something feels off about it, it's there but also it's not."),
        ("The Scroll of Infinite Wisdom", "This scroll calls out for me. But what is-\nYou fainted.")
    ],
    "Mob Siva": [
        ("Infinity Gauntlet", "This looks like Thanos' toy.\nThe Plaque Reads:\nThe Celestial Gauntlet of Kandara Kawasaki\nThis Gauntlet unlike it's cheap knock off OEM clone; The Infinity Gauntlet\nneeds no stones as it is readily imbued with\nThe Essence of Sama-ji. The Gauntlet wearer is capable of calling forth the power of the Fighter God Mob Siva.\nThe Gauntlet is not meant to be worn in traditional way.\nBut instead it is imbued upon being when Mob Siva wanted to.\nWielders of the Gauntlet in their soul:\nSaitama\nClark Kent\nDovahkiin\nDoom Slayer\nChuck Norris\nCaptain Vijaykanth\nAK\nSura\nNokia 3310"),
        ("The Guardian Console", "A console with various buttons, switches, screens and etc.\nThe Plaque Reads:\nThe Guardian Console.\nThe Guardian Console is the command console of the Guardian Squad.\nThe Guardian Squad consist of elite Kunjumon created by sama-ji.\nThey Serve as Guardians for all of Sama-ji creations\nEnsuring they are kept safe, blessed and even punished if needed.\nMany Religion calls them as Guardian Angels / Ancestor Spirits / Guardian Deity and more."),
        ("Drums of Liberation", "No one is playing the drum but I could feel the sound coming from it. I feel so liberated, so happy, so free! It's the sound of Joy Boy!")
    ],
    "Sousuke Vertine": [
        ("The Chalice of Aeons", "A huge unique chalice float in the space. It's filled with thick silver liquid to brim.\nThe Plaque Reads: \nThe Challice of Aeon\nThe True Challice of Aeon where the inferior smaller Challice of Aeon \ngiven to the Annunaki; Ninhursag so that Earth can be filled with life.\nThis chalice holds the power of creation and destruction.\nIt contains Chr-Oma Cu’m, the essence of creation itself,\na product of the Kaiyeh Thunnai ritual"),
        ("Cosmic Urn of Pandaman", "A weird box with menacing energy. \nThe Warning Reads:\nIts lid ripples time whenever it is opened. Only for Kunjus Usages!"),
    ],
}

# 4) Unique realm intros (when you first enter each realm)
KUNJU_REALM_INTRO = {
    "Vikna Otsutsuki": "The abyss stretches before you; every ripple in the water is a brushstroke of history.",
    "Joshua Joestar": "Ruins stand in eternal twilight—ghosts of futures long since erased whisper in the wind.",
    "Melvin Satoru": "Dark clouds gather overhead; lightning of malice cracks the sky as you step forward.",
    "Arvindo Freecss": "Fields of golden light bloom under your feet, singing of life’s endless cycle.",
    "Rishi D. Owh Yeah": "A chorus of croaks and footsteps greets you—harmony in motion at every turn.",
    "Son Isaac": "Endless libraries stretch into infinity; every book hums with the knowledge of the cosmos.",
    "Mob Siva": "Colossal statues of strength line the path; your heartbeat echoes like war drums.",
    "Sousuke Vertine": "A shower of stardust rains down; creation itself seems to pulse around you."
}