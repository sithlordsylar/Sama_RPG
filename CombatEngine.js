class CombatEngine {
    constructor(gameData, onWin, onLose) {
        this.gameData = gameData;
        this.onWin = onWin;
        this.onLose = onLose;

        this.playerHP = 420;
        this.steviraHP = 420;
        this.veesusHP = 420;

        this.dialogueBox = document.getElementById('dialogue-box');
        this.optionsBox = document.getElementById('options-box');
    }

    startCombat() {
        this.showText(`
            <p>You stand as the Supreme Lord Swami Vikramnantha Sama-Ji.</p>
            <p>Your HP: ${this.playerHP}</p>
            <p>Ste'vi Ra HP: ${this.steviraHP}</p>
            <p>Veesus HP: ${this.veesusHP}</p>
        `);
        this.playerTurn();
    }

    playerTurn() {
        this.showOptions(this.gameData.player_abilities.map(ability => {
            return {
                text: ability,
                action: () => this.playerAttack(ability)
            };
        }));
    }

    playerAttack(ability) {
        const target = (this.steviraHP > 0 && this.veesusHP > 0) ? (Math.random() < 0.5 ? 'SteviRa' : 'Veesus') : (this.steviraHP > 0 ? 'SteviRa' : 'Veesus');
        const damage = Math.floor(Math.random() * (96 - 69 + 1)) + 69;

        if (target === 'SteviRa') {
            this.steviraHP = Math.max(0, this.steviraHP - damage);
        } else {
            this.veesusHP = Math.max(0, this.veesusHP - damage);
        }

        this.showText(`
            <p>You use ${ability} on ${target}, dealing ${damage} damage!</p>
            <p>Ste'vi Ra HP: ${this.steviraHP}</p>
            <p>Veesus HP: ${this.veesusHP}</p>
        `);

        if (this.steviraHP === 0 && this.veesusHP === 0) {
            this.win();
        } else {
            setTimeout(() => this.enemyTurn(), 1000);
        }
    }

    enemyTurn() {
        let text = '';
        if (this.steviraHP > 0) {
            const ability = this.gameData.stevira_abilities[Math.floor(Math.random() * this.gameData.stevira_abilities.length)];
            const damage = Math.floor(Math.random() * (69 - 42 + 1)) + 42;
            this.playerHP = Math.max(0, this.playerHP - damage);
            text += `<p>Ste'vi Ra uses ${ability}, dealing ${damage} damage to you!</p>`;
        }
        if (this.veesusHP > 0) {
            const ability = this.gameData.veesus_abilities[Math.floor(Math.random() * this.gameData.veesus_abilities.length)];
            const damage = Math.floor(Math.random() * (69 - 42 + 1)) + 42;
            this.playerHP = Math.max(0, this.playerHP - damage);
            text += `<p>Veesus uses ${ability}, dealing ${damage} damage to you!</p>`;
        }

        text += `<p>Your HP: ${this.playerHP}</p>`;

        this.showText(text);

        if (this.playerHP === 0) {
            this.lose();
        } else {
            setTimeout(() => this.playerTurn(), 1000);
        }
    }

    win() {
        this.showText("<p>All enemies defeated. You are victorious as Sama-Ji!</p>");
        setTimeout(this.onWin, 2000);
    }

    lose() {
        this.showText("<p>You have been defeated!</p>");
        setTimeout(this.onLose, 2000);
    }

    showText(text) {
        this.dialogueBox.innerHTML = text;
    }

    showOptions(options) {
        this.optionsBox.innerHTML = '';
        for (const option of options) {
            const button = document.createElement('button');
            button.innerText = option.text;
            button.onclick = option.action;
            this.optionsBox.appendChild(button);
        }
    }
}
