// game.js - The Sama-Ji Adventure Engine

// ==========================================
// 1. THE ENGINE STATE (Memory)
// ==========================================
const gameState = {
    location: "white_room", // white_room, temple, realm, dim69
    subLocation: "main",    // entrance, antechamber, sanctum, heart, secret1, etc.
    inventory: [],
    visitedKunjus: [],
    currentKunju: null,     // The object of the current god being visited
    templeData: null,       // Temporary data for the current temple instance
    gameData: null          // The full JSON loaded from file
};

// ==========================================
// 2. UI HANDLERS (The Visuals)
// ==========================================
const ui = {
    text: (msg) => {
        const consoleEl = document.getElementById('dialogue-text');
        // Create a new paragraph for the history log
        const newLog = document.createElement('div');
        newLog.className = "mb-4 border-b border-cyan-900/30 pb-2 fade-in";
        newLog.innerHTML = `<span class="text-cyan-400 font-bold">> SYSTEM:</span> <span class="text-gray-300">${msg}</span>`;
        consoleEl.appendChild(newLog);
        consoleEl.scrollTop = consoleEl.scrollHeight;
    },
    clearOptions: () => {
        document.getElementById('inner-actions').innerHTML = '';
    },
    addOption: (label, onClick, icon="arrow_forward") => {
        const btn = document.createElement('button');
        btn.className = "w-full h-12 rounded-full stone-btn flex items-center justify-between px-5 group relative overflow-hidden mb-2";
        btn.innerHTML = `
            <span class="relative z-10 text-gray-300 font-bold uppercase text-sm tracking-wider group-hover:text-primary transition-colors text-left">${label}</span>
            <span class="material-symbols-outlined text-gray-500 group-hover:text-primary transition-colors z-10">${icon}</span>
            <div class="absolute inset-0 bg-white/5 translate-y-full group-hover:translate-y-0 transition-transform duration-300"></div>
        `;
        btn.onclick = onClick;
        document.getElementById('inner-actions').appendChild(btn);
    },
    setDPad: (north, south, east, west) => {
        // Maps D-Pad buttons to functions. Pass null to disable.
        document.getElementById('btn-north').onclick = north ? north : null;
        document.getElementById('btn-south').onclick = south ? south : null;
        document.getElementById('btn-east').onclick = east ? east : null;
        document.getElementById('btn-west').onclick = west ? west : null;
        
        // Visual opacity for disabled buttons
        document.getElementById('btn-north').style.opacity = north ? 1 : 0.3;
        document.getElementById('btn-south').style.opacity = south ? 1 : 0.3;
        document.getElementById('btn-east').style.opacity = east ? 1 : 0.3;
        document.getElementById('btn-west').style.opacity = west ? 1 : 0.3;
    }
};

// ==========================================
// 3. CORE LOGIC (The Brain)
// ==========================================

async function initGame() {
    try {
        const response = await fetch('game_data.json');
        gameState.gameData = await response.json();
        
        // Start the loop
        renderWhiteRoom();
    } catch (e) {
        ui.text("<span class='text-red-500'>CRITICAL FAILURE: Could not load game_data.json</span>");
        console.error(e);
    }
}

// --- SCENE 1: THE WHITE ROOM ---
function renderWhiteRoom() {
    gameState.location = "white_room";
    
    ui.text("You find yourself in a featureless white room.<br>A single door stands before you, and a small sign is affixed to it.<br>In the otherwise empty space, a tiny hole floats in mid-air.");
    
    updateWhiteRoomActions();
}

function updateWhiteRoomActions() {
    ui.clearOptions();
    ui.setDPad(null, null, null, null); // No movement yet

    ui.addOption("Read Sign", () => {
        ui.text("THE SIGN READS: 'Life is like a blank canvas...'<br><br>HOW TO PLAY:<br>- Use the D-Pad to Move<br>- Use Actions to Inspect/Interact<br>- Collect Kunju Cards to ascend.");
    }, "menu_book");

    ui.addOption("Inspect Hole", () => {
        ui.text("It is a tiny hole, about 5cm across. Infinite darkness lies within.");
    }, "visibility");

    ui.addOption("Open Door", () => {
        ui.text("You push the door open and step through...");
        setTimeout(startNextTemple, 1500);
    }, "door_open");
}

