function checkPalindrome() {
    var input = document.getElementById("text-input").value.trim();

    if (input === "") {
        alert("Please input a value");
        return;
    }

    var cleanInput = input.toLowerCase().replace(/[^a-z0-9]/g, '');
    var reversed = cleanInput.split('').reverse().join('');

    if (cleanInput === reversed) {
        document.getElementById("result").innerHTML = "<strong>" + input + "</strong> is a palindrome.";
    } else {
        document.getElementById("result").innerHTML = "<strong>" + input + "</strong> is not a palindrome.";
    }
}