const rectangles = [
    {
        text: "CSC"
    },
    {
        text: "PHYS"
    },
    {
        text: "MATH"
    },
    {
        text: "BIO"
    },
    {
        text: "HH"
    }
];

let current_index = 0;
let prev_index = (current_index - 1 + rectangles.length) % rectangles.length;
let next_index = (current_index + 1) % rectangles.length;

const prevRectangle = document.getElementById('prev-rectangle');
const currentRectangle = document.getElementById('current-rectangle');
const nextRectangle = document.getElementById('next-rectangle');

function updateRectangles() {
    prevRectangle.textContent = rectangles[prev_index].text;
    currentRectangle.textContent = rectangles[current_index].text;
    nextRectangle.textContent = rectangles[next_index].text;
}

updateRectangles();

function moveToNext() {
    prev_index = current_index;
    current_index = next_index;
    next_index = (next_index + 1) % rectangles.length;
    updateRectangles()
}

function moveToPrev() {
    next_index = current_index;
    current_index = prev_index;
    prev_index = (prev_index - 1 + rectangles.length) % rectangles.length;
    updateRectangles()
}

prevRectangle.addEventListener('click', moveToPrev);
nextRectangle.addEventListener('click', moveToNext);
