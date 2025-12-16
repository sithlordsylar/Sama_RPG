// game.js - The Main Controller

// Helper function to create Divine Precursor styled buttons
function createStoneButton(text, onClick) {
    const btn = document.createElement('button');
    btn.className = "w-full h-12 rounded-full stone-btn flex items-center justify-between px-5 group relative overflow-hidden mb-2";
    
    // The button structure to match Stitch's design
    btn.innerHTML = `
        <span class="relative z-10 text-gray-300 font-bold uppercase text-sm tracking-wider group-hover:text-primary transition-colors text-left">${text}</span>
        <span class="material-symbols-outlined text-gray-500 group-hover:text-primary transition-colors z-10">arrow_forward</span>
        <div class="absolute inset-0 bg-white/5 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
    `;
    
    btn.onclick = onClick;
    return btn;
}

// Shared helper to update the UI
window.updateUI = {
    showText: (text) => {
        const dialogueContainer = document.getElementById('dialogue-text');
        dialogueContainer.innerHTML = `
            <div class="animate-pulse mb-2 text-cyan-400">> INCOMING_TRANSMISSION...</div>
            <div class="text-cyan-100/90 leading-relaxed text-lg">${text}</div>
        `;
        // Auto scroll to bottom
        dialogueContainer.scrollTop = dialogueContainer.scrollHeight;
    },
    showOptions: (options) => {
        const actionPanel = document.getElementById('action-panel');
        // Clear previous buttons but keep the container styles
        actionPanel.innerHTML = '<div class="bg-black/20 backdrop-blur-sm p-4 rounded-2xl border border-white/5 flex flex-col gap-3" id="inner-actions"></div>';
        
        const innerContainer = document.getElementById('inner-actions');
        
        options.forEach(opt => {
            const btn = createStoneButton(opt.text, opt.action);
            innerContainer.appendChild(btn);
        });
    }
};

async function main() {
    // Load the game data
    try {
        const response = await fetch('game_data.json');
        const gameData = await response.json();

        function startGame() {
            window.updateUI.showText("System Online. The Divine Precursor interface is active.<br><br>Select your protocol:");
            
            window.updateUI.showOptions([
                { text: "Protocol: Dance Off", action: () => danceOff(gameData, startGame, startGame) },
                { text: "Protocol: Trivia", action: () => trivia(gameData, startGame, startGame) },
                { text: "Protocol: Combat", action: () => new CombatEngine(gameData, startGame, startGame).startCombat() }
            ]);
        }

        // Start the game
        startGame();
    } catch (error) {
        console.error("Error loading game data:", error);
        document.getElementById('dialogue-text').innerHTML = "<span style='color:red'>CRITICAL ERROR: Could not load game_data.json. Make sure the file exists!</span>";
    }
}

// Wait for HTML to load before running
document.addEventListener('DOMContentLoaded', main);