import { GAME_DATA } from './content.js';

class Game {
    constructor() {
        this.gameState = {
            currentLevel: 'mainMenu',
            inventory: [],
            flags: {},
            visitedTemples: [],
            cards: []
        };
        this.terminalOutput = document.getElementById('terminal-output');
        this.sceneImage = document.getElementById('scene-image');
        this.menuButtons = document.getElementById('menu-buttons');
        this.inventoryList = document.getElementById('inventory-list');
        this.dPadUp = document.getElementById('d-pad-up');
        this.dPadDown = document.getElementById('d-pad-down');
        this.dPadLeft = document.getElementById('d-pad-left');
        this.dPadRight = document.getElementById('d-pad-right');
        this.dPadEnter = document.getElementById('d-pad-enter');
        this.actionGrid = document.getElementById('action-grid');
    }

    start() {
        this.render();
    }

    updateImage(imageText) {
        this.sceneImage.src = `https://placehold.co/600x400?text=${imageText}`;
    }

    render() {
        this.actionGrid.innerHTML = '';
        this.menuButtons.innerHTML = '';

        if (this.gameState.currentLevel !== 'temple' && this.gameState.currentLevel !== 'realm' && this.gameState.currentLevel !== 'minigame') {
            this.clearTerminal();
        }

        if (this.gameState.currentLevel === 'mainMenu') {
            this.renderMainMenu();
        } else if (this.gameState.currentLevel === 'whiteRoom') {
            this.renderWhiteRoom();
        }

        this.updateInventory();
    }

    renderMainMenu() {
        this.logToTerminal("Welcome to Sama-Ji TextRPG. Inspired by the legendary Zork");
        this.logToTerminal("This game is developed in Python by the Left Hand of Sama-Ji \\nTo choose the right Vessel for Sama-Ji's Return!");
        this.logToTerminal("Owh Yeah!");
        this.updateImage("The_Sama-Ji_Scrolls");

        const startButton = document.createElement('button');
        startButton.textContent = 'Start Game';
        startButton.onclick = () => {
            this.gameState.currentLevel = 'whiteRoom';
            this.render();
        };
        this.menuButtons.appendChild(startButton);

        const helpButton = document.createElement('button');
        helpButton.textContent = 'How to Play';
        helpButton.onclick = () => {
            this.showHelp();
        };
        this.menuButtons.appendChild(helpButton);
    }

    renderWhiteRoom() {
        this.logToTerminal("You find yourself in a featureless white room.");
        this.logToTerminal("A single door stands before you, and a small sign is affixed to it.");
        this.logToTerminal("In the otherwise empty space, a tiny hole, about 5 cm across, floats in mid-air.");
        this.updateImage("White_Room");

        this.createActionButton("Read Sign", () => {
            this.logToTerminal("The sign reads: 'Life is like a blank canvas, you paint what you want to show.'");
            this.logToTerminal("There's a subtitle in the sign that reads:\\n'Here are some basic interaction mechanics of the game'");
            this.showHelp();
            this.gameState.flags.signRead = true;
        });

        this.createActionButton("Inspect Hole", () => {
            this.logToTerminal("There's something about this hole, it makes me feel funny and...");
            this.updateImage("CloseUp_Strange_Hole");
            this.renderHoleInteraction();
        });

        this.dPadEnter.onclick = () => {
            if (this.gameState.flags.signRead) {
                this.logToTerminal("You push the door open and step through...");
                this.startTempleSequence();
            } else {
                this.logToTerminal("Is it safe? I better read the sign.");
            }
        };
    }

    renderHoleInteraction() {
        this.actionGrid.innerHTML = '';
        this.createActionButton("Look Closer", () => {
            this.updateImage("hole1.gif");
            this.logToTerminal("You walk closer and realize you're getting harder… then all goes black.");
            this.logToTerminal("You awaken back in the white room, dizzy but unharmed. Your boner gets harder");
            setTimeout(() => this.renderWhiteRoom(), 2000);
        });
        this.createActionButton("Give in to Urge", () => {
            this.updateImage("hole2.gif");
            this.logToTerminal("You... insert the HDMI cable… you awaken back in the white room.");
            setTimeout(() => this.renderWhiteRoom(), 2000);
        });
        this.createActionButton("Leave", () => {
            this.logToTerminal("You realize staring at the hole gives your boner, confused, you step back, refocusing on the door and sign.");
            this.renderWhiteRoom();
        });
    }

    startTempleSequence() {
        this.gameState.currentLevel = 'temple';
        const kunju = GAME_DATA.kunjus[0]; // Start with the first Kunju for now
        this.activeTemple = new Temple(this, kunju);
        this.activeTemple.render();
    }

    createActionButton(text, onClick) {
        const button = document.createElement('button');
        button.textContent = text;
        button.className = 'action-btn';
        button.onclick = onClick;
        this.actionGrid.appendChild(button);
        return button;
    }

    showHelp() {
        this.logToTerminal("\\n--- How to Play ---");
        this.logToTerminal("Use the D-Pad to move and the action buttons to interact with the environment.");
    }

    updateInventory() {
        this.inventoryList.innerHTML = '';
        if (this.gameState.inventory.length === 0) {
            this.inventoryList.innerHTML = '<li>(empty)</li>';
        } else {
            this.gameState.inventory.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item;
                this.inventoryList.appendChild(li);
            });
        }
    }

    logToTerminal(message) {
        const p = document.createElement('p');
        p.innerHTML = message.replace(/\\n/g, '<br>');
        this.terminalOutput.appendChild(p);
        this.terminalOutput.scrollTop = this.terminalOutput.scrollHeight;
    }

    clearTerminal() {
        this.terminalOutput.innerHTML = '';
    }
}

