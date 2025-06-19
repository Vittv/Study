// Reusable dropdown function
function createDropdown({ buttonSelector, contentSelector, toggleClass = "visible" }) {
  	const dropdownButton =
    typeof buttonSelector === "string"
      	? document.querySelector(buttonSelector)
      	: buttonSelector;
  	const dropdownContent =
    typeof contentSelector === "string"
      	? document.querySelector(contentSelector)
      	: contentSelector;

  	if (!dropdownButton || !dropdownContent) return;

  	dropdownButton.addEventListener("click", () => {
    dropdownContent.classList.toggle(toggleClass);
  	});
}

createDropdown({ buttonSelector: ".dropdown-button", contentSelector: ".dropdown-content" })

// Example usage:
// createDropdown({ buttonSelector: ".dropdown-button", contentSelector: ".dropdown-content" });
// You can call createDropdown multiple times for different dropdowns.
