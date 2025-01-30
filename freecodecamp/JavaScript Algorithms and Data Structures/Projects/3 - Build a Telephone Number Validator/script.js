const validatePhoneNumber = () => {
    const phoneNumber = document.getElementById("user-input").value.trim();
    const resultDiv = document.getElementById("results-div");
    console.log("Phone Number Entered:", phoneNumber);

    const regex = /^(?:\+?1\s?)?(?:\(\d{3}\)|\d{3})[\s.-]?\d{3}[\s.-]?\d{4}$/;
    console.log("Regex Test Result:", regex.test(phoneNumber));

    if (!phoneNumber) {
        alert("Please provide a phone number");
        return;
    }

    const validationResult = regex.test(phoneNumber) ? `Valid US number: ${phoneNumber}` : `Invalid US number: ${phoneNumber}`;
    const resultElement = document.createElement("p");
    resultElement.textContent = validationResult;
    
    if (regex.test(phoneNumber)) {
        resultElement.style.color = "#e8efff";
    }
    else {
        resultElement.style.color = "#dbd0c8";
    }

    resultDiv.appendChild(resultElement);
    document.getElementById('user-input').value = '';
}

const clearInput = () => {
    document.getElementById('user-input').value = '';
}

document.getElementById("check-btn").addEventListener("click", validatePhoneNumber);
document.getElementById("clear-btn").addEventListener("click", () => {
    document.getElementById("results-div").textContent = "";
    clearInput();
});

document.getElementById("user-input").addEventListener("keypress", (event) => {
    if (event.key === "Enter") {
        validatePhoneNumber();
    }
});