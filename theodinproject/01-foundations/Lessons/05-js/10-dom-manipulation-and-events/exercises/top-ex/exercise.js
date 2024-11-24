// Add the following elements to the container using ONLY JavaScript and the DOM methods shown above:

/*
1. a <p> with red text that says “Hey I’m red!”
2. an <h3> with blue text that says “I’m a blue h3!”
3. a <div> with a black border and pink background color with the following elements inside of it:

   - another <h1> that says “I’m in a div”
   - a <p> that says “ME TOO!”
   - Hint for this one: after creating the <div> with createElement, append the <h1> and <p> to it before adding it to the container.

*/

// Starting code

const container = document.querySelector("#container");

const content = document.createElement("div");
content.classList.add("content");
content.textContent = "This is the glorious text-content!";

container.appendChild(content);

// Start here

const paragraph = document.createElement("p");
paragraph.textContent = "Hey I'm red!";
paragraph.style.color = "red";

const headerthree = document.createElement("h3");
headerthree.textContent = "I'm a blue h3!";
headerthree.style.color = "blue";

container.appendChild(paragraph);
container.appendChild(headerthree);

const blackpink = document.createElement("div");
blackpink.style.border = "2px solid black";
blackpink.style.backgroundColor = "pink";

const headerone = document.createElement("h1");
headerone.textContent = "I'm in a div"
const anotherparagraph = document.createElement("p");
anotherparagraph.textContent = "ME TOO!";

blackpink.appendChild(headerone);
blackpink.appendChild(anotherparagraph);

container.appendChild(blackpink);