// --- SCENE 2: TEMPLE GENERATOR ---
function startNextTemple() {
    // 1. Pick a random Kunju that hasn't been visited
    const availableKunjus = gameState.gameData.kunjus.filter(k => !gameState.visitedKunjus.includes(k));
    
    if (availableKunjus.length === 0) {
        startBossBattle(); // END GAME TRIGGER
        return;
    }

    const nextKunjuName = availableKunjus[Math.floor(Math.random() * availableKunjus.length)];
    gameState.currentKunju = nextKunjuName;
    gameState.location = "temple";
    gameState.subLocation = "entrance";
    
    // Reset temple specific flags
    gameState.templeData = {
        hasKey: false,
        doorUnlocked: false,
        cardCollected: false,
        chestOpen: false
    };

    // Show Lore Screen (Transition)
    ui.clearOptions();
    ui.text(`<br>--- LORE OF ${nextKunjuName.toUpperCase()} ---<br>The Realm: ${gameState.gameData.realms[nextKunjuName]}<br>Approaching destination...`);
    
    setTimeout(renderTempleEntrance, 3000);
}

function renderTempleEntrance() {
    gameState.subLocation = "entrance";
    ui.text(`--- ENTERING TEMPLE OF ${gameState.currentKunju.toUpperCase()} ---<br>Moss covers ancient stone walls. You hear chants: 'Owh Yeah! Kunji on the loose!'`);
    
    ui.clearOptions();
    // Only North is valid
    ui.setDPad(() => renderAntechamber(), null, null, null); 
    ui.addOption("Inspect Walls", () => ui.text("Ancient writings you cannot decipher."));
}

function renderAntechamber() {
    gameState.subLocation = "antechamber";
    ui.text("You are in a dimly lit Antechamber.<br>A locked chest rests against the west wall.<br>Exits: North, South.");

    ui.clearOptions();
    ui.setDPad(
        () => renderSanctum(), // North
        () => renderTempleEntrance(), // South
        null, null
    );

    if (!gameState.templeData.chestOpen) {
        ui.addOption("Open Chest", triggerChestRiddle, "lock");
    } else {
        ui.addOption("Inspect Chest", () => ui.text("It is empty. You already have the key."), "lock_open");
    }
}

function triggerChestRiddle() {
    // Determine which riddle to use based on Kunju
    // SIMPLIFIED FOR DEMO: Using a generic riddle or pulling from logic if we had the python logic fully mapped
    // Ideally we map `minigames.py` logic here.
    
    ui.text("THE CHEST IS LOCKED. <br>Riddle: 'Who teaches Kamehameha to Goku?'");
    
    ui.clearOptions();
    // creating fake multiple choice for the 'input' style of the python game
    ["Vegeta", "Roshi", "Piccolo", "Sama-Ji"].forEach(ans => {
        ui.addOption(ans, () => {
            if (ans === "Roshi") {
                ui.text("The chest clicks open! You pocket the **Temple Key**. Owh Yeah!");
                gameState.templeData.hasKey = true;
                gameState.templeData.chestOpen = true;
                gameState.inventory.push("Temple Key");
                renderAntechamber(); // Refresh view
            } else {
                ui.text("The chest remains sealed. Wrong answer.");
                renderAntechamber();
            }
        });
    });
}

function renderSanctum() {
    gameState.subLocation = "sanctum";
    ui.text("You move North to the Sanctum.<br>Floating tomes swirl. A Sealed Door bars your path.<br>The Knowledge Altar stands in the center.");

    ui.clearOptions();
    ui.setDPad(
        null, // North blocked by door
        () => renderAntechamber(), // South
        null, null
    );

    // Contextual Actions
    ui.addOption("Inspect Altar", () => {
        if (!gameState.templeData.cardCollected) {
            ui.text(`You find the **Limited Edition TCG Card of ${gameState.currentKunju}**! Owh Yeah!`);
            gameState.templeData.cardCollected = true;
            gameState.inventory.push(`${gameState.currentKunju} Card`);
        } else {
            ui.text("The altar is empty. You have the card.");
        }
    }, "style");

    ui.addOption("Inspect Sealed Door", () => {
        ui.text(gameState.templeData.doorUnlocked ? "The door is open." : "It is sealed with glowing runes.");
    }, "meeting_room");

    if (!gameState.templeData.doorUnlocked) {
        ui.addOption("Use Key on Door", () => {
            if (gameState.templeData.hasKey) {
                ui.text("You use the Temple Key. The runes fade. The path opens!");
                gameState.templeData.doorUnlocked = true;
                // Enable North Movement
                ui.setDPad(() => enterRealm(), () => renderAntechamber(), null, null);
                // Remove this button and refresh
                setTimeout(renderSanctum, 1000);
            } else {
                ui.text("You don't have a key!");
            }
        }, "key");
    } else {
        // If unlocked, show Enter button
         ui.addOption("ENTER PORTAL", enterRealm, "login");
    }
}

