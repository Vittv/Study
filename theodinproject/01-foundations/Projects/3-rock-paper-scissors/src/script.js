let playerScore = 0;
let charlotteScore = 0;
let playerChoice = "";
let charlotteChoice = "";
let playCount = 0;
let gameOver = false;

const rockButton = document.querySelector(".rock-btn");
const paperButton = document.querySelector(".paper-btn");
const scissorsButton = document.querySelector(".scissors-btn");
const roundCount = document.querySelector(".round-count");

rockButton.addEventListener("click", () => handlePlayerChoice(".rock-btn"));
paperButton.addEventListener("click", () => handlePlayerChoice(".paper-btn"));
scissorsButton.addEventListener("click", () => handlePlayerChoice(".scissors-btn"));

// Saves the Player's choice and plays a round
function handlePlayerChoice(buttonClass) {
    if (gameOver) return; // Stop the game if the game is over

    getPlayerChoice(buttonClass);
    playCount++;
    roundCount.innerText = `Round: ${playCount}`;
    playRound();
    // End the game if a player reaches 5 points first
    if (playerScore === 5 || charlotteScore === 5) {
        gameOver = true;
        gameResults();
    }
};

// Generates 3 random numbers
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
};

// Gathers the Player's choice and returns its value
function getPlayerChoice(buttonClass) {
    if (buttonClass === ".rock-btn") {
        playerChoice = "Rock";
        console.log(`You chose ${playerChoice}`)
        document.querySelector(".player-choice").innerHTML = `You chose <strong>${playerChoice}</strong>`;
        return playerChoice        
    }
    else if (buttonClass === ".paper-btn") {
        playerChoice = "Paper";
        console.log(`You chose ${playerChoice}`)
        document.querySelector(".player-choice").innerHTML = `You chose <strong>${playerChoice}</strong>`;
        return playerChoice      
    }
    else if (buttonClass === ".scissors-btn") {
        playerChoice = "Scissors";
        console.log(`You chose ${playerChoice}`)
        document.querySelector(".player-choice").innerHTML = `You chose <strong>${playerChoice}</strong>`;
        return playerChoice      
    };
};

// Gathers Charlotte's choice and returns its value
function getCharlotteChoice() {
    let charlotteNumber = getRandomInt(3);
    if (charlotteNumber == 0) {
        charlotteChoice = "Rock";
        console.log(`Charlotte chose ${playerChoice}`)
        document.querySelector(".charlotte-choice").innerHTML = `Charlotte chose <strong>${charlotteChoice}</strong>`;
        return charlotteChoice
    }
    else if (charlotteNumber == 1) {
        charlotteChoice = "Paper";
        console.log(`Charlotte chose ${playerChoice}`)
        document.querySelector(".charlotte-choice").innerHTML = `Charlotte chose <strong>${charlotteChoice}</strong>`;
        return charlotteChoice
    }
    else if (charlotteNumber == 2) {
        charlotteChoice = "Scissors";
        console.log(`Charlotte chose ${playerChoice}`)
        document.querySelector(".charlotte-choice").innerHTML = `Charlotte chose <strong>${charlotteChoice}</strong>`;
        return charlotteChoice
    };
};

// Handles the round's logic and returns its outcome
function getRoundResult() {
    getCharlotteChoice();

    if (playerChoice === charlotteChoice) {
        console.log("It's a tie")
        document.querySelector(".round-result").innerText = "It's a tie"
    } else if (
        (playerChoice === "Rock" && charlotteChoice === "Scissors") ||
        (playerChoice === "Paper" && charlotteChoice === "Rock") ||
        (playerChoice === "Scissors" && charlotteChoice === "Paper")
    ) { 
        console.log("You win");
        document.querySelector(".round-result").innerText = "You win"
        playerScore++; // +1 player score
        document.querySelector(".player-score").innerText = `You: ${playerScore}`;          
    } else {
        console.log("Charlotte wins");
        document.querySelector(".round-result").innerText = "Charlotte wins"
        charlotteScore++; // + 1 charlotte score
        document.querySelector(".charlotte-score").innerText = `Charlotte: ${charlotteScore}`; 
    };
};

// Plays a round
function playRound() {
    getRoundResult();
};

// Updates results
function gameResults() {
    if (playerScore > charlotteScore) {
    document.querySelector(".match-result").innerText = "You've won this match"
    return
    } else if (charlotteScore > playerScore) {
        document.querySelector(".match-result").innerText = "Charlotte wins the match"
    } else {
        document.querySelector(".match-result").innerText = "Draw"
    }
}

// Resets game
function resetGame() {
    playerScore = 0;
    charlotteScore = 0;
    playerChoice = `your <strong>choice</strong>`;
    charlotteChoice = `charlotte's <strong>choice</strong>`;
    playCount = 0;
    gameOver = false; // Reset gameOver so the game can restart
    document.querySelector(".round-count").innerText = `Round: ${playCount}`;
    document.querySelector(".player-choice").innerHTML = `${playerChoice}`;
    document.querySelector(".charlotte-choice").innerHTML = `${charlotteChoice}`;
    document.querySelector(".player-score").innerText = `You: ${playerScore}`;
    document.querySelector(".charlotte-score").innerText = `Charlotte: ${charlotteScore}`;
    document.querySelector(".round-result").innerText = "round result";
    document.querySelector(".match-result").innerText = "match winner";
}

// Plays the game
function startGame() {
    playRound();
};

// Button to reset the game
document.querySelector(".play-again").addEventListener("click", () => playAgain())
function playAgain() {
    resetGame();
}