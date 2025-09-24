// Pig Game for two players, playable in a web browser

let scores = [0, 0];
let currentPlayer = 0;
let roundTotal = 0;
let gameActive = true;

function updateUI() {
    document.getElementById("score1").textContent = scores[0];
    document.getElementById("score2").textContent = scores[1];
    document.getElementById("current-player").textContent = `Player ${currentPlayer + 1}`;
    document.getElementById("round-total").textContent = roundTotal;
}

function rollDice() {
    if (!gameActive) return;
    let num = Math.floor(Math.random() * 6) + 1;
    document.getElementById("dice").textContent = `You rolled: ${num}`;
    if (num === 1) {
        scores[currentPlayer] = 0;
        roundTotal = 0;
        alert(`Player ${currentPlayer + 1}: You lost ALL of your points!`);
        nextPlayer();
    } else {
        roundTotal += num;
        updateUI();
    }
}

function savePoints() {
    if (!gameActive) return;
    scores[currentPlayer] += roundTotal;
    roundTotal = 0;
    updateUI();
    if (scores[currentPlayer] >= 100) {
        gameActive = false;
        alert(`Congratulations Player ${currentPlayer + 1}, you won with ${scores[currentPlayer]} points!`);
    } else {
        nextPlayer();
    }
}

function nextPlayer() {
    roundTotal = 0;
    currentPlayer = currentPlayer === 0 ? 1 : 0;
    updateUI();
}

function resetGame() {
    scores = [0, 0];
    currentPlayer = 0;
    roundTotal = 0;
    gameActive = true;
    document.getElementById("dice").textContent = "";
    updateUI();
}

window.onload = function() {
    document.body.innerHTML = `
        <h2>Pig Game - Two Players</h2>
        <div>
            <strong>Player 1 Score:</strong> <span id="score1">0</span><br>
            <strong>Player 2 Score:</strong> <span id="score2">0</span><br>
            <strong>Current player:</strong> <span id="current-player">Player 1</span><br>
            <strong>Total this round:</strong> <span id="round-total">0</span><br>
            <span id="dice"></span>
        </div>
        <button onclick="rollDice()">Roll the die</button>
        <button onclick="savePoints()">Save points</button>
        <button onclick="resetGame()">Restart</button>
    `;
    updateUI();
};