// --- SCENE 3: REALM GENERATOR ---
function enterRealm() {
    gameState.location = "realm";
    gameState.subLocation = "heart";
    const realmName = gameState.gameData.realms[gameState.currentKunju];
    
    ui.text(`You pass through the threshold...<br><br>--- ENTERING REALM OF ${realmName.toUpperCase()} ---<br>Reality bends around you.`);
    
    setTimeout(renderRealmHeart, 2000);
}

function renderRealmHeart() {
    ui.text("You stand in the HEART of the Realm.<br>A glowing Sigil floats before you.<br>Exits: Forward (Blocked), Back.");
    
    ui.clearOptions();
    
    // Check if puzzle solved
    if (gameState.templeData.sigilSolved) {
        ui.text("The Sigil is dormant. The path forward is open.");
        ui.setDPad(() => renderPortalChamber(), null, null, null);
    } else {
        ui.setDPad(null, null, null, null);
        ui.addOption("Inspect/Solve Sigil", triggerSigilMinigame, "extension");
    }
}

function triggerSigilMinigame() {
    // This connects to the minigames.js file
    // We assume minigames.js exposes a function or we inline it here
    // For now, let's simulate the Card Match from the transcript
    
    ui.text("SIGIL CHALLENGE: Memory Match.<br>X <-> Y<br>Match found!");
    
    setTimeout(() => {
        ui.text("Challenge Completed! You collect a Realm Fragment.");
        gameState.templeData.sigilSolved = true;
        gameState.inventory.push("Realm Fragment");
        
        // Trigger Secret Room Sequence (As per transcript)
        triggerSecretRoomSequence();
    }, 1500);
}

function triggerSecretRoomSequence() {
    ui.text("--- A hidden space cracks open in the emptiness... ---<br>You feel compelled to explore it.");
    
    // Mocking the sequence: Beginnings -> Middles -> Hall
    let roomIndex = 0;
    const rooms = ["The Beginnings", "The Middles", "Hall of Prophecy"];
    
    function nextSecretRoom() {
        if (roomIndex >= rooms.length) {
            ui.text("You return to the Heart.");
            renderRealmHeart();
            return;
        }
        
        ui.text(`--- SECRET ROOM: ${rooms[roomIndex]} ---<br>Sacred texts line the walls.`);
        ui.clearOptions();
        ui.addOption("Inspect Books", () => ui.text("You read ancient lore about Owh Yeah."));
        ui.addOption("Leave Room", () => {
            roomIndex++;
            nextSecretRoom();
        }, "logout");
    }
    
    setTimeout(nextSecretRoom, 2000);
}

function renderPortalChamber() {
    ui.text("You move forward to the Portal Chamber.<br>A swirling portal hums with power.");
    
    ui.clearOptions();
    ui.addOption("ENTER PORTAL", () => {
        ui.text("You step into the portal...");
        gameState.visitedKunjus.push(gameState.currentKunju);
        
        // Loop back to next temple
        setTimeout(startNextTemple, 3000);
    }, "all_inclusive");
}

function startBossBattle() {
    ui.text("--- DIMENSION 69 ---<br>All Kunjus collected.<br>Ste'vi Ra and Veesus await.");
    // Connect to CombatEngine here
    new CombatEngine(gameState.gameData, () => ui.text("YOU WIN"), () => ui.text("YOU DIED")).startCombat();
}

// Start the engine
document.addEventListener('DOMContentLoaded', initGame);