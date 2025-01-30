const numberInput = document.getElementById("number-input");
const convertBtn = document.getElementById("convert-btn");
const result = document.getElementById("result");


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
            num -= value;
        }
    }

    return result;

};



const checkUserInput = () => {
    const inputInt = parseInt(numberInput.value);
  
    if (!numberInput.value || isNaN(inputInt) || inputInt < 0) {
      alert("Please provide a decimal number greater than or equal to 0");
      return;
    }
  
    result.textContent = decimalToRoman(inputInt);
    numberInput.value = "";
};

convertBtn.addEventListener("click", checkUserInput);

numberInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    checkUserInput();
  }
});
