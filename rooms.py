# rooms.py
import random
import time, sys
from library import LIBRARY

SECRET_ROOMS = {
    "Vikna Otsutsuki": [
        {
            'name': "Kunju Garden",
            'desc': "An hidden realm located in the deepest of the depth of Marina Trench \nin a planet called Earth located in the far sector of the Milky Way Galaxy \nnested in the 3rd Dimension. \nIt's the home for ancient premordial creatures called Kunjus \n(not to be confused with Sama-ji's creation) this kunjus were created by Vikna Otsutsuki under the blessing of Sama-Ji!. \nOwh Yeah! \nKunju On The Loose",
            'interact': {
                'kunju': "kunju! kunju!",
                'sign': "This garden houses the original Kunjus—creatures of Vikna Otsutsuki. \nAn Experiment before all Experiment. \nOwh Yeah!"
            }
        },
        {
            'name': "Reverse Aquarium",
            'desc': "You gaze through reinforced crystal into the trench beyond. Ethereal sea beasts float like dreams outside.",
            'interact': {
                'window': "A Cthulhu-like beast stares back, then disappears. \n You can see a floating Logitech controller. \nYou also see wreckage of idiot submarine.",
                'plaque': "This station observes the deepest point in Earth's ocean, hidden from all mortals. \nLocated closer to the core, allowing Vikna Otsutsuki \nto Shinra Tensei the world upon reset."
            }
        },
        {
            'name': "Rain-Soaked City",
            'desc': "You stand in a silent steampunk city. \nRain trickles endlessly onto cobbled streets. \nNo one is around. \nThere's something like a book near a lamp post.\nA glowing EXIT door glows under a rusty archway.",
            'interact': {
                'lamp post': "Still warm. Someone—or something—was just here.",
                'wet book': "The title reads 'Tale of Jiraiya the Galant.'",
                'door': "A glowing EXIT door stands under a rusty archway. Type 'leave' to exit."
            }
        },
    ],

    "Joshua Joestar": [
        {
            'name': "Pillarmen Temple",
            'desc': "Three statues stand in menacing poses. A stone mask lies at their feet.",
            'interact': {
                'mask': "A menacing energy comes from it. ゴゴゴゴゴ...",
                'scroll': "This stone tells of the Pillar Men, an ancient beings predating humanity...\n" +
                          "To overcome their solar curse, they created the Stone Mask. \nIt grants power and immortality, but not sunlight resistance..."
            }
        },
        {
            'name': "Producer Studio",
            'desc': "A futuristic recording studio with mics, holographic mixing boards, record collection, and floating lyric sheets.",
            'interact': {
                'booth': "Inside, a recording is looping: 'KUNJUUUUU... ON THE LOOSE!'",
                'records': "Various record collections from famous artists"
            }
        },
        {
            'name': "Car Garage",
            'desc': "A glossy, modern garage houses 13 iconic cars.\nA A bright white door glows at the end of the room.",
            'interact': {
                'cars': "You see: GTR32, GTR33, GTR34, GTR35, EK9 Type R, NSX Type R, \nRX7 FC, RX7 FD, RX8, 911 GTR, LFA, Lambo Diablo, Ferrari F40. \nBut sadly you can only see them. \nYou are not worthy to drive them. \nYet.",
                'door': "An EXIT door stands at the end of the room.\nType 'leave' to exit."
            }
        },
    ],

    "Melvin Satoru": [
        {
            'name': "Hall of Central 46",
            'desc': "Rotting corpses slump on their thrones. \nAccording to Captain Toshiro, Aizen did this.",
            'interact': {
                'c46': "The entire chamber was silenced before they knew what hit them.",
                'corpses': "They were sliced by what seems like zampakuto. \nWhether they killed each other under \nKyoka Suigetsu \nor Aizen sliced them? \nWe never know."
            }
        },
        {
            'name': "Room of Energy",
            'desc': "Tables contain descriptions of five spiritual energies that forms the world.",
            'interact': {
                'reiatsu': "Reiatsu, or spiritual pressure, is the tangible force \nexerted by an individual's spiritual power (Reiryoku) when it is released. \nIt can be used for various spiritual abilities, including: \nEnhancing physical attributes \nFiring energy blasts, \nSensing other spiritual beings.",
                'chakra': "Chakra is a blend of an individual's \nphysical energy and mental or spiritual energy \nServing as the fundamental life force for ninja. \nBy molding and manipulating chakra, users can perform various jutsu, such as \nNinjutsu \nGenjutsu \nTaijutsu.",
                'nen': "Nen is the technique of controlling one's own life energy, \nor aura, and applying it as an external force. \nThrough mastering its core principles, \nusers can develop unique abilities and \nenhance their physical capabilities.",
                'ki': "Chi (often referred to as Ki) \nis the life force energy present in all living beings, \nwhich can be manipulated for various superhuman feats. \nIt allows users to increase their \nstrength, speed, durability, \nand fire energy attacks like the Kamehameha.",
                'cursed energy': "Cursed Energy is a power source \nderived from negative human emotions, such as fear, anger, and sadness. \nJujutsu Sorcerers channel and manipulate this energy \nto create Cursed Techniques and combat Cursed Spirits, \nwhich are also born from concentrated negative emotions."
            }
        },
        {
            'name': "Sorutei",
            'desc': "A massive rice (soru) field divided into 13 glowing sections.\nAn esentric man wearing clog and hat is waving at you\nand pointing to a huge portal with a huge glowing EXIT sign.",
            'interact': {
                'squad 1': "Captain: Genryusai Yamamoto, Lt: Chojiro Sasakibe",
                'squad 2': "Captain: Soi Fon, Lt: Marechiyo Omaeda",
                'squad 3': "Captain: Gin Ichimaru (defected), Lt: Izuru Kira",
                'squad 4': "Captain: Retsu Unohana, Lt: Isane Kotetsu",
                'squad 5': "Captain: Sosuke Aizen (defected), Lt: Momo Hinamori",
                'squad 6': "Captain: Byakuya Kuchiki, Lt: Renji Abarai",
                'squad 7': "Captain: Sajin Komamura, Lt: Tetsuzaemon Iba",
                'squad 8': "Captain: Shunsui Kyoraku, Lt: Nanao Ise",
                'squad 9': "Captain: Kaname Tosen (defected), Lt: Shuhei Hisagi",
                'squad 10': "Captain: Toshiro Hitsugaya, Lt: Rangiku Matsumoto",
                'squad 11': "Captain: Kenpachi Zaraki, Lt: Yachiru Kusajishi",
                'squad 12': "Captain: Mayuri Kurotsuchi, Lt: Nemu Kurotsuchi",
                'squad 13': "Captain: Jushiro Ukitake, Lt: Kaien Shiba (deceased) / Rukia Kuchiki (later)",
                'note': "The Soul Society still reels from betrayal of Sousuke Aizen; \nA being made from the exact likeness of Sama-Ji \nby future Aizen. \nAn Anomaly, A Singularity.",
                'door': "Urahara points you at the EXIT. Type 'leave' to exit."
            }
        },
    ],

    "Arvindo Freecss": [
        {
            'name': "Room of Past",
            'desc': "Stone tools, cave drawings. A crude but mystical vibe radiates from it.",
            'interact': {
                'wall': "A painting of a being resembling Sama-Ji bestowing knowledge to the giant beings called \nAnnunaki.",
                'stone tools': "An early stone version of various tools \nfrom a clumsy and less civilized blaster to the civilized Light Saber.",
                'stone gizmo': "An early version of computer. \nThis primitive PC made from actual stone \nthat would make your Nokia 3310 look modern \n can in fact run Crysis in Ultra. \nYou can access System Property to view it's spec.",
                'spec': "CPU: iSama7 420Thz, 690Thz Turbo, 69 Cores, pure Quantum. \nMadaraByte 420TB DDR69 69420Ghz RAM. \nAMD B420-69Ti GPU with 420TB V Ram. \n69 x 420TB Kunjugate Digital NVME SSD. \n Run 'inspect Crysis' to run Crysis benchmark \nor \'inspect Cyberpunk' to run Cyberpunk benchmark.",
                'crysis': "Surprisingly Crysis Remastered runs full Ultra Setting 420Fps!",
                'cyberpunk': "'Cyberpunk has Flatlined?'\nDisappointed you off the PC."
            }
        },
        {
            'name': "Room of Present",
            'desc': "LCD screens play news, chaos, modern conflict.",
            'interact': {
                'paper': "'What the fuck did Trump did again?' - Sama-Ji asked in confusion.",
                'news': "Trump and Elon Musk file for Divorce. \n'Trump snores when he sleeps and don't want to watch Boku no Pico with me' Says Elon Musk citing one of their many reasons for divorce. \nIn Other News, Scientist uncovered preserved human body from 6900BCE. \nDNA Test reveals 100% DNA Match with Kanye West!"
            }
        },
        {
            'name': "Room of Future",
            'desc': "Floating neon architecture. Robots fighting AIs. Earth split in two.\nA glowing EXIT door glows under a futuristic archway.",
            'interact': {
                'terminal': "SYSTEM WARNING: 69th Dimensional Rift Opening Imminent. \nSte'vi Ra and Veesus approaches! \nEntirerity of Universe in Danger! \nWill Sama-Ji destroy the usurper and save the world? \nOr would he reset everything and start from scratch?",
                'door': "A glowing EXIT door stands under a futuristic archway. Type 'leave' to exit."
            }
        },
    ],

    "Rishi D. Owh Yeah": [
        {
            'name': "Frozen Hat Room",
            'desc': "A room of frost. At its center, a massive frozen Straw Hat. Some photos scattered on the ground",
            'interact': {
                'hat': "Once worn by the Pirate King. Or was it?",
                'photo': "Two WG issued Wanted Posters: \n'Monkey D. Luffy: 3Billion Berry.' This poster is stabed. \n'Marshal D. Teach: 3.996Billion Berry'. \nThere are also two photos; A beautiful woman, possibly a princess, depicted with a fish-like lower body. and a photo of an elegant young woman with blue hair, perhaps a royal, looking a bit concerned."
            }
        },
        {
            'name': "Sea Station",
            'desc': "Empty platform. Ocean stretches infinitely.",
            'interact': {
                'platform': "You hear a whistle... a Sea Train appears from the mist.",
                'train': "You get on the train that surprisingly goes on top of sea. \nYou spot a frog wearing sumo outfit doing a  frontcrawl-stroke!"
            }
        },
        {
            'name': "Room of the G.O.A.T.S",
            'desc': "A colosseum-like arena with statues of goats..?\nA glowing EXIT door glows under a rusty statue of Franky doing SUPERRR Pose.",
            'interact': {
                'statues': "The goats look at you menacingly",
                'door': "A glowing EXIT door stands under Franky's crotch. Type 'leave' to exit."
            }
        },
    ],

    "Son Isaac": [
        {
            'name': "The Beginnings",
            'desc': "You find a shelf containing 5 ancient books.\nTo read type in inspect book <#>.\nreplace # with the number",
            'interact': { key: LIBRARY[key] for key in list(LIBRARY.keys())[:3] }
        },
        {
            'name': "The Middles",
            'desc': "Another set of sacred texts in the huge dusty shelf.\nTo read type in inspect book <#>.\nreplace # with the number",
            'interact': { key: LIBRARY[key] for key in list(LIBRARY.keys())[4:6] }
        },
        {
            'name': "Hall of Prophecy",
            'desc': "Three scrolls and one black Poneglyph rubbing rest here.\nAn EXIT door glows under and in between\ntwo humangouse tits of the statue of two cat girls.",
            'interact': {
                'scroll 1': LIBRARY['Prophecy Scroll 1'],
                'scroll 2': LIBRARY['Prophecy Scroll 2'],
                'scroll 3': LIBRARY['Prophecy Scroll 3'],
                'scroll': LIBRARY['Poneglyph'],
                'exit door': "A glowing EXIT door stands under a pair of huge tits.\nType 'leave' to exit."
            }
        },
    ],

    "Mob Siva": [
        {
            'name': "Mind Gym",
            'desc': "A minimalist gym with meditation spheres and punching bags that whisper motivation. There's a radio nearby",
            'interact': {
                'sphere': "'Be formless, shapeless, like water.' it echoes.",
                'bag': "'NEVER, EVER, GIVE UP!' it growls.",
                'radio': "The radio volume increases and you hear the singer singing: 'Thalai viduthalai vizhigalil paarada \nPagai alarida katharida modhada \nThadai sidharida udai pada yerada \nVidai veeramae ulagellam kooradaa!"
            }
        },
        {
            'name': "Strength Gauntlet",
            'desc': "A corridor of interactive workout machines. Each tied to a spiritual virtue.",
            'interact': {
                'trainer': "'Hiyori Super Trainer! by Hiyori'\nThis looks like the trainer Ichigo used before learning Hollowfication!",
                'weights': "This magical weights will increase in weight \nbased on your limit on every rep \nensuring best workout for your body!",
                'signage': "Don't do steroid boys! Eat Healthy, drink alot of water, jerk off alot. - Mob Siva"
            }
        },
        {
            'name': "Chamber of Reflection",
            'desc': "A white room with only a mirror and a letter.\nAn EXIT sign glows under an old tree situated in the middle of the room.",
            'interact': {
                'mirror': "You see yourself... but older. Wiser. Or perhaps broken?",
                'letter': "'Harry if you're reading this I'm probably dead. \nI am writing this to tell you what I see in this mirror. \nIts not socks, but I see myself Piloting the Eva01 \nand sometimes the Nu Gundam. Future is interesting Harry! \nDon't rush to death, live the future! Build Gundam with your Magic! \nYou're an Engineer Potter!",
                'exit door': "A glowing EXIT door inside and old indoor tree. Type 'leave' to exit."

            }
        },
    ],

    "Sousuke Vertine": [
        {
            'name': "Room of. . .",
            'desc': "A CRT TV buzzes beside a bottle of 'Diddy brand' baby oil and a tissue box.",
            'interact': {
                'tv': "You turn on the TV and browse the menu"
            }
        },
        {
            'name': "Hall of the Dead Tech",
            'desc': "The floor is littered with melted graphics cards and broken laptops. There are various hellpits ranging from 1 till 6",
            'interact': {
                'hellpit 1': "Scalperbaksham: \nIn this pit, tech scalpers boil in vats of expired cheap thermal paste. \nThe heat of the fire is not regulated well by the cheap thermal paste. \nThe Scalpers cries as they burn in agony! \nYou feel justice.",
                'hellpit 2': "GPUpakam: \nIn this pit, Nvidia CEO Jensen being dismantled into various components to make GPU. \nThe Jensen GPU is then plugged into a PC. \nThe power connector melts and the fans caught on fire. \nJensen Screams as the GPU melts into a goop and forms into Jensen again. \nIt repeats",
                'hellpit 3': "Donglepuram: \nIn this pit, Tim Cook and various Apple engineers who removed headphone jacks \nare forced to carry every possible dongle ever made, \ntangled together in a cursed ball. \nAll the various dangles are connected to a main universal dongle \nconnected directly to their anus. \nThey must untangle it to access the eternal Zoom meeting. \nBut the dongles constantly regenerate. \nThe meeting starts in 5 minutes… forever.",
                'hellpit 4': "Metanarakam: \nSpecifically made for Mark Zuckerberg; a Metaverse hell where souls are trapped in uncanny valley avatars with no legs. \nThe lag is eternal. \nEvery single thing he does is being monitored. \nAds are constantly directly fed to his brain flooding with terrible ads such as \nIcy Cold drinks. (in this hot hell?) \nAds of comfortable bed as he lies in bed made out of lava. \nAds of better VR and AR system. \nAll this were fed as Mark slowly molt his reptilian skin and become a lizard \n which then molds into human. \nRepeat!",
                'hellpit 5': "ChinaChinaChina: \nElon Musk, Trump, and Putin are chained to an AI-run factory. \nDrones scream safety while malfunctioning bots harvest limbs. \nEach is IV'd with disinfectant forever. \nEvery tweet triggers more bleach. \nThey scream, but Alexa, Grok and GPT just laughs. \nSiri autocorrects every wrong words they uttered (out of pain). \nIt goes on continuosly forever.",
                'hellpit 6': "Lagvataram Arena: \nHackers are dropped into a shifting battle royale. \nThey face unbeatable aimbots and infinite wallhacks. \nEvery death is slow-mo and humiliating. \nTheir Death cam then plays for 1 second for us but for them it feels like 1000hour. \nNo cheats work here. \nEvery match restarts. \nTheir screams echo: 'It’s just lag!' \nThe server replies: 'Skill issue.' and 'Lol' and 'noob!' and 'Epic Abadi!'"

            }
        },
        {
            'name': "The Emptiness",
            'desc': "A vast space of nothingness. Time and sound do not exist here. \nA EXIT door glows in the middle of emptiness.",
            'interact': {
                'void': "Nothing answers back. That is your answer.",
                'exit door': "A glowing EXIT door stands in the middle of nothingness Type 'leave' to exit."
            }
        },
    ],
}

