let current_index = 1;
let prev_index = (current_index - 1 + subject_list.length) % subject_list.length;
let next_index = (current_index + 1) % subject_list.length;

console.log(prev_index)
console.log(next_index)

const allRectangles = document.getElementsByClassName('rectangle');
const rectArray = []

for (i = 0; i < allRectangles.length; i++)
{
    rectArray.push(allRectangles[i]);
}

const prevRectangle = rectArray[prev_index];
const currentRectangle = rectArray[current_index];
const nextRectangle = rectArray[next_index];

console.log(prevRectangle.textContent)
console.log(currentRectangle.textContent)
console.log(nextRectangle.textContent)

function updateRectangles()
{
    prevRectangle.textContent = subject_list[prev_index].text;
    currentRectangle.textContent = subject_list[current_index].text;
    nextRectangle.textContent = subject_list[next_index].text;
}

function moveToNext()
{
    /*
    console.log("next detected")
    Array.from(rectArray).forEach(rectangle =>
    {
        rectangle.style.transform = 'translateX(-117%)';
    });

    setTimeout(() => { */
    prev_index = current_index;
    current_index = next_index;
    next_index = (next_index + 1) % subject_list.length;
    updateRectangles();

        /*
        currentRectangle.style.transition = '';
        prevRectangle.style.transition = '';
        nextRectangle.style.transition = '';

        const tempRect = rectArray.shift()
        rectArray.push(tempRect)

    }, 300); */
}

function moveToPrev()
{
    /*
    console.log("prev detected")
    Array.from(allRectangles).forEach(rectangle =>
    {
        rectangle.style.transform = 'translateX(117%)';
    });

    setTimeout(() => { */
    next_index = current_index;
    current_index = prev_index;
    prev_index = (prev_index - 1 + subject_list.length) % subject_list.length;
    updateRectangles();

        /*
        // Reset transitions
        currentRectangle.style.transition = '';
        prevRectangle.style.transition = '';
        nextRectangle.style.transition = '';
    }, 300); */
}

function searchCategory()
{
    window.location.href = `/search/${currentRectangle.innerText}`;
}

prevRectangle.addEventListener('click', moveToPrev);
currentRectangle.addEventListener('click', searchCategory);
nextRectangle.addEventListener('click', moveToNext);
