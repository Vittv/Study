const colors = ["#e57373", "#64b5f6", "#81c784"];
const carouselScreen = document.querySelector(".carousel-screen");
const leftArrow = document.querySelector(".left-arrow");
const rightArrow = document.querySelector(".right-arrow");
const pages = Array.from(document.querySelectorAll(".carousel-page"));

let current = 0;
let timer;

function setupTrack() {
	let track = carouselScreen.querySelector(".carousel-track");
	if (track) track.remove();
	track = document.createElement("div");
	track.className = "carousel-track";
	colors.forEach((color, i) => {
		const img = document.createElement("div");
		img.className = "carousel-image";
		img.style.background = color;
		img.textContent = `Image ${i + 1}`;
		track.appendChild(img);
	});
	carouselScreen.appendChild(track);
}

function renderCarousel() {
	const track = carouselScreen.querySelector(".carousel-track");
	if (!track) return;
	track.style.transform = `translateX(-${current * 320}px)`;
	pages.forEach((dot, i) => {
		dot.classList.toggle("active", i === current);
	});
}

function goTo(idx) {
	current = (idx + colors.length) % colors.length;
	renderCarousel();
}

leftArrow.textContent = "←";
rightArrow.textContent = "→";

leftArrow.addEventListener("click", () => {
	goTo(current - 1);
	resetTimer();
});
rightArrow.addEventListener("click", () => {
	goTo(current + 1);
	resetTimer();
});
pages.forEach((dot, i) => {
	dot.addEventListener("click", () => {
		goTo(i);
		resetTimer();
	});
});

function resetTimer() {
	clearInterval(timer);
	timer = setInterval(() => goTo(current + 1), 5000);
}

setupTrack();
renderCarousel();
timer = setInterval(() => goTo(current + 1), 5000);

// Pause on hover
carouselScreen.addEventListener('mouseenter', () => clearInterval(timer));
carouselScreen.addEventListener('mouseleave', () => {
	timer = setInterval(() => goTo(current + 1), 5000);
});
