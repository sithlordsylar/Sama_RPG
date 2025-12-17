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
        this.commandInput = document.getElementById('command-input');
        this.sceneImage = document.getElementById('scene-image');
        this.menuButtons = document.getElementById('menu-buttons');
        this.inventoryList = document.getElementById('inventory-list');

        this.commandInput.addEventListener('keydown', (event) => {
            if (event.key === 'Enter') {
                this.processCommand(this.commandInput.value);
                this.commandInput.value = '';
            }
        });
    }

    start() {
        this.render();
    }

    processCommand(command) {
        this.logToTerminal(`> ${command}`);
        const [verb, ...args] = command.toLowerCase().split(' ');

        if (this.gameState.currentLevel === 'whiteRoom') {
            this.handleWhiteRoomCommands(verb, args);
        }
    }

    handleWhiteRoomCommands(verb, args) {
        if (verb === 'read' && args.includes('sign')) {
            this.logToTerminal("The sign reads: 'Life is like a blank canvas, you paint what you want to show.'");
            this.logToTerminal("There's a subtitle in the sign that reads:\\n'Here are some basic interaction mechanics of the game'");
            this.showHelp();
            this.gameState.flags.signRead = true;
        } else if (verb === 'open' && args.includes('door')) {
            if (this.gameState.flags.signRead) {
                this.logToTerminal("You push the door open and step through...");
                this.startTempleSequence();
            } else {
                this.logToTerminal("Is it safe? I better read the sign.");
            }
        } else if (verb === 'inspect' && args.includes('hole')) {
            this.logToTerminal("There's something about this hole, it makes me feel funny and...");
            // For simplicity, the hole interaction is just a text description for now.
        } else if (verb === 'help') {
            this.showHelp();
        } else {
            this.logToTerminal("Unknown command. (type 'help')");
        }
    }

    startTempleSequence() {
        this.gameState.currentLevel = 'temple';
        // For now, we'll just go to a placeholder temple
        this.logToTerminal("You are now in a temple. (More to come)");
        this.render();
    }

    showHelp() {
        this.logToTerminal("\\n--- How to Play ---");
        this.logToTerminal("Use commands to interact with environments:");
        this.logToTerminal(" - move <direction> (or 'go')");
        this.logToTerminal(" - inspect <object> (or 'look', 'look around', 'read')");
        this.logToTerminal(" - take <item> (or 'get')");
        this.logToTerminal(" - use <item>");
        this.logToTerminal(" - solve <puzzle> (or 'unlock', 'open')");
        this.logToTerminal(" - inventory (or 'inv') to view inventory");
        this.logToTerminal(" - enter to pass through opened doors or portals");
        this.logToTerminal(" - help (or '?') to show this message anytime");
    }

    render() {
        this.clearTerminal();
        this.menuButtons.innerHTML = '';

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
        this.sceneImage.src = 'https://placehold.co/600x400/ffffff/000000?text=White+Room';
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

const game = new Game();
game.start();