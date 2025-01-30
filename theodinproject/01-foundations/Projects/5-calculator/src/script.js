const numberButtons = document.querySelectorAll(".number");
const operatorButtons = document.querySelectorAll(".operator");
const operationTop = document.querySelector(".operation");
const displayBottom = document.querySelector(".display");
const backspaceButton = document.querySelector(".btn-backspace");
const clearButton = document.querySelector(".btn-clear");
const decimalButton = document.querySelector(".btn-decimal");
const equalsButton = document.querySelector(".btn-equals");

const MAX_LENGTH = 16; // Maximum number of digits allowed

let isTypingNewNumber = false;
let firstNumber = null;
let operator = null;
let isResultDisplayed = false;

// Initialize the bottom display with 0
displayBottom.textContent = "0";

// Number buttons
numberButtons.forEach((button) => {
    button.addEventListener("click", () => {
        if (isResultDisplayed) {
            // Clear everything if result is displayed and start fresh
            operationTop.textContent = "";
            displayBottom.textContent = "";
            firstNumber = null;
            operator = null;
            isResultDisplayed = false;
        }

        if (isTypingNewNumber || displayBottom.textContent === "0") {
            displayBottom.textContent = ""; // Clear the bottom for new input
            isTypingNewNumber = false;
        }
        
        // Add the number only if it doesn't exceed the max length
        if (displayBottom.textContent.length < MAX_LENGTH) {
            displayBottom.textContent += button.textContent;
        }
    });
});

// Decimal button
decimalButton.addEventListener("click", () => {
    if (isResultDisplayed) {
        // Clear everything if result is displayed and start fresh
        operationTop.textContent = "";
        displayBottom.textContent = "0";
        firstNumber = null;
        operator = null;
        isResultDisplayed = false;
    }

    // Add a decimal point only if it doesn't already exist in the current number
    if (!displayBottom.textContent.includes(".")) {
        if (isTypingNewNumber || displayBottom.textContent === "0") {
            // If starting a new number or display is empty, add "0." instead of just "."
            displayBottom.textContent = "0.";
            isTypingNewNumber = false;
        } else {
            displayBottom.textContent += ".";
        }
    }
});

// Operator Buttons
operatorButtons.forEach((button) => {
    button.addEventListener("click", () => {
        const currentNumber = parseFloat(displayBottom.textContent);

        // If no number has been entered yet, allow starting with a negative number
        if (firstNumber === null && displayBottom.textContent === "0") {
            if (button.textContent === "-") {
                if (displayBottom.textContent === "-") {
                    return; // Ignore subsequent "-" presses
                }
                displayBottom.textContent = "-"; // Start typing a negative number
                isTypingNewNumber = false; // Continue typing
            }
            return; // Exit early as no operation is yet being performed
        }

        if (operator && firstNumber !== null && !isTypingNewNumber) {
            // If there’s an ongoing operation, calculate the result
            const result = operateNumbers(operator, firstNumber, currentNumber);

            // Update the top display and bottom display with the result
            operationTop.textContent = `${firstNumber} ${operator} ${currentNumber} =`;
            displayBottom.textContent = result;

            // Prepare the result as the first number for the next operation
            firstNumber = result;
            isTypingNewNumber = true; // Ready for the next number
            operator = button.textContent; // Update operator
            operationTop.textContent = `${firstNumber} ${operator}`; // Update with new operation
        } else {
            // Store the first number and operator for a new operation
            firstNumber = currentNumber;
            operator = button.textContent;

            if (!isNaN(firstNumber)) {
                operationTop.textContent = `${firstNumber} ${operator}`;
            }

            isTypingNewNumber = true; // Ready for new number input
        }

        isResultDisplayed = false; // Ensure the result flag is reset
    });
});

// Backspace Button
backspaceButton.addEventListener("click", () => {
    // Backspace functionality for the bottom display
    if (displayBottom.textContent !== "") {
        displayBottom.textContent = displayBottom.textContent.slice(0, -1) || "0"; // Remove the last character 
    }

    // If the displayBottom becomes empty, reset isTypingNewNumber for new input
    if (displayBottom.textContent === "") {
        isTypingNewNumber = true;
    }
});

// Clear button
clearButton.addEventListener("click", () => {
    operationTop.textContent = "";
    displayBottom.textContent = "0";
    firstNumber = null;
    operator = null;
    isTypingNewNumber = false; // Reset
    isResultDisplayed = false; // Reset result display flag
});

// Equals button
equalsButton.addEventListener("click", () => {
    // Only allow the equals button to work if there is a valid operator
    if (operator && operationTop.textContent !== "" && displayBottom.textContent !== "") {
        const secondNumber = parseFloat(displayBottom.textContent);
        const result = operateNumbers(operator, firstNumber, secondNumber);

        // Limit the result length to MAX_LENGTH
        const resultString = result.toString();
        if (resultString.length > MAX_LENGTH) {
            // Truncate or round the result to fit within MAX_LENGTH
            displayBottom.textContent = resultString.slice(0, MAX_LENGTH);
        } else {
            displayBottom.textContent = result;
        }

        operationTop.textContent = `${firstNumber} ${operator} ${secondNumber} =`
        firstNumber = parseFloat(displayBottom.textContent); // Update firstNumber with the result
        isTypingNewNumber = true;
        operator = null;
        isResultDisplayed = true; // Set result display flag
    }
});

// Basic operations
function addTwoNumbers(firstNumber, secondNumber) {
    return firstNumber + secondNumber;
};

function subtractTwoNumbers(firstNumber, secondNumber) {
    return firstNumber - secondNumber;
};

function multiplyTwoNumbers(firstNumber, secondNumber) {
    return firstNumber * secondNumber;
};

function divideTwoNumbers(firstNumber, secondNumber) {
    if (secondNumber === 0) {
        return "Error";
    }
    return firstNumber / secondNumber;
};

// Utility function to round numbers to a maximum of 6 decimal places
function roundToDisplay(number) {
    return parseFloat(number.toFixed(6)); // Round to 6 decimal places and remove trailing zeros
};

// Operating function
function operateNumbers(operator, firstNumber, secondNumber) {
    let result;
    switch (operator) {
        case "+":
            result = addTwoNumbers(firstNumber, secondNumber);
            break;
        case "-":
            result = subtractTwoNumbers(firstNumber, secondNumber);
            break;
        case "x":
            result = multiplyTwoNumbers(firstNumber, secondNumber);
            break;
        case "/":
            result = divideTwoNumbers(firstNumber, secondNumber);
            break;
        default:
            return null;
    }
    return roundToDisplay(result); // Round the result before returning
}

// Keyboard support
document.addEventListener("keydown", (e) => {
    const key = e.key;

    // Handle number keys (0-9)
    if (!isNaN(key)) {
        const button = [...numberButtons].find(btn => btn.textContent === key);
        if (button) button.click();
    }

    // Handle operator keys (+, -, x, /)
    const operatorMap = {
        "+": "+",
        "-": "-",
        "x": "x",
        "/": "/"
    };

    if (operatorMap[key]) {
        const button = [...operatorButtons].find(btn => btn.textContent === operatorMap[key]);
        if (button) button.click();
    }

    // Handle decimal point (.)
    if (key === ".") {
        decimalButton.click();
    }

    // Handle backspace (Backspace)
    if (key === "Backspace") {
        backspaceButton.click();
    }

    // Handle clear (c or Escape key)
    if (key === "Escape") {
        clearButton.click();
    }
    if (key === "c") {
        clearButton.click();
    }

    // Handle equals (= or Enter key)
    if (key === "=" || key === "Enter") {
        equalsButton.click();
    }
});