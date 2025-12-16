async function main() {
    const response = await fetch('game_data.json');
    const gameData = await response.json();

    const dialogueBox = document.getElementById('dialogue-box');
    const optionsBox = document.getElementById('options-box');

    function showText(text) {
        dialogueBox.innerHTML = text;
    }

    function showOptions(options) {
        optionsBox.innerHTML = '';
        for (const option of options) {
            const button = document.createElement('button');
            button.innerText = option.text;
            button.onclick = option.action;
            optionsBox.appendChild(button);
        }
    }

    function startGame() {
        showText("Choose an activity.");
        showOptions([
            { text: "Dance Off", action: () => danceOff(gameData, startGame, startGame) },
            { text: "Trivia", action: () => trivia(gameData, startGame, startGame) },
            { text: "Combat", action: () => new CombatEngine(gameData, startGame, startGame).startCombat() }
        ]);
    }

    startGame();
}

main();
