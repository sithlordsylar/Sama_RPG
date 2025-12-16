
function danceOff(gameData, onWin, onLose) {
    const dialogueBox = document.getElementById('dialogue-box');
    const optionsBox = document.getElementById('options-box');

    const seq = gameData.pickle_dance_seqs[Math.floor(Math.random() * gameData.pickle_dance_seqs.length)];
    let playerSeq = [];

    function showDance() {
        dialogueBox.innerHTML = `
            <p>An ancient rhythm pulses and goes 'Ayayayaya'... follow these moves:</p>
            <p>${seq.join(' -> ')}</p>
            <p>Your moves: ${playerSeq.join(' -> ')}</p>
        `;

        optionsBox.innerHTML = '';
        const moves = ['left', 'up', 'right', 'down'];
        for (const move of moves) {
            const button = document.createElement('button');
            button.innerText = move.charAt(0).toUpperCase() + move.slice(1);
            button.addEventListener('click', () => danceMove(move));
            optionsBox.appendChild(button);
        }
    }

    function danceMove(move) {
        playerSeq.push(move);
        if (playerSeq[playerSeq.length - 1] !== seq[playerSeq.length - 1]) {
            dialogueBox.innerHTML += "<p>You falter, but some beat remains within you.</p>";
            setTimeout(onLose, 1000);
            return;
        }

        if (playerSeq.length === seq.length) {
            dialogueBox.innerHTML += "<p>You move in perfect harmony. Owh Yeah!</p>";
            setTimeout(onWin, 1000);
            return;
        }

        showDance();
    }

    showDance();
}

function trivia(gameData, onWin, onLose) {
    const dialogueBox = document.getElementById('dialogue-box');
    const optionsBox = document.getElementById('options-box');
    const questions = gameData.one_piece_trivia;
    let currentQuestionIndex = 0;
    let correctAnswers = 0;

    function showQuestion() {
        if (currentQuestionIndex >= 4) {
            if (correctAnswers === 4) {
                dialogueBox.innerHTML = `<p>You got ${correctAnswers}/4. Owh Yeah!</p>`;
                setTimeout(onWin, 1000);
            } else {
                dialogueBox.innerHTML = `<p>You got ${correctAnswers}/4. Not quite there.</p>`;
                setTimeout(onLose, 1000);
            }
            return;
        }

        const question = questions[currentQuestionIndex];
        dialogueBox.innerHTML = `<p>${question.q}</p>`;

        optionsBox.innerHTML = '';
        for (const option of question.options) {
            const button = document.createElement('button');
            button.innerText = option;
            button.onclick = () => {
                if (option === question.a) {
                    correctAnswers++;
                }
                currentQuestionIndex++;
                showQuestion();
            };
            optionsBox.appendChild(button);
        }
    }

    showQuestion();
}