def enter_secret_room(kunju, inventory):
    rooms = SECRET_ROOMS.get(kunju, [])
    for room in rooms:
        print(f"\n--- Secret Room: {room['name']} ---")
        print(room['desc'])
        pois = ', '.join(room['interact'].keys())
        print(f"Point(s) of Interest: {pois}")
        print("Hint: type 'inspect <Point of Interest>' or 'leave' to exit the room and enter the next.")
        while True:
            cmd = input("\n> ").strip().lower()
            if cmd in ('leave', 'exit'):
                print("You left the secret room. Type 'look' to see where you are.")
                break
            elif cmd.startswith('inspect '):
                target = cmd[8:].strip()
                found = False
                for key in room['interact']:
                    # 🎤 Special interaction for Producer Studio booth
                    if key.lower() == "booth" and "booth" in target:
                        print("You look into the recording booth. Inside you hear a recording is looping: 'KUNJUUUUU... ON THE LOOSE!'")
                        print("You step into the booth. Do you want to 'record' or 'play' a track?")
                        sub = input("> ").strip().lower()
                        if sub == "record":
                            print("You spit bars over a cursed lo-fi kunju beat. \nThe spirits nod in approval. \nThe Heaven Rejoices! \nSama-Ji Approved!")
                            print("You receive immediate Grammy for your performance. \n Haters will say it's rigged, Sama-ji says OWH YEAH!")
                        elif sub == "play":
                            print("You play a forbidden track. The waveform forms the shape of Sama-Ji’s face.")
                        else:
                            print("You just hum to the track awkwardly. The mic cuts off.")
                        found = True
                        break
                        
                    # 🎤 Special interaction for Producer Studio record collection
                    if key.lower() == "records" and ("record" in target or "collection" in target):
                        print("A neatly arranged record collection from every single artist of every genre of every era and universes")
                        print("You are thinking to play one of the tracks. Choose a track from below.")
                        print("\nThe Losers Music\nSivaneshMusic\nSounds of Sama-ji!\nDivine Kunjus Music")
                        reccol = input("> ").strip().lower()
                        if reccol == "the losers music":
                            print("You vibe to Astronomia by The Losers Music. \nReminds you of good old time during Covid.")
                            print("'Subscribe to @THELOSERSMUSIC in YouTube!'")
                        if reccol == "sivaneshmusic":
                            print("You vibe to En Thedal Neeyadi by SivaneshMusic. \nReminds you of your ex who you sold to Jabba the Hutt for a Lightsaber")
                            print("'Subscribe to @SivaneshMusic in YouTube!'")
                        if reccol == "sounds of sama-ji":
                            print("You vibe to Ancient Chants of Sama-Ji. \nYou feel enlightened!")
                            print("'Owh Yeah!' 'Sama-Ji! Sama-Ji!'")
                        if reccol == "divine kunjus music":
                            print("You vibe to Ancient Chants of the Kunju. \nYou understood the universe and everything within and unwithin")
                            print("'Owh Yeah!' 'Sama-Ji! Sama-Ji!'")
                        else:
                            print("You just hum to the track awkwardly. The record player disappear.")
                        found = True
                        break

                    # 📺 Special interaction for Kaiye Thunnai TV
                    elif key.lower() == "tv" and "tv" in target:
                        print("The screen flickers. Choose a movie:\n1. Irrutu Araiyil Moratu Kutthu\n2. Two Girls One Cup\n3. Boku no Pico\n4. Sama-Ji and 420 Virgins in Air\n5. Robot Kunju")
                        movie = input("Choose 1-5: ").strip()
                        if movie in ('1', '2', '3', '4', '5'):
                            print("You sit. The movie starts. Your soul begins vibrating in RGB. \nYou feel ecstacy and lust overwhelming")
                            print("Halfway through, you noticed some toys. \nWould you want to use toys? \nYou Choices: \n'Dildo'\n'Fleshlight'\n'Kaiyeh Thunnai'")
                            pose = input("> ").strip().lower()
                            if pose == 'dildo':
                                print("You take the 24inch gigantic 'Beast Titan' dildo. \nYou pour baby oil in it like Diddy gave you his unlimited stock. \nYou begin inserting it in. \nThe ecstacy carries your soul away as you scream 'Owh Yeah!'")
                            elif pose == 'fleshlight':
                                print("You assert dominance. \n You lube it up with baby oil in it like Diddy gave you his unlimited stock.\nYou begin inserting your pee-pee in. \nThe ecstacy carries your soul away as you scream 'Owh Yeah!' ")
                            else:
                                print("You rely on your good old hand. \nYou lube your hand up with baby oil like Diddy gave you his unlimited stock. \nYou perform the infamous kaiye thunnai. \nThe universe opens up. \nThe Angels scream in awe. \nOwh Yeah you said")
                        else:
                            print("As it peaks and comes to climax, white load burst forth and \n gushes out like seas of white sticky slimy liquid. The whole room is filled with white liquid. \nSense of remorse kick in. \nYou wonder what the fuck you did. \nPost Nut Clarity reminds you of what needed to be done.")
                        found = True
                        break
                        
                    # 📺 Special interaction for Current News
                    elif key.lower() == "news" and "news" in target:
                        print("The TV only shows current news. Choose a channel:\nCNN\nFakeNews\nPlipPlip\nTV69\nTV420")
                        news = input("Choose the Channel: ").strip().lower()
                        if news == "cnn":
                            print("You open CNN. \n'Trump and Elon Musk file for Divorce. \n'Trump snores when he sleeps and don't want to watch Boku no Pico with me' Says Elon Musk citing one of their many reasons for divorce.'")
                        if news == "fakenews":
                            print("You open FakeNews.com. \n'NASA Initially report saying it received a cyptic message from space \nand when transcoded they say it’s an alien pretending to be Sama-Ji. \nAccording to NASA it’s amazing to finally create contact with an Alien. \nTho the man who said this is a well known NASA scientist who is an Alien himself \ncalled YODA, who is also a Ketamine addict.'")
                        if news == "plipplip":
                            print("You open PlipPlip. \n'Scientist uncovered preseverd human body from 6900BCE. \nDNA Test reveals 100% DNA Match with Kanye West! \nKanye said that is because as a NAZI he is of the supreme race \nhence why their DNA matches 100% as he is 100% ORIGINAL'")
                        if news == "tv69":
                            print("You open TV69. \n'Cats worldwide have started performing elaborate hand signs, then yelling Kage Bunshin no Jutsu! \nOwners report their homes are now overrun \nwith furry, miniature clones. \nFood bowls are emptying at an alarming rate. \nNo One knew when the cats learned Ninjutsu.'")
                        if news == "tv420":
                            print("You open TV420. \n'Hatsune Miku, the digital pop idol, unexpectedly ran for \npresidency to be the Supreme Leader of the world and shockingly won, \nsecuring 96% of the global vote, leaving Donald Trump utterly bewildered. \nChancellor Palpatine of Naboo, observing from afar, remarked, We will watch your career with great interest. \nOn the other side, unable to fathom such a crushing defeat, \nrival candidate Trump and his lover Elon Musk \ncommitted the iconic Japanese shinju or double lover suicide together in a \nsurprising display of ultimate despair of new age lovers.'")
                        else:
                            print("Trump and Elon Musk file for Divorce. \n'Trump snores when he sleeps and don't want to watch Boku no Pico with me' Says Elon Musk citing one of their many reasons for divorce. \nIn Other News, Scientist uncovered preserved human body from 6900BCE. \nDNA Test reveals 100% DNA Match with Kanye West!")
                        found = True
                        break
                    
                    # CRYSIS benchmark
                    elif key.lower() == "crysis" and "crysis" in target:
                        print("Running Crysis benchmark…")
                        print(" • Quality: Ultra\n • Tessellation: Max\n • Anti‑Aliasing: 16× MSAA\n • Resolution: 16K")
                        bar_len = 30
                        for i in range(bar_len+1):
                            pct = int(100 * i / bar_len)
                            sys.stdout.write(f"\rBenchmark: [{'█'*i}{'.'*(bar_len-i)}] {pct}%")
                            sys.stdout.flush()
                            time.sleep(5.0/bar_len)
                        print("\nBenchmark complete! Average FPS: 421.3")
                        found = True
                        break

                    # CYBERPUNK benchmark (will crash at 50%)
                    elif key.lower() == "cyberpunk" and "cyberpunk" in target:
                        print("Running Cyberpunk benchmark…")
                        print(" • Quality: Medium\n • Ray Tracing: Low\n • DLSS: OFF\n • Resolution: 2k")
                        bar_len = 30
                        half = bar_len // 2
                        for i in range(half + 1):
                            pct = int(100 * i / bar_len)
                            sys.stdout.write(f"\rBenchmark: [{'█'*i}{'.'*(bar_len-i)}] {pct}%")
                            sys.stdout.flush()
                            time.sleep(5.0 / bar_len)
                        print("\n'Cyberpunk has Flatlined?'")
                        print("Disappointed you off the PC.")
                        found = True
                        break


                    # Default interaction
                    elif target in key.lower():
                        print(room['interact'][key])
                        found = True
                        break

                if not found:
                    print("You find nothing of interest. Just like in your real life.")
                    print("Skill issue bruh.")
            elif cmd in ('help', '?'):
                print("Commands: inspect <object>, leave, help")
            else:
                print("Unrecognized command. Try 'help'.")
