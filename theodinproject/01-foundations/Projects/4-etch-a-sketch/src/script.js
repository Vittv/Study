// Default grid value
let totalDiv = 16;

const newInput = document.querySelector(".numberInput");
const gridContainer = document.querySelector('.new-grid-container');
const makeSquares = document.querySelector(".make-squares-btn");
const clearButton = document.querySelector(".clear-btn");
const resetButton = document.querySelector(".reset-btn");
const blackColorButton = document.querySelector(".black-color-btn");
const randomColorButton = document.querySelector(".random-color-btn");
const opacityIncreaseButton = document.querySelector(".opacity-increase-btn");
const randomAndOpacityButton = document.querySelector(".random-and-opacity-btn")

// Automatically focus the input field when the page loads
document.addEventListener("DOMContentLoaded", () => {
    newInput.focus();
});

// Event listeners
// Click event for makeSquares button
makeSquares.addEventListener("click", () => {
    const newValue = parseInt(newInput.value, 10) || 16; // Default to 16
    readInput(newValue);
    document.querySelector(".current-input").textContent = `Scale: ${newValue} x ${newValue}`;
    newInput.value = "";
    document.querySelector(".current-color-mode").innerText = `Mode: Black`;
});

// Resets back to default mode
resetButton.addEventListener("click", () => {
    totalDiv = 16;
    document.querySelector(".current-input").textContent = `Scale: ${totalDiv} x ${totalDiv}`;
    newInput.value = "";
    makeNewGrid(totalDiv);
    document.querySelector(".current-color-mode").innerText = `Mode: Black`;
});

// Keydown event for the input field
newInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        const newValue = parseInt(newInput.value, 10) || 16; // Default to 16;
        readInput(newValue);
        newInput.value = "";
        document.querySelector(".current-input").textContent = `Scale: ${newValue} x ${newValue}`;
        document.querySelector(".current-color-mode").innerText = `Mode: Black`
    }
});

// Change to color black
blackColorButton.addEventListener("click", () => {
    makeNewGrid(totalDiv, "black");
    document.querySelector(".current-color-mode").innerText = `Mode: Black`;
});

// Change to random color
randomColorButton.addEventListener("click", () => {
    makeNewGrid(totalDiv, "random");
    document.querySelector(".current-color-mode").innerText = `Mode: Random`;
});

// Clear board
clearButton.addEventListener("click", () => {
    makeNewGrid(totalDiv, currentColorMode);
});

// Change to opacity black
opacityIncreaseButton.addEventListener("click", () => {
    makeNewGrid(totalDiv, "opacity-black");
    document.querySelector(".current-color-mode").innerText = `Mode: Opacity Black`;
});

// Change to opacity random color
randomAndOpacityButton.addEventListener("click", () => {
    makeNewGrid(totalDiv, "random-opacity");
    document.querySelector(".current-color-mode").innerText = `Mode: Opacity Random`;
})

// Generate a random RGB color
function getRandomColor() {
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
};

// Clear and regenerate the grid with the current settings
function clearBoard() {
    gridContainer.innerHTML = ""; // Clear the grid container
    makeNewGrid(totalDiv, currentColorMode);
};

let currentColorMode = "black";

// Generate the grid
function makeNewGrid(totalDiv, colorMode = "black") {
    gridContainer.innerHTML = ""; // Clear previous grid
    currentColorMode = colorMode; // Update the current color mode

    // Create and append the squares
    for (let i = 0; i < totalDiv * totalDiv; i++ ) {
        const newGrid = document.createElement("div");
        newGrid.className = "new-grid";
        newGrid.setAttribute("data-opacity", 0); // Initialize opacity at 0
        gridContainer.appendChild(newGrid)
    };
    // Resize every square dynamically so it fits inside the given field
    function resizeSquares(totalDiv) {
        const allSquares = document.querySelectorAll(".new-grid"); // Select all squares
        const squareSize = 700 / totalDiv; // Calculate size per square

        allSquares.forEach(square => {
            square.style.width = `${squareSize}px`;
            square.style.height = `${squareSize}px`;
        });
    };

    // Black or Random color hover effect
    function changeColorOnHover(mode) {
        const allSquares = document.querySelectorAll(".new-grid");
        allSquares.forEach(square => {
            square.addEventListener("mouseover", () => {
                square.style.backgroundColor =
                    mode === "black" ? "black" : getRandomColor();
            });
        });
    };

    // Opacity Black or Random color hover effect
    function changeColorOnHoverOpacity(mode) {
        const allSquares = document.querySelectorAll(".new-grid");
    
        allSquares.forEach(square => {
            // Initialize the opacity attribute if not present
            if (!square.getAttribute("data-opacity")) {
                square.setAttribute("data-opacity", "0");
            }
    
            square.addEventListener("mouseover", () => {
                let currentOpacity = parseFloat(square.getAttribute("data-opacity"));
    
                // Increment opacity, max at 1
                if (currentOpacity < 1) {
                    currentOpacity += 0.1; // Increase opacity
                    square.setAttribute("data-opacity", currentOpacity); // Update data attribute
    
                    if (mode === "black") {
                        square.style.backgroundColor = `rgba(0, 0, 0, ${currentOpacity})`; // Black with varying opacity
                    } else if (mode === "random") {
                        const r = Math.floor(Math.random() * 256);
                        const g = Math.floor(Math.random() * 256);
                        const b = Math.floor(Math.random() * 256);
                        square.style.backgroundColor = `rgba(${r}, ${g}, ${b}, ${currentOpacity})`; // Random color with opacity
                    }
                }
            });
        });
    };
    

    // Apply the hover effect based on the current color mode
    if (colorMode === "black") {
        changeColorOnHover("black");
    } else if (colorMode === "random") {
        changeColorOnHover("random");
    } else if (colorMode === "opacity-black") {
        changeColorOnHoverOpacity("black");
    } else if (colorMode === "random-opacity") {
        changeColorOnHoverOpacity("random");
    }
    // Make sure it fits inside the grid-container
    resizeSquares(totalDiv);
};

// Prevent the input from being lower than 0 and higher than 100
function validateInput(input) {
    // Remove non-numeric characters
    input.value = input.value.replace(/[^0-9]/g, "");

    // Enforce max value of 100
    if (input.value > 100) {
        input.value = 100;
    }
};

// Remake the grid with value given by the user
function readInput(newValue) {
    totalDiv = newValue;
    makeNewGrid(totalDiv);
};

// Default grid and mode starting as you open the application
makeNewGrid(totalDiv, "black");

// Todo:
// 01. Make the input change the number of squares made                           DONE
// 02. Make the squares change size to fit in the 700x700 grid-container we made  DONE
// 03. Implement hover for default color                                          DONE                                         
// 04. Implement Random Colors function                                           DONE
// 05. Implement Opacity Increase function                                        DONE
// 06. Implement Random Colors + Opacity Increase function                        DONE
// 07. Finish design                                                              DONE
// 08. Push and enable live preview                                               DONE