let price = 1.87;
let cid = [
  ["PENNY", 1.01],
  ["NICKEL", 2.05],
  ["DIME", 3.1],
  ["QUARTER", 4.25],
  ["ONE", 90],
  ["FIVE", 55],
  ["TEN", 20],
  ["TWENTY", 60],
  ["ONE HUNDRED", 100]
];

const coinValues = {
  "PENNY": 0.01,
  "NICKEL": 0.05,
  "DIME": 0.1,
  "QUARTER": 0.25,
  "ONE": 1,
  "FIVE": 5,
  "TEN": 10,
  "TWENTY": 20,
  "ONE HUNDRED": 100
};

document.getElementById("price-screen").innerHTML = `Total: $${price}`;

const formatAmount = (amount) => {
  return amount % 1 === 0 ? amount.toString() : amount.toFixed(2);
};

// Displays cid on screen for the user
const displayCashDrawer = () => {
  document.getElementById("pennies").innerHTML = `Pennies: $${formatAmount(cid[0][1])}`;
  document.getElementById("nickels").innerHTML = `Nickels: $${formatAmount(cid[1][1])}`;
  document.getElementById("dimes").innerHTML = `Dimes: $${formatAmount(cid[2][1])}`;
  document.getElementById("quarters").innerHTML = `Quarters: $${formatAmount(cid[3][1])}`;
  document.getElementById("ones").innerHTML = `Ones: $${formatAmount(cid[4][1])}`;
  document.getElementById("fives").innerHTML = `Fives: $${formatAmount(cid[5][1])}`;
  document.getElementById("tens").innerHTML = `Tens: $${formatAmount(cid[6][1])}`;
  document.getElementById("twenties").innerHTML = `Twenties: $${formatAmount(cid[7][1])}`;
  document.getElementById("hundreds").innerHTML = `Hundreds: $${formatAmount(cid[8][1])}`;
};

const checkChange = (cash, price) => {
  let changeDue = cash - price;
  let changeBreakdown = [];

  if (cash < price) {
    alert("Customer does not have enough money to purchase the item");
    return;
  }

  if (cash === price) {
    document.getElementById("change-due").innerHTML = "No change due - customer paid with exact cash";
    return;
  }

  let totalCashInDrawer = cid.reduce((acc, curr) => acc + curr[1], 0);

  if (totalCashInDrawer < changeDue) {
    document.getElementById("change-due").innerHTML = `Status: INSUFFICIENT_FUNDS`;
    return;
  }

  for (let i = cid.length - 1; i >= 0; i--) {
    
    let coinName = cid[i][0];
    let coinTotal = cid[i][1];
    let coinValue = coinValues[coinName];

    let count = Math.min(Math.floor(changeDue / coinValue), coinTotal / coinValue);

    if (count > 0) {

      changeBreakdown.push([coinName, count * coinValue]);
      changeDue -= count * coinValue;
      changeDue = Math.round(changeDue * 100) / 100;
      cid[i][1] -= count * coinValue; // Subtract from drawer

    }
  }

  if (changeDue > 0) {
    document.getElementById("change-due").innerHTML = "Status: INSUFFICIENT_FUNDS";
    return;
  }

  if (cid.every(item => item[1] === 0)) {
    let changeHtml = `STATUS: CLOSED<br>`;
    changeBreakdown.forEach(item => {
      changeHtml += `${item[0]}: $${formatAmount(item[1])}<br>`;
    });
    document.getElementById("change-due").innerHTML = changeHtml;

  } else {
    let changeHtml = `STATUS: OPEN<br>`;
    changeBreakdown.forEach(item => {
      changeHtml += `${item[0]}: $${formatAmount(item[1])}<br>`;
    });
    document.getElementById("change-due").innerHTML = changeHtml;
  }
};

document.getElementById("purchase-btn").addEventListener("click", () => {
  let cash = parseFloat(document.getElementById("cash").value);
  checkChange(cash, price);
  displayCashDrawer();
});

displayCashDrawer();