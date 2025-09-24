// Pig Game for two players, playable in a web browser

let scores = [0, 0];
let currentPlayer = 0;
let roundTotal = 0;
let gameActive = true;

function updateUI() {
    document.getElementById("score1").textContent = scores[0];
    document.getElementById("score2").textContent = scores[1];
    document.getElementById("current-player").textContent = `Spelare ${currentPlayer + 1}`;
    document.getElementById("round-total").textContent = roundTotal;
}

function rollDice() {
    if (!gameActive) return;
    let num = Math.floor(Math.random() * 6) + 1;
    document.getElementById("dice").textContent = `Du kastade: ${num}`;
    if (num === 1) {
        scores[currentPlayer] = 0;
        roundTotal = 0;
        alert(`Spelare ${currentPlayer + 1}: Du tappade ALLA dina poäng!`);
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
        alert(`Grattis Spelare ${currentPlayer + 1}, du vann med ${scores[currentPlayer]} poäng!`);
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
        <h2>Pig Game - Två spelare</h2>
        <div>
            <strong>Spelare 1 Poäng:</strong> <span id="score1">0</span><br>
            <strong>Spelare 2 Poäng:</strong> <span id="score2">0</span><br>
            <strong>Nuvarande spelare:</strong> <span id="current-player">Spelare 1</span><br>
            <strong>Summa denna runda:</strong> <span id="round-total">0</span><br>
            <span id="dice"></span>
        </div>
        <button onclick="rollDice()">Kasta tärningen</button>
        <button onclick="savePoints()">Spara poäng</button>
        <button onclick="resetGame()">Starta om</button>
    `;
    updateUI();
};