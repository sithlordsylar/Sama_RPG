// CombatEngine.js
class CombatEngine {
    constructor(gameData, onWin, onLose) {
        this.gameData = gameData;
        this.onWin = onWin;
        this.onLose = onLose;

        this.playerHP = 420;
        this.steviraHP = 420;
        this.veesusHP = 420;
    }

    startCombat() {
        this.updateDisplay("Combat Protocol Initiated. Enemy signatures detected.");
        this.playerTurn();
    }

    updateDisplay(message) {
        const statusHTML = `
            <p>${message}</p>
            <br>
            <div class="grid grid-cols-1 gap-2 text-sm font-mono border-t border-cyan-900/50 pt-2 mt-2">
                <span class="text-primary font-bold">SAMA-JI HP: ${this.playerHP}</span>
                <span class="text-red-400">STE'VI RA HP: ${this.steviraHP}</span>
                <span class="text-red-400">VEESUS HP: ${this.veesusHP}</span>
            </div>
        `;
        window.updateUI.showText(statusHTML);
        
        // Update the Holographic HUD HP bar width
        const hpPercent = Math.max(0, (this.playerHP / 420) * 100);
        const hpBar = document.querySelector('#hp-bar > div');
        if(hpBar) hpBar.style.width = `${hpPercent}%`;
    }

    playerTurn() {
        window.updateUI.showOptions(this.gameData.player_abilities.map(ability => {
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

        this.updateDisplay(`You unleashed <strong>${ability}</strong> on ${target} for <span class="text-primary text-xl">${damage}</span> damage!`);

        if (this.steviraHP === 0 && this.veesusHP === 0) {
            this.win();
        } else {
            setTimeout(() => this.enemyTurn(), 2000);
        }
    }

    enemyTurn() {
        let text = '';
        if (this.steviraHP > 0) {
            const ability = this.gameData.stevira_abilities[Math.floor(Math.random() * this.gameData.stevira_abilities.length)];
            const damage = Math.floor(Math.random() * (69 - 42 + 1)) + 42;
            this.playerHP = Math.max(0, this.playerHP - damage);
            text += `WARNING: Ste'vi Ra uses <strong>${ability}</strong>! Damage: ${damage}.<br>`;
        }
        if (this.veesusHP > 0) {
            const ability = this.gameData.veesus_abilities[Math.floor(Math.random() * this.gameData.veesus_abilities.length)];
            const damage = Math.floor(Math.random() * (69 - 42 + 1)) + 42;
            this.playerHP = Math.max(0, this.playerHP - damage);
            text += `WARNING: Veesus uses <strong>${ability}</strong>! Damage: ${damage}.`;
        }

        this.updateDisplay(text || "Enemies are hesitating...");

        if (this.playerHP === 0) {
            this.lose();
        } else {
            setTimeout(() => this.playerTurn(), 2000);
        }
    }

    win() {
        window.updateUI.showText("<span class='text-primary text-2xl'>VICTORY ACHIEVED.</span><br>All hostiles eliminated.");
        setTimeout(this.onWin, 3000);
    }

    lose() {
        window.updateUI.showText("<span class='text-red-500 text-2xl'>CRITICAL FAILURE.</span><br>System shutting down.");
        setTimeout(this.onLose, 3000);
    }
}