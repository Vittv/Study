const numberInput = document.getElementById("number");
const convertBtn = document.getElementById("convert-btn");
const output = document.getElementById("output");


const decimalToRoman = (input) => {
    const romanSymbols = [
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1]
    ];

    let result = "";

    for (const [symbol, value] of romanSymbols) {
        
        while (input >= value) {
            result += symbol;
            input -= value;
        }
    }

    return result;

};


const checkUserInput = () => {
    const inputStr = numberInput.value;
    const inputInt = parseInt(inputStr);

  if (inputStr === "" || isNaN(inputInt)) {
    output.textContent = "Please enter a valid number.";
    output.classList.remove("hidden");
    output.classList.add("alert");
    return;
  }

  if (inputInt < 1) {
      output.textContent = "Please enter a number greater than or equal to 1";
      output.classList.remove("hidden");
      output.classList.add("alert");
      return;
  }

  if (inputInt > 3999) {
      output.textContent = "Please enter a number less than or equal to 3999";
      output.classList.remove("hidden");
      output.classList.add("alert");
      return;
  }

  output.textContent = decimalToRoman(inputInt);
  output.classList.remove("hidden");
  output.classList.remove("alert")

};

convertBtn.addEventListener("click", checkUserInput);

numberInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    checkUserInput();
  }
});
