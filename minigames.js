// minigames.js
function danceOff(gameData, onWin, onLose) {
    const seq = gameData.pickle_dance_seqs[Math.floor(Math.random() * gameData.pickle_dance_seqs.length)];
    let playerSeq = [];

    function showDance() {
        const instructions = `
            <p class="text-xl text-primary mb-4">DANCE PROTOCOL INITIATED</p>
            <p>Match this sequence pattern:</p>
            <div class="text-2xl font-bold tracking-widest my-4 text-cyan-400 border border-cyan-500/30 p-2 inline-block rounded">${seq.join(' -> ').toUpperCase()}</div>
            <p class="text-sm text-gray-400">Current Input: <span class="text-white">${playerSeq.join(' -> ').toUpperCase()}</span></p>
        `;
        window.updateUI.showText(instructions);

        const moves = ['left', 'up', 'right', 'down'];
        window.updateUI.showOptions(moves.map(move => ({
            text: move.toUpperCase(),
            action: () => danceMove(move)
        })));
    }

    function danceMove(move) {
        playerSeq.push(move);
        
        // Immediate check for wrong move
        if (playerSeq[playerSeq.length - 1] !== seq[playerSeq.length - 1]) {
            window.updateUI.showText("<span class='text-red-500 text-xl'>RHYTHM MISMATCH.</span><br><br>You stumbled on the dance floor.");
            setTimeout(onLose, 2000);
            return;
        }

        if (playerSeq.length === seq.length) {
            window.updateUI.showText("<span class='text-primary text-xl'>SYNCHRONIZATION 100%.</span><br><br>The crowd goes wild! Owh Yeah!");
            setTimeout(onWin, 2000);
            return;
        }

        showDance();
    }

    showDance();
}

function trivia(gameData, onWin, onLose) {
    const questions = gameData.one_piece_trivia;
    let currentQuestionIndex = 0;
    let correctAnswers = 0;

    function showQuestion() {
        if (currentQuestionIndex >= 4) { // Only ask 4 questions
            if (correctAnswers === 4) {
                window.updateUI.showText(`Score: ${correctAnswers}/4.<br><span class="text-primary text-xl">KNOWLEDGE VERIFIED.</span>`);
                setTimeout(onWin, 2000);
            } else {
                window.updateUI.showText(`Score: ${correctAnswers}/4.<br><span class="text-red-500 text-xl">INSUFFICIENT DATA.</span><br>Study more, Sama-Ji.`);
                setTimeout(onLose, 2000);
            }
            return;
        }

        const question = questions[currentQuestionIndex];
        
        window.updateUI.showText(`<span class="text-cyan-400">QUERY ${currentQuestionIndex + 1}/4:</span><br><br>${question.q}`);

        const options = question.options.map(opt => ({
            text: opt,
            action: () => {
                if (opt === question.a) correctAnswers++;
                currentQuestionIndex++;
                showQuestion();
            }
        }));
        
        window.updateUI.showOptions(options);
    }

    showQuestion();
}