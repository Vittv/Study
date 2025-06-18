const dropdownMenu = (() => {
	const dropdownButton = document.querySelector(".dropdown-button");
	const dropdownContent = document.querySelector(".dropdown-content");

	if (!dropdownContent || !dropdownContent) return;

	dropdownButton.addEventListener("click", () => {
		dropdownContent.classList.toggle("visible");
	});
})();