class Temple {
    constructor(game, kunju) {
        this.game = game;
        this.kunju = kunju;
        this.room = 'entrance';
        this.riddle = GAME_DATA.riddles[this.kunju][0];
    }

    render() {
        this.game.clearTerminal();
        this.game.actionGrid.innerHTML = '';
        if (this.room === 'entrance') {
            this.renderEntrance();
        } else if (this.room === 'antechamber') {
            this.renderAntechamber();
        }
    }

    renderEntrance() {
        this.game.logToTerminal(`You stand before the Temple of ${this.kunju}. Moss covers ancient stone walls.`);
        this.game.updateImage(`${this.kunju}_Temple_Entrance`);
        this.game.dPadUp.onclick = () => {
            this.room = 'antechamber';
            this.render();
        };
        this.game.dPadDown.onclick = null;
        this.game.dPadLeft.onclick = null;
        this.game.dPadRight.onclick = null;
    }

    renderAntechamber() {
        this.game.logToTerminal("A dimly lit antechamber. A locked chest rests against the west wall.");
        this.game.updateImage(`${this.kunju}_Antechamber_Closed`);
        this.game.createActionButton("Inspect Chest", () => {
            this.startRiddle();
        });
        this.game.dPadDown.onclick = () => {
            this.room = 'entrance';
            this.render();
        };
    }

    startRiddle() {
        this.game.logToTerminal(`Clue: ${this.riddle.clue}`);
        this.game.updateImage("Lockpicking_GIF_Placeholder");
        this.game.actionGrid.innerHTML = '';
        const options = [...this.riddle.answers, "Wrong Answer 1", "Wrong Answer 2"];
        options.sort(() => Math.random() - 0.5);
        options.forEach(option => {
            this.game.createActionButton(option, () => {
                if (this.riddle.answers.includes(option.toLowerCase())) {
                    this.game.logToTerminal("Correct! The chest clicks open.");
                    this.game.updateImage(`${this.kunju}_Antechamber_Chest_OPEN`);
                    this.game.gameState.inventory.push("Temple Key");
                    this.game.updateInventory();
                } else {
                    this.game.logToTerminal("Wrong answer.");
                }
                setTimeout(() => this.render(), 2000);
            });
        });
    }
}

class ButtonMashingMinigame {
    constructor(game, onComplete) {
        this.game = game;
        this.onComplete = onComplete;
        this.clicks = 0;
        this.targetClicks = 15;
    }

    start() {
        this.game.gameState.currentLevel = 'minigame';
        this.game.logToTerminal("Mash the button to build power!");
        this.game.updateImage("Button_Mashing_Minigame");
        this.game.actionGrid.innerHTML = '<div class="progress-bar-container"><div id="progress-bar"></div></div>';
        const powerButton = this.game.createActionButton("POWER", () => this.handleClick());
    }

    handleClick() {
        this.clicks++;
        const progress = (this.clicks / this.targetClicks) * 100;
        document.getElementById('progress-bar').style.width = `${progress}%`;
        if (this.clicks >= this.targetClicks) {
            this.game.logToTerminal("You've built up enough power!");
            this.onComplete(true);
        }
    }
}

class MemoryMatchMinigame {
    constructor(game, onComplete) {
        this.game = game;
        this.onComplete = onComplete;
        this.sequence = [];
        this.playerSequence = [];
        this.level = 3;
    }

    start() {
        this.game.gameState.currentLevel = 'minigame';
        this.game.logToTerminal("Memorize the sequence!");
        this.game.updateImage("Memory_Match_Minigame");
        this.nextLevel();
    }

    nextLevel() {
        this.playerSequence = [];
        this.sequence.push(Math.floor(Math.random() * 4));
        this.playSequence();
    }

    playSequence() {
        let i = 0;
        const interval = setInterval(() => {
            this.highlightPanel(this.sequence[i]);
            i++;
            if (i >= this.sequence.length) {
                clearInterval(interval);
                this.awaitPlayerInput();
            }
        }, 600);
    }

    highlightPanel(index) {
        const panels = this.game.actionGrid.children;
        panels[index].classList.add('highlight');
        setTimeout(() => {
            panels[index].classList.remove('highlight');
        }, 300);
    }

    awaitPlayerInput() {
        this.game.actionGrid.innerHTML = '';
        for (let i = 0; i < 4; i++) {
            const panel = this.game.createActionButton(`${i + 1}`, () => this.handlePanelClick(i));
            panel.classList.add('memory-panel');
        }
    }

    handlePanelClick(index) {
        this.playerSequence.push(index);
        if (this.playerSequence[this.playerSequence.length - 1] !== this.sequence[this.playerSequence.length - 1]) {
            this.game.logToTerminal("Wrong sequence! You lose.");
            this.onComplete(false);
            return;
        }

        if (this.playerSequence.length === this.sequence.length) {
            if (this.sequence.length >= this.level) {
                this.game.logToTerminal("You win!");
                this.onComplete(true);
            } else {
                this.nextLevel();
            }
        }
    }
}


const game = new Game();
game.start();
// Example of how to start a minigame:
// setTimeout(() => {
//     const minigame = new ButtonMashingMinigame(game, (success) => {
//         game.gameState.currentLevel = 'whiteRoom';
//         game.render();
//     });
//     minigame.start();
// }, 3000);

// setTimeout(() => {
//     const minigame = new MemoryMatchMinigame(game, (success) => {
//         game.gameState.currentLevel = 'whiteRoom';
//         game.render();
//     });
//     minigame.start();
// }, 3000);