document.addEventListener("DOMContentLoaded", () => {
	const form = document.querySelector("form");
	const email = document.getElementById("email");
	const country = document.getElementById("country");
	const postal = document.getElementById("postal-code");
	const password = form.querySelectorAll("input[type=\"password\"]")[0];
	const passwordConfirm = form.querySelectorAll("input[type=\"password\"]")[1];

	email.required = true;
	email.type = "email";
	email.setAttribute("autocomplete", "email");

	country.required = true;
	country.pattern = "^[A-Za-z\\s]{2,}$";

	postal.required = true;
	postal.pattern = "^\\d{4,10}$";

	password.required = true;
	password.minLength = 6;

	passwordConfirm.required = true;

	function showMessage(input, message) {
		let msg = input.nextElementSibling;
		if (!msg || !msg.classList.contains("error-message")) {
			msg = document.createElement("div");
			msg.className = "error-message";
			input.after(msg);
		}
		msg.textContent = message;
		msg.style.color = message ? "#c00" : "inherit";
	}

	function clearMessage(input) {
		let msg = input.nextElementSibling;
		if (msg && msg.classList.contains("error-message")) {
			msg.textContent = "";
		}
	}

	email.addEventListener("input", () => {
		if (email.validity.valueMissing) {
			showMessage(email, "Email is required.");
		} else if (email.validity.typeMismatch) {
			showMessage(email, "Please enter a valid email address.");
		} else {
			clearMessage(email);
		}
	});

	country.addEventListener("input", () => {
		if (country.validity.valueMissing) {
			showMessage(country, "Country is required.");
		} else if (country.validity.patternMismatch) {
			showMessage(country, "Country must be at least 2 letters and only contain letters and spaces.");
		} else {
			clearMessage(country);
		}
	});

	postal.addEventListener("input", () => {
		if (postal.validity.valueMissing) {
			showMessage(postal, "Postal code is required.");
		} else if (postal.validity.patternMismatch) {
			showMessage(postal, "Postal code must be 4-10 digits.");
		} else {
			clearMessage(postal);
		}
	});

	password.addEventListener("input", () => {
		if (password.validity.valueMissing) {
			showMessage(password, "Password is required.");
		} else if (password.validity.tooShort) {
			showMessage(password, "Password must be at least 6 characters.");
		} else {
			clearMessage(password);
		}
		passwordConfirm.dispatchEvent(new Event("input"));
	});

	passwordConfirm.addEventListener("input", () => {
		if (passwordConfirm.validity.valueMissing) {
			showMessage(passwordConfirm, "Please confirm your password.");
		} else if (passwordConfirm.value !== password.value) {
			showMessage(passwordConfirm, "Passwords do not match.");
		} else {
			clearMessage(passwordConfirm);
		}
	});

	form.addEventListener("submit", (e) => {
		e.preventDefault();
		let valid = true;
		
		email.dispatchEvent(new Event("input"));
		country.dispatchEvent(new Event("input"));
		postal.dispatchEvent(new Event("input"));
		password.dispatchEvent(new Event("input"));
		passwordConfirm.dispatchEvent(new Event("input"));

		if (!email.checkValidity() || !country.checkValidity() || !postal.checkValidity() || !password.checkValidity() || !passwordConfirm.checkValidity()) {
			valid = false;
		}

		if (valid) {
			[ email, country, postal, password, passwordConfirm ].forEach(clearMessage);
			let highfive = document.getElementById("highfive");
			if (!highfive) {
				highfive = document.createElement("div");
				highfive.id = "highfive";
				highfive.style.color = "green";
				highfive.style.fontWeight = "bold";
				highfive.style.marginTop = "1rem";
				form.after(highfive);
			}
			highfive.textContent = "🖐 High five! All fields are valid.";
		} else {
			let highfive = document.getElementById("highfive");
			if (highfive) highfive.textContent = "";
		}
	});
});