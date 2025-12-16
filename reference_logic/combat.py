import random

# Define abilities with descriptive names and categories
PLAYER_ABILITIES = [
    "Chibaku Tensei (Creation)",
    "Shinra Tensei (Destruction)",
    "Getsuga Tensho (Offense)",
    "Rasengan (Offense)",
    "RGB Chroma Shield (Defense)",
    "Sutthule Choppa (Mind)",
    "Susanoo Guard (Defense)",
    "Hierro Skin (Defense)",
    "Kaiye Thunai (Heal)",
    "Owh Yeah! Kunju on the loose! (Debuff)",
    "Takos Better Watch Their Back! (Offense)",
    "Kunjuforce! (Crowd Control)",
    "Fuck the Popo! (Support)",
    "Kuchiyose No Jutsu! (Summon)",
    "Ethereal Dive (Offense)",
    "KANDARA KAWASAKI! (Ultimate)"
]
STEVIRA_ABILITIES = ["Rim Job", "Kunji Pechi"]
VEESUS_ABILITIES = [
    "Gigi Besar", "Gaydar Wave", "Suttadi Sunambu",
    "Torment Wave", "Abyssal Bite", "I AM VEESA!"
]

# Hit points for each combatant
PLAYER_MAX_HP = 420
STEVIRA_MAX_HP = 420
VEESUS_MAX_HP = 420


def start_final_combat(cards):
    # Display player state
    print("You stand as the; \nSupreme Lord Swami Vikramnantha Sama-Ji, \nThe Lord of all 69 dimension. \nThe One before everything, The one who is everything. \nA new vessel consisting of the eight Divine Kunjus:")
    for card in cards:
        print(f" - {card}")
    print(f"Your HP: {PLAYER_MAX_HP}\nSte'vi Ra HP: {STEVIRA_MAX_HP}, Veesus HP: {VEESUS_MAX_HP}")
    print("Prepare for the ultimate battle! \nBattle between the power of Friendship and the power of Dato Rim! \nJust kidding, this isn't Pokemon. \nTHIS \nIS \nMORTAL \nKOMBATTTTT!!!!!!!!")

    # Initialize HP
    player_hp = PLAYER_MAX_HP
    enemy_hp = {'SteviRa': STEVIRA_MAX_HP, 'Veesus': VEESUS_MAX_HP}
    turn = 1

    while True:
        print(f"\n-- Turn {turn} --")

        # Player's turn
        print("Your abilities:")
        for i, ab in enumerate(PLAYER_ABILITIES, 1):
            print(f" {i}. {ab}")
        choice = input("Choose ability number: ")
        if not choice.isdigit() or not (1 <= int(choice) <= len(PLAYER_ABILITIES)):
            print("696969ms! \nSama-ji experienced High latency, \nConnection delayed between vessel and Supreme Swamiji. \nYou lose your focus and skip the turn.")
        else:
            idx = int(choice) - 1
            ability = PLAYER_ABILITIES[idx]
            target = random.choice([name for name, hp in enemy_hp.items() if hp > 0])
            dmg = random.randint(69, 96)
            enemy_hp[target] = max(0, enemy_hp[target] - dmg)
            print(f"You use {ability} on {target}, dealing {dmg} damage!")

        # Show enemies' HP
        for name, hp in enemy_hp.items():
            print(f"{name} HP: {hp}")
        if all(hp == 0 for hp in enemy_hp.values()):
            print("All enemies defeated. \nOf course it was all according to your Keikaku! \nSama-Ji would never loose! \nAll Heil Sama-Ji! \nAll Heil the Fourth Reich! \nHeil Sama-Ji! \nKunju On The Loose!!! \nOwh Yeah Kandara Kawasaki!")
            return

        # Enemies' turn
        print("\nEnemies' turn:")
        for name, abilities in [('SteviRa', STEVIRA_ABILITIES), ('Veesus', VEESUS_ABILITIES)]:
            if enemy_hp[name] > 0:
                ab = random.choice(abilities)
                dmg = random.randint(42, 69)
                player_hp = max(0, player_hp - dmg)
                print(f"{name} uses {ab}, dealing {dmg} damage to you! \nThis but a scratch")

        # Show player HP
        print(f"Your HP: {player_hp}")
        if player_hp == 0:
            print("Owh No! I'm Dying! Call the Ambulance.")
            print("But not for me!")
            player_hp = PLAYER_MAX_HP
            print("Hehehe, it's all according to my Kunjumani Keikaku!")
            print(f"Your HP has been restored to {player_hp}.")

        # Check if combat should end
        if all(hp == 0 for hp in enemy_hp.values()):
            print("All enemies defeated. You are victorious as Sama-Ji! \nAll Heil Sama-Ji! \nAll Heil the Fourth Reich! \nHeil Sama-Ji! \nKunju On The Loose!!! \nOwh Yeah Kandara Kawasaki!")
            return

        turn += 1

    print("The battle has ended. \nAll Heil Sama-Ji! \nAll Heil the Fourth Reich! \nHeil Sama-Ji! \nKunju On The Loose!!! \nOwh Yeah Kandara Kawasaki!")
