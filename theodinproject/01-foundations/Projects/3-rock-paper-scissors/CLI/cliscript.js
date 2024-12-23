let humanScore = 0;
let computerScore = 0;

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

function formatChoice(usedString) {
    return usedString.charAt(0).toUpperCase() + usedString.slice(1);
}

// Handles the player prompt and gathers their choice
function getHumanChoice() {
    let humanChoice;

    while(true) {
        humanChoice = prompt("Rock, Paper or Scissors?").toLowerCase().trim();

        if (humanChoice === "rock" || 
            humanChoice === "paper" || 
            humanChoice === "scissors") {
            console.log(`You chose ${formatChoice(humanChoice)}!`);
            return humanChoice;
        }
        else {
            alert("Invalid choice! Please enter Rock, Paper or Scissors.")
        }
    }
}

// Generates a random choice for the opponent
function getComputerChoice() {
    let computerNumber = getRandomInt(3);
    let choice;

    if (computerNumber == 0) {
        choice = "rock";
    }
    else if (computerNumber == 1) {
        choice = "paper";
    }
    else {
        choice = "scissors";
    }

    console.log(`I chose ${formatChoice(choice)}!`);
    return choice;
}

// Plays a round and keeps score
function playRound(humanChoice, computerChoice) {
    if (humanChoice === computerChoice) {
        console.log("It's a tie!");
    }
    else if (
        (humanChoice === "rock" && computerChoice === "scissors") ||       
        (humanChoice === "paper" && computerChoice === "rock") ||
        (humanChoice === "scissors" && computerChoice === "paper")
    ) {
        humanScore++;
        console.log("You win this round!");
    }
    else {
        computerScore++;
        console.log("You lose this round!");
    }
    console.log(`Score -> You: ${humanScore} | Computer: ${computerScore}`);
}

// Plays the game totalling 5 rounds and determines win or loss depending on final score
function game() {
    let roundNumber = 1;

    while (roundNumber <= 5){
        console.log(`========== Round ${roundNumber} ==========`);
        let humanChoice = getHumanChoice();
        let computerChoice = getComputerChoice();

        playRound(humanChoice, computerChoice);
        roundNumber++;
    }

    if (humanScore > computerScore) {
        console.log("\nYou win the game!");
    } else if (humanScore < computerScore) {
        console.log("\nYou lose the game!");
    } else {
        console.log("\nIt's a tie game!");
    }
}

game